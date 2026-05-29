#!/usr/bin/env python3
"""Render BPM EP04 v2.1 with Doubao/Volcengine TTS.

Claude CLI claude-opus-4-8 draft via TUI interactive mode,
Gemini CLI gemini-3.1-pro-preview cross-model review (NEEDS_FIX),
3 must-fix + 2 should-fix applied. Natural speed, zh-female-warm.
"""
from __future__ import annotations

import argparse, json, os, re, shlex, subprocess, time
from pathlib import Path

ROOT = Path('/root/documents/BPM_Course/source-pack/week04')
REPO = Path('/root/hermes-agent-podcast-repo/general/bpm-course')
OUT_DIR = Path('/root/.hermes/audio_cache')
ENV_PATH = Path('/root/.hermes/.env')
DOUBAO = Path('/root/.hermes/hermes-agent/venv/bin/doubao-speech')
VOICE = 'zh-female-warm'

PARTS = {
    'single': {
        'episode': 'EP04',
        'title': 'EP04 v2.1 — BPMN 子流程与定时事件 (Claude Opus 4.8 + Gemini review)',
        'input': REPO / 'episode4_tts_script_v2.1.txt',
        'cache': ROOT / 'doubao_cache_v2.1',
        'wav': OUT_DIR / 'BPM_EP04_v2.1_DoubaoTTS_full.wav',
        'mp3': REPO / 'ep4-v2.1.mp3',
        'meta': REPO / 'ep04_v2.1_render_metadata.json',
        'log': ROOT / 'ep04_v2.1_doubao_segment_log.json',
    },
}

def load_env() -> dict[str, str]:
    env = os.environ.copy()
    if ENV_PATH.exists():
        for raw in ENV_PATH.read_text(encoding='utf-8', errors='ignore').splitlines():
            line = raw.strip()
            if not line or line.startswith('#') or '=' not in line: continue
            k, v = line.split('=', 1); k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in env: env[k] = v
    return env

def run(cmd, *, env=None, timeout=120):
    p = subprocess.run(cmd, env=env, text=True, capture_output=True, timeout=timeout)
    if p.returncode != 0:
        msg = (p.stderr or p.stdout or '').strip()
        msg = re.sub(r'(?i)(access[_-]?token|api[_-]?key|authorization)\s*[:=]\s*\S+', r'\1=***', msg)
        raise RuntimeError(f"cmd failed ({p.returncode}): {' '.join(shlex.quote(c) for c in cmd[:5])} ... {msg[:900]}")
    return p

def ffprobe_duration(path):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', str(path)], text=True).strip())

def seconds_to_hhmmss(s):
    h, rem = divmod(int(round(s)), 3600); m, sec = divmod(rem, 60)
    return f'{h:02d}:{m:02d}:{sec:02d}'

def parse_segments(text):
    segs = []
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line: continue
        if line.startswith('A:'): segs.append({'spk': 'A', 'v': VOICE, 'txt': line[2:].strip(), 'ln': n})
        elif line.startswith('B:'): segs.append({'spk': 'B', 'v': VOICE, 'txt': line[2:].strip(), 'ln': n})
        else: raise ValueError(f'unprefixed line {n}: {line[:80]}')
    return segs

def synth_segment(path, text, voice, env):
    if path.exists() and path.stat().st_size > 0: return
    (tmp := path.with_suffix('.txt')).write_text(text, encoding='utf-8')
    for attempt in range(1, 4):
        try:
            run([str(DOUBAO), 'say', '--text-file', str(tmp), '--out', str(path), '--audio-format', 'wav', '--voice', voice], env=env, timeout=120)
            if path.exists() and path.stat().st_size > 0: return
            raise RuntimeError('empty output')
        except Exception as exc:
            if attempt < 3: print(f'  retry {attempt} for {path.name}: {exc}', flush=True); time.sleep(3 * attempt)
    raise RuntimeError(f'failed {path.name}')

def validate_part(part):
    cfg = PARTS[part]; text = cfg['input'].read_text(encoding='utf-8'); segs = parse_segments(text)
    ga, gb = sum(1 for l in text.splitlines() if l.startswith('A:')), sum(1 for l in text.splitlines() if l.startswith('B:'))
    ca, cb = sum(1 for s in segs if s['spk']=='A'), sum(1 for s in segs if s['spk']=='B')
    if (ga,gb) != (ca,cb): raise RuntimeError(f'grep/parse mismatch: grep {ga,gb} parse {ca,cb}')
    if re.findall(r'(^#|```|^>|\*\*|`|【|】|^\s*[-*]\s+|\|)', text, flags=re.M):
        raise RuntimeError('residual TTS artifacts')
    return {'part': part, 'input': str(cfg['input']), 'segments_count': len(segs),
            'speaker_counts': {'A': ca, 'B': cb}, 'max_segment_chars': max(len(s['txt']) for s in segs),
            'cjk_chars': sum(1 for ch in text if '\u4e00' <= ch <= '\u9fff')}

def render_part(part):
    if not DOUBAO.exists(): raise SystemExit(f'missing: {DOUBAO}')
    cfg = PARTS[part]; info = validate_part(part); env = load_env()
    segs = parse_segments(cfg['input'].read_text(encoding='utf-8'))
    cfg['cache'].mkdir(parents=True, exist_ok=True); OUT_DIR.mkdir(parents=True, exist_ok=True)
    rendered, log = [], []; t0 = time.time()
    for idx, seg in enumerate(segs, 1):
        out = cfg['cache'] / f'seg_{idx:03d}_{seg["spk"]}_{VOICE}.wav'
        synth_segment(out, seg['txt'], VOICE, env)
        print(f'{part} {idx}/{len(segs)} spk={seg["spk"]} chars={len(seg["txt"])}', flush=True)
        log.append({'idx': idx, 'spk': seg['spk'], 'voice': VOICE, 'chars': len(seg['txt']), 'line': seg['ln'], 'file': str(out)})
        rendered.append(out)
    list_path = cfg['cache'] / 'concat.txt'
    list_path.write_text(''.join(f"file {shlex.quote(str(p))}\n" for p in rendered), encoding='utf-8')
    run(['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(list_path), '-ar', '24000', '-ac', '1', str(cfg['wav'])], timeout=300)
    cfg['mp3'].parent.mkdir(parents=True, exist_ok=True)
    run(['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error', '-i', str(cfg['wav']), '-codec:a', 'libmp3lame', '-b:a', '128k', str(cfg['mp3'])], timeout=300)
    dur = round(ffprobe_duration(cfg['mp3']), 3)
    meta = {'episode': cfg['episode'], 'title': cfg['title'], 'version': 'v2.1',
            'script_model': 'Claude CLI claude-opus-4-8 (TUI interactive mode)',
            'review_model': 'Gemini CLI gemini-3.1-pro-preview (cross-model review)',
            'fixes_applied': ['Add Corleone example name', 'Add Check stock availability example name', 'Add DO/DS abbreviations', 'Add MI abbreviation', 'Pool crossing consistency note already present'],
            'tts_model': 'Volcengine/Doubao seed-tts via doubao-speech CLI', 'tts_provider': 'doubao',
            'voices': {'A': VOICE, 'B': VOICE}, 'segments_count': len(segs),
            'speaker_counts': info['speaker_counts'], 'max_segment_chars': info['max_segment_chars'],
            'cjk_chars': info['cjk_chars'], 'speed': 'natural (unprocessed)',
            'final_mp3': str(cfg['mp3']), 'duration_mp3_sec': dur, 'duration_hhmmss': seconds_to_hhmmss(dur),
            'mp3_bytes': cfg['mp3'].stat().st_size, 'elapsed_synthesis_time_sec': round(time.time()-t0, 2)}
    cfg['log'].write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding='utf-8')
    cfg['meta'].write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(meta, ensure_ascii=False, indent=2), flush=True)
    return meta

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--validate-only', action='store_true')
    args = ap.parse_args()
    parts = ['single']
    if args.validate_only: print(json.dumps([validate_part(p) for p in parts], ensure_ascii=False, indent=2))
    else: print(json.dumps([render_part(p) for p in parts], ensure_ascii=False, indent=2))

if __name__ == '__main__': main()
