"""Monta a linha do tempo de um episódio e renderiza o vídeo.

uso: python3 -m engine.render episodes.ep01_quanto_te_amam ep01 [--preview N] [--frames a:b]
"""
import importlib
import json
import math
import os
import random
import subprocess
import sys
from multiprocessing import Pool

import cairo
import numpy as np

from .chars import draw_char, Pose, CAST, hexc, setc, rrect, fill_stroke, OUT, TAU, star
from . import scenes as SC
from .scenes import W, H, text

FPS = 24
GAP_NAR = 0.22
GAP_DIALOG = 0.35
LEAD = 0.4
TAIL = 2.5


def ease(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def ease_out(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


def probe(path):
    out = subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path])
    return float(out)


def envelope(path, dur):
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'])
    a = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768
    n = int(math.ceil(dur * FPS)) + 1
    hop = 16000 // FPS
    env = np.zeros(n)
    for i in range(n):
        seg = a[i * hop:(i + 1) * hop]
        if len(seg):
            env[i] = np.sqrt(np.mean(seg ** 2))
    if env.max() > 0:
        env = env / np.percentile(env[env > 0.01] if (env > 0.01).any() else env, 90)
    return np.clip(env, 0, 1)


# ---------------------------------------------------------------- linha do tempo
def build(ep_mod, ep_id):
    ep = importlib.import_module(ep_mod)
    adir = f'media/{ep_id}/audio'
    t = LEAD
    clips = []
    shots = []
    prev_sp = None
    for i, line in enumerate(ep.LINES):
        sp, txt = line[0], line[1]
        scene = line[2] if len(line) > 2 else None
        path = f'{adir}/{i:03d}.mp3'
        d = probe(path)
        if prev_sp is not None:
            t += GAP_DIALOG if (sp != 'nar' or prev_sp != 'nar') else GAP_NAR
        clips.append(dict(i=i, sp=sp, path=path, t0=t, t1=t + d, text=txt))
        if scene is not None or not shots:
            shots.append(dict(scene=scene, t0=t, lines=[i]))
        else:
            shots[-1]['lines'].append(i)
        t += d
        prev_sp = sp
    total = t + TAIL
    for k, s in enumerate(shots):
        s['t0'] = 0 if k == 0 else s['t0'] - 0.12
        s['t1'] = shots[k + 1]['t0'] - 0.12 if k + 1 < len(shots) else total
    for k, s in enumerate(shots):
        if k + 1 < len(shots):
            s['t1'] = shots[k + 1]['t0']
    seen = False
    for s in shots:
        if 'espelho_num' in s['scene'].get('fx', []):
            s['scene']['_mirror_seen'] = seen
            seen = True
    # barras: de onde cada uma vem
    last = {}
    for s in shots:
        bars = {}
        for cid, slot, pose, bar in s['scene']['cast']:
            if bar is None:
                continue
            kf = bar if isinstance(bar, list) else [(0, bar)]
            start = last.get(cid, 0)
            if isinstance(bar, list):
                start = kf[0][1] if cid not in last else last[cid]
            bars[cid] = (start, kf)
            last[cid] = kf[-1][1]
        s['bars'] = bars
    return ep, clips, shots, total


def bar_value(start, kf, u, dur):
    """valor animado da barra no tempo local u (s)."""
    v = start
    pop = 0.0
    prev = start
    for frac, val in kf:
        ts = frac * dur + (0.25 if frac == 0 else 0)
        if u >= ts:
            k = ease_out((u - ts) / 0.7)
            if val != prev:
                v = prev + (val - prev) * k
                if u - ts < 0.45:
                    pop = max(pop, 1 - (u - ts) / 0.45)
            else:
                v = val
            prev = val
        else:
            break
    return v, pop


# ---------------------------------------------------------------- barra neon
def neon_bar(ctx, x, y, s, value, pop=0.0, alpha=1.0, flicker=False, t=0):
    w, h = 230 * s, 60 * s
    sc = 1 + 0.22 * pop
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(sc, sc)
    if flicker and int(t * 14) % 3 == 0:
        alpha *= 0.35
    # brilho
    for k in range(6, 0, -1):
        rrect(ctx, -w / 2 - k * 5 * s, -h / 2 - k * 5 * s, w + k * 10 * s, h + k * 10 * s, h / 2 + k * 5 * s)
        ctx.set_source_rgba(1, 0.24, 0.65, 0.05 * alpha * (1 + pop))
        ctx.fill()
    rrect(ctx, -w / 2, -h / 2, w, h, h / 2)
    ctx.set_source_rgba(0.12, 0.02, 0.12, 0.85 * alpha)
    ctx.fill()
    frac = max(0.0, min(1.0, value / 100))
    if frac > 0:
        ctx.save()
        rrect(ctx, -w / 2, -h / 2, w, h, h / 2)
        ctx.clip()
        g = cairo.LinearGradient(-w / 2, 0, w / 2, 0)
        g.add_color_stop_rgba(0, 1, 0.3, 0.75, alpha)
        g.add_color_stop_rgba(1, 1, 0.1, 0.45, alpha)
        ctx.rectangle(-w / 2, -h / 2, w * frac, h)
        ctx.set_source(g)
        ctx.fill()
        ctx.restore()
    rrect(ctx, -w / 2, -h / 2, w, h, h / 2)
    ctx.set_source_rgba(1, 0.75, 0.92, alpha)
    ctx.set_line_width(5 * s)
    ctx.stroke()
    # coração
    hx = -w / 2 - 6 * s
    heart(ctx, hx, 0, 34 * s, (1, 0.25, 0.6, alpha))
    label = f'{int(round(value))}%'
    ctx.select_font_face('Poppins', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(42 * s)
    e = ctx.text_extents(label)
    ctx.move_to(-e.width / 2 - e.x_bearing + 10 * s, e.height / 2)
    ctx.text_path(label)
    ctx.set_source_rgba(0.1, 0, 0.1, alpha)
    ctx.set_line_width(8 * s)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.stroke_preserve()
    ctx.set_source_rgba(1, 1, 1, alpha)
    ctx.fill()
    ctx.restore()


def heart(ctx, x, y, r, col):
    ctx.save()
    ctx.translate(x, y)
    ctx.move_to(0, r * 0.35)
    ctx.curve_to(-r * 1.1, -r * 0.4, -r * 0.45, -r * 1.15, 0, -r * 0.45)
    ctx.curve_to(r * 0.45, -r * 1.15, r * 1.1, -r * 0.4, 0, r * 0.35)
    ctx.close_path()
    ctx.set_source_rgba(*col)
    ctx.fill_preserve()
    ctx.set_source_rgba(1, 1, 1, col[3])
    ctx.set_line_width(max(2, r * 0.12))
    ctx.stroke()
    ctx.restore()


# ---------------------------------------------------------------- overlays
def notebook(ctx, title=None):
    ctx.save()
    ctx.translate(960, 560)
    ctx.rotate(-0.025)
    rrect(ctx, -620, -420, 1240, 840, 20)
    fill_stroke(ctx, '#FBF8EF', 8)
    ctx.set_source_rgba(0.55, 0.7, 0.95, 0.7)
    ctx.set_line_width(3)
    for k in range(-340, 420, 70):
        ctx.move_to(-600, k); ctx.line_to(600, k); ctx.stroke()
    ctx.set_source_rgba(0.95, 0.4, 0.4, 0.8)
    ctx.move_to(-470, -420); ctx.line_to(-470, 420); ctx.stroke()
    for k in range(-360, 400, 90):
        ctx.arc(-575, k, 16, 0, TAU)
        ctx.set_source_rgba(0.2, 0.2, 0.25, 1)
        ctx.fill()
    ctx.restore()


def hand_text(ctx, s, x, y, size, col='#1D3557', alpha=1.0):
    ctx.select_font_face('Poppins', cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(size)
    ctx.move_to(x, y)
    c = hexc(col)
    ctx.set_source_rgba(c[0], c[1], c[2], alpha)
    ctx.show_text(s)


def mini_head(ctx, cid, x, y, r):
    from .chars import draw_head
    c = CAST[cid]
    draw_head(ctx, cid, c, Pose(mouth='smile'), x, y, r)


def overlay(ctx, fx, u, dur, t, shot):
    p = u / max(dur, 0.01)
    if 'title' in fx and p > 0.25:
        a = ease((p - 0.25) / 0.15)
        ctx.save()
        ctx.translate(0, (1 - a) * -60)
        rrect(ctx, 260, 60, 1400, 200, 30)
        ctx.set_source_rgba(0.08, 0.02, 0.12, 0.82 * a)
        ctx.fill()
        text(ctx, 'E SE VOCÊ PUDESSE VER', 960, 140, 64, '#FFFFFF', outline='#1A0A1F', lw=10)
        text(ctx, 'O QUANTO CADA PESSOA TE AMA?', 960, 225, 64, '#FF4FAE', outline='#1A0A1F', lw=10)
        ctx.restore()
    if 'conta' in fx:
        notebook(ctx)
        rows = [('Bia = 41%', '#C9184A'), ('Prof. Ed. Física = 35%', '#1D3557'), ('Seu Jorge (porteiro) = 72%', '#1D3557'), ('41 é bom??', '#C9184A')]
        for k, (s, col) in enumerate(rows):
            a = ease((p - 0.1 - k * 0.2) / 0.12)
            if a > 0:
                hand_text(ctx, s, 520, 330 + k * 140, 66, col, a)
    if 'ranking' in fx:
        rows = [('vo', 'Vó Cida', 100), ('mae', 'Mãe', 100), ('davi', 'Davi', 98), ('lari', 'Lari', 87), ('jorge', 'Seu Jorge', 72),
                ('prof', 'Prof. Matemática', 60), ('bia', 'Bia', 41), ('aluno3', 'Prof. Ed. Física', 35), ('tia', 'Tia Marta', 3)]
        text(ctx, 'QUEM TE AMA MAIS', 960, 95, 60, '#FFD23F', outline='#10002B', lw=10)
        for k, (cid, name, v) in enumerate(rows):
            a = ease((p * 1.6 - k * 0.09) / 0.1)
            if a <= 0:
                continue
            y = 150 + k * 98
            hl = cid in ('bia', 'jorge')
            rrect(ctx, 460, y, 1000, 82, 20)
            ctx.set_source_rgba(1, 0.3, 0.7, 0.35 * a) if hl else ctx.set_source_rgba(1, 1, 1, 0.1 * a)
            ctx.fill()
            text(ctx, f'{k + 1}º', 520, y + 56, 40, '#FFFFFF', align='center')
            ctx.save(); ctx.translate(610, y + 42); ctx.scale(0.3, 0.3); mini_head(ctx, cid, 0, 0, 118); ctx.restore()
            text(ctx, name, 680, y + 56, 40, '#FFFFFF', align='left')
            neon_bar(ctx, 1290, y + 42, 0.95, v * a, alpha=a)
        if p > 0.72:
            a = ease((p - 0.72) / 0.1)
            ctx.save(); ctx.translate(1540, 640); ctx.rotate(-0.15)
            text(ctx, 'perdeu pro', 0, 0, 44, '#FFFFFF', outline='#C9184A', lw=10)
            text(ctx, 'PORTEIRO', 0, 60, 60, '#FFD23F', outline='#C9184A', lw=12)
            ctx.restore()
    if 'tabela' in fx:
        notebook(ctx)
        hand_text(ctx, 'AÇÃO', 520, 280, 64, '#C9184A')
        hand_text(ctx, 'PONTOS', 1200, 280, 64, '#C9184A')
        ctx.set_source_rgba(0.8, 0.1, 0.3, 0.8); ctx.set_line_width(5)
        ctx.move_to(1150, 220); ctx.line_to(1150, 900); ctx.stroke()
        rows = [('juntar canetas', '+3'), ('emprestar carregador', '+3'), ('rir da piada (ruim)', '+1'), ('biblioteca', '+2?')]
        for k, (a1, a2) in enumerate(rows):
            a = ease((p - 0.25 - k * 0.15) / 0.1)
            if a > 0:
                hand_text(ctx, a1, 520, 420 + k * 120, 54, '#1D3557', a)
                hand_text(ctx, a2, 1220, 420 + k * 120, 54, '#2A9D8F', a)
    if 'estudo' in fx:
        a = ease(p / 0.1)
        rrect(ctx, 610, 60, 700, 110, 24)
        ctx.set_source_rgba(1, 1, 1, 0.12 * a); ctx.fill()
        text(ctx, 'ESTUDO • 2018', 960, 135, 56, '#FFD23F')
        if p > 0.55:
            b = ease((p - 0.55) / 0.1)
            for x in (620, 1300):
                bubble(ctx, x + 230, 330, 110 * b, '?%')
    if 'lacuna' in fx:
        for x, achou in ((620, 38), (1300, 41)):
            a = ease((p - 0.05) / 0.12)
            bubble(ctx, x + 230, 230, 110 * a, f'{achou}%', small='achou')
        if p > 0.55:
            a = ease((p - 0.55) / 0.1)
            rrect(ctx, 560, 900, 800, 110, 24)
            ctx.set_source_rgba(0.1, 0, 0.15, 0.8 * a); ctx.fill()
            text(ctx, '"LACUNA DO GOSTAR"', 960, 975, 56, '#FFFFFF')
    if 'ligacao' in fx or 'ligacao_vo' in fx:
        phone_ui(ctx, p, talking='ligacao_vo' in fx, t=t)
    if 'placar' in fx:
        text(ctx, 'PONTUAÇÃO', 960, 120, 70, '#FFD23F', outline='#10002B', lw=10)
        cells = [('vo', 100), ('davi', 98), ('lari', 87), ('jorge', 72), ('bia', 52), ('tia', 3)]
        for k, (cid, v) in enumerate(cells):
            cx = 420 + (k % 3) * 540
            cy = 330 + (k // 3) * 400
            a = ease((p * 2 - k * 0.12) / 0.2)
            rrect(ctx, cx - 220, cy - 120, 440, 340, 30)
            ctx.set_source_rgba(1, 1, 1, 0.08 * a); ctx.fill()
            ctx.save(); ctx.translate(cx, cy); ctx.scale(0.6, 0.6); mini_head(ctx, cid, 0, 0, 118); ctx.restore()
            jitter = (math.sin(t * 13 + k) * 3) if p > 0.5 else 0
            neon_bar(ctx, cx, cy + 150, 1.2, max(0, min(100, v + jitter)), alpha=a)
    if 'audios' in fx:
        chat_ui(ctx, p, t)
    if 'quadrilha' in fx and p > 0.1:
        a = ease((p - 0.1) / 0.12)
        ctx.save(); ctx.translate(960, 230); ctx.scale(0.6 + 0.4 * a, 0.6 + 0.4 * a); ctx.rotate(-0.05)
        text(ctx, 'QUADRILHA!', 0, 0, 120, '#FFD23F', outline='#9D0208', lw=16)
        text(ctx, 'todo mundo precisa de um par', 0, 80, 46, '#FFFFFF', outline='#1E1E24', lw=8)
        ctx.restore()
    if 'risos' in fx:
        random.seed(9)
        for k in range(7):
            ts = k * 0.11
            if p > ts:
                a = ease((p - ts) / 0.08)
                ctx.save(); ctx.translate(200 + random.random() * 1500, 150 + random.random() * 300); ctx.rotate(random.random() * 0.6 - 0.3)
                ctx.scale(a, a)
                text(ctx, random.choice(['HAHAHA', 'KKKKK', 'HAHA']), 0, 0, 64, '#FFFFFF', outline='#E63946', lw=10)
                ctx.restore()
    if 'cta' in fx and p > 0.15:
        a = ease((p - 0.15) / 0.12)
        rrect(ctx, 960, 260, 860, 500, 40)
        ctx.set_source_rgba(0, 0, 0, 0.35 * a); ctx.fill()
        text(ctx, 'E VOCÊ?', 1390, 380, 96, '#FFD23F', outline='#10002B', lw=12)
        text(ctx, 'quem você olharia', 1390, 480, 54, '#FFFFFF')
        text(ctx, 'primeiro?', 1390, 550, 54, '#FFFFFF')
        if p > 0.6:
            b = ease((p - 0.6) / 0.1)
            ctx.save(); ctx.translate(1390, 680); ctx.scale(b, b)
            rrect(ctx, -260, -50, 520, 100, 50)
            ctx.set_source_rgba(1, 0.25, 0.6, 1); ctx.fill()
            text(ctx, 'COMENTA AQUI', 0, 18, 48, '#FFFFFF')
            ctx.restore()


def bubble(ctx, x, y, r, label, small=None):
    if r <= 1:
        return
    for k, (dx, dy, rr_) in enumerate(((-0.9, 1.25, 0.12), (-0.6, 1.0, 0.18))):
        ctx.arc(x + dx * r, y + dy * r, rr_ * r, 0, TAU)
        fill_stroke(ctx, '#FFFFFF', 4)
    ctx.save(); ctx.translate(x, y); ctx.scale(1.25, 0.9); ctx.arc(0, 0, r, 0, TAU); ctx.restore()
    fill_stroke(ctx, '#FFFFFF', 5)
    if small:
        text(ctx, small, x, y - r * 0.3, r * 0.3, '#6C757D')
        text(ctx, label, x, y + r * 0.35, r * 0.55, '#C9184A')
    else:
        text(ctx, label, x, y + r * 0.2, r * 0.6, '#C9184A')


def phone_ui(ctx, p, talking, t):
    ctx.save()
    ctx.translate(1450, 540)
    rrect(ctx, -210, -400, 420, 800, 50)
    fill_stroke(ctx, '#1E1E24', 8)
    rrect(ctx, -190, -370, 380, 740, 36)
    g = cairo.LinearGradient(0, -370, 0, 370)
    g.add_color_stop_rgb(0, 0.2, 0.25, 0.45)
    g.add_color_stop_rgb(1, 0.1, 0.1, 0.2)
    ctx.set_source(g); ctx.fill()
    text(ctx, 'Vó Cida', 0, -170, 50, '#FFFFFF')
    text(ctx, 'em chamada' if talking else 'chamando...', 0, -115, 30, '#BBBBBB')
    pulse = 1 + 0.06 * math.sin(t * 8)
    ctx.save(); ctx.translate(0, 40); ctx.scale(0.75 * pulse, 0.75 * pulse)
    from .chars import draw_head
    draw_head(ctx, 'vo', CAST['vo'], Pose(mouth='smile', talk=(0.6 + 0.4 * math.sin(t * 22)) if talking else 0, eyes='happy'), 0, 0, 118)
    ctx.restore()
    if talking:
        neon_bar(ctx, 0, -260, 0.8, 100)
    for dx, col in ((-100, '#E63946'), (100, '#06D6A0')):
        ctx.arc(dx, 280, 46, 0, TAU)
        fill_stroke(ctx, col, 5)
    ctx.restore()


def chat_ui(ctx, p, t):
    ctx.save()
    rrect(ctx, 560, 40, 800, 1000, 40)
    fill_stroke(ctx, '#ECE5DD', 8)
    rrect(ctx, 560, 40, 800, 120, 40)
    setc(ctx, '#128C7E'); ctx.fill()
    ctx.rectangle(560, 120, 800, 40); ctx.fill()
    text(ctx, 'Família', 760, 115, 48, '#FFFFFF', align='left')
    ctx.save(); ctx.translate(680, 100); ctx.scale(0.36, 0.36); mini_head(ctx, 'vo', 0, 0, 118); ctx.restore()
    n = int(min(23, 1 + p * 26))
    ctx.rectangle(560, 160, 800, 880); ctx.clip()
    shown = list(range(max(0, n - 7), n))
    for k, idx in enumerate(shown):
        y = 220 + k * 118
        rrect(ctx, 600, y, 560, 92, 20)
        fill_stroke(ctx, '#FFFFFF', 3)
        ctx.arc(650, y + 46, 24, 0, TAU)
        setc(ctx, '#128C7E'); ctx.fill()
        ctx.move_to(642, y + 32); ctx.line_to(642, y + 60); ctx.line_to(664, y + 46); ctx.close_path()
        ctx.set_source_rgba(1, 1, 1, 1); ctx.fill()
        random.seed(idx)
        for b in range(24):
            hh = 8 + random.random() * 34
            ctx.rectangle(700 + b * 14, y + 46 - hh / 2, 7, hh)
        ctx.set_source_rgba(0.5, 0.55, 0.6, 1); ctx.fill()
        text(ctx, 'alô?' if idx % 6 != 3 else '...', 1130, y + 60, 30, '#555555', align='right')
    ctx.restore()
    text(ctx, f'{n} áudios', 1560, 300, 70, '#FFFFFF', outline='#081C15', lw=10)
    if p > 0.55:
        a = ease((p - 0.55) / 0.1)
        text(ctx, '19× "alô?"', 1560, 420, 60, '#25D366', outline='#081C15', lw=10)


# ---------------------------------------------------------------- frame
class Ctx:
    pass


def char_pose(cid, pose, speaking_amp, t, fx, k):
    kw = dict(pose)
    ph = (hash(cid) % 100) / 100 * TAU
    kw['bob'] = math.sin(t * 2.2 + ph) * 0.6
    if 'danca' in fx:
        kw['bob'] = abs(math.sin(t * 5 + k)) * 7
    if 'confete' in fx and kw.get('arms') == 'up':
        kw['bob'] = abs(math.sin(t * 6 + k)) * 5
    # piscar
    period = 3.1 + (hash(cid) % 7) * 0.3
    if (t + ph) % period < 0.12 and kw.get('eyes', 'normal') in ('normal', 'wide', 'half', 'side', 'sad', 'angry'):
        kw['blink'] = True
    if speaking_amp is not None:
        kw['talk'] = float(speaking_amp)
    return Pose(**kw)


def draw_frame(ctx, ep, clips, shots, envs, t):
    # shot atual
    si = 0
    for k, s in enumerate(shots):
        if s['t0'] <= t:
            si = k
    shot = shots[si]
    sc = shot['scene']
    u = t - shot['t0']
    dur = shot['t1'] - shot['t0']
    fx = sc.get('fx', [])
    bg, fg = SC.BG[sc['bg']]
    # quem está falando agora
    speaking = {}
    for c in clips:
        if c['t0'] <= t < c['t1'] and c['sp'] != 'nar':
            fi = int((t - c['t0']) * FPS)
            e = envs[c['i']]
            speaking[c['sp']] = e[min(fi, len(e) - 1)]
    # câmera
    cam = sc.get('cam', {})
    z0 = cam.get('zoom', 1.0)
    z1 = cam.get('to', z0 * 1.04)
    z = z0 + (z1 - z0) * ease(u / max(dur, 0.01))
    if 'zoom_punch' in fx:
        z *= 1 + 0.15 * (1 - ease_out(u / 0.35))
    slots = SC.SLOTS.get(sc['bg'], {})
    cx, cy = cam.get('cx', W / 2), cam.get('cy', H / 2)
    if 'zoom' not in cam and sc['cast']:
        xs = [slots[sl][0] for _, sl, _, _ in sc['cast']]
        ys = [slots[sl][1] - 300 * slots[sl][2] for _, sl, _, _ in sc['cast']]
        cx = (min(xs) + max(xs)) / 2
        cy = sum(ys) / len(ys)
        z0, z1 = 1.18, 1.24
        z = z0 + (z1 - z0) * ease(u / max(dur, 0.01))
    if 'focus' in cam:
        for cid, slot, pose, bar in sc['cast']:
            if cid == cam['focus']:
                x, y, s = slots[slot]
                hs = CAST[cid]['h']
                cx = x
                cy = y - 470 * hs * s
    vw, vh = W / z, H / z
    cx = min(max(cx, vw / 2), W - vw / 2)
    cy = min(max(cy, vh / 2), H - vh / 2)
    if 'shake' in fx and u < 0.5:
        a = (1 - u / 0.5) * 14
        cx += math.sin(u * 70) * a
        cy += math.cos(u * 55) * a
    ctx.save()
    ctx.translate(W / 2, H / 2)
    ctx.scale(z, z)
    ctx.translate(-cx, -cy)
    bg(ctx, t)
    heads = {}
    for k, (cid, slot, pose, bar) in enumerate(sc['cast']):
        x, y, s = slots[slot]
        p = char_pose(cid, pose, speaking.get(cid), t, fx, k)
        if 'look_lr' in fx and cid == 'voce':
            p.look = -1 if u < dur / 2 else 1
            p.facing = -1 if u < dur / 2 else 1
        info = draw_char(ctx, cid, x, y, s, p)
        heads[cid] = (info, s)
    # reflexo no espelho
    if sc['bg'] == 'banheiro':
        mirror(ctx, sc, t, u, dur, fx, heads)
    if fg:
        fg(ctx, t)
    if 'estojo' in fx:
        SC.fx_estojo(ctx, t)
    # barras
    for cid, (start, kf) in shot['bars'].items():
        info, s = heads[cid]
        v, pop = bar_value(start, kf, u, dur)
        tx, ty = info['top']
        neon_bar(ctx, tx, ty - 60 * s, max(0.75, s), v, pop, flicker=('flicker' in fx and cid == 'davi'), t=t)
    if 'hearts' in fx:
        random.seed(2)
        for k in range(10):
            hx = random.random() * W
            hy = H - ((t * 60 + random.random() * H) % (H + 100))
            heart(ctx, hx, hy, 18 + random.random() * 16, (1, 0.35, 0.65, 0.75))
    if 'confete' in fx:
        random.seed(5)
        for k in range(120):
            x = random.random() * W + math.sin(t * 2 + k) * 30
            y = (random.random() * H + t * (120 + random.random() * 120)) % (H + 40) - 20
            ctx.save(); ctx.translate(x, y); ctx.rotate(t * 3 + k)
            ctx.rectangle(-8, -4, 16, 8)
            setc(ctx, random.choice(['#E63946', '#FFB703', '#2A9D8F', '#8338EC', '#06D6A0', '#FF006E']))
            ctx.fill(); ctx.restore()
    if 'estrelas' in fx:
        random.seed(8)
        for k in range(14):
            a = abs(math.sin(t * 2 + k))
            star(ctx, 100 + random.random() * 1700, 80 + random.random() * 380, 8 + 10 * a, '#FFF3B0')
    ctx.restore()
    overlay(ctx, fx, u, dur, t, shot)
    SC.vignette(ctx, 0.22)


def mirror(ctx, sc, t, u, dur, fx, heads):
    mx, my, mw, mh = SC.MIRROR
    ctx.save()
    rrect(ctx, mx, my, mw, mh, 20)
    ctx.clip()
    g = cairo.LinearGradient(mx, my, mx + mw, my + mh)
    g.add_color_stop_rgb(0, 0.78, 0.9, 0.95)
    g.add_color_stop_rgb(1, 0.6, 0.75, 0.85)
    ctx.paint()
    ctx.rectangle(mx, my, mw, mh)
    ctx.set_source(g)
    ctx.fill()
    pose = dict(sc['cast'][0][2])
    pose['facing'] = -1
    p = char_pose('voce', pose, None, t, fx, 0)
    info = draw_char(ctx, 'voce', 1240, 760, 0.8, p)
    val = None
    for key, kf in (('espelho_num', [(0, 22)]), ('espelho_29', [(0, 22), (0.55, 29)]), ('espelho_61', [(0, 29), (0.05, 61)])):
        if key in fx:
            first = key == 'espelho_num' and not sc.get('_mirror_seen')
            val = bar_value(0 if first else kf[0][1], kf, u, dur)
    if val:
        tx, ty = info['top']
        neon_bar(ctx, tx, ty - 50, 0.85, val[0], val[1])
    # brilho do vidro
    ctx.set_source_rgba(1, 1, 1, 0.25)
    for k in range(2):
        ctx.move_to(mx + 60 + k * 90, my)
        ctx.line_to(mx + 120 + k * 90, my)
        ctx.line_to(mx - 80 + k * 90, my + mh)
        ctx.line_to(mx - 140 + k * 90, my + mh)
        ctx.close_path()
        ctx.fill()
    ctx.restore()


# ---------------------------------------------------------------- render
_G = {}


def _init(ep_mod, ep_id):
    ep, clips, shots, total = build(ep_mod, ep_id)
    envs = {c['i']: envelope(c['path'], c['t1'] - c['t0']) for c in clips if c['sp'] != 'nar'}
    _G.update(ep=ep, clips=clips, shots=shots, envs=envs, total=total)


def _render_range(args):
    ep_mod, ep_id, f0, f1, out = args
    if not _G:
        _init(ep_mod, ep_id)
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H)
    ctx = cairo.Context(surf)
    proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgra', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                             '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    for f in range(f0, f1):
        ctx.save()
        ctx.set_source_rgb(0, 0, 0)
        ctx.paint()
        draw_frame(ctx, _G['ep'], _G['clips'], _G['shots'], _G['envs'], f / FPS)
        ctx.restore()
        surf.flush()
        proc.stdin.write(bytes(surf.get_data()))
    proc.stdin.close()
    proc.wait()
    return out


def sfx_pop(sr=44100):
    n = int(0.16 * sr)
    tt = np.arange(n) / sr
    f = 700 + 900 * tt / 0.16
    w = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-tt * 28)
    return (w * 0.35).astype(np.float32)


def music_bed(n, sr):
    """arpejo suave em loop (I-V-vi-IV), 84 bpm."""
    out = np.zeros(n, dtype=np.float32)
    beat = 60 / 84 / 2
    chords = [[60, 64, 67, 72], [55, 59, 62, 67], [57, 60, 64, 69], [53, 57, 60, 65]]
    k = 0
    t = 0.0
    note_len = int(sr * 1.2)
    tt = np.arange(note_len) / sr
    envl = np.exp(-tt * 3.2) * (1 - np.exp(-tt * 200))
    cache = {}
    while int(t * sr) < n:
        ch = chords[(k // 8) % 4]
        m = ch[[0, 2, 1, 3, 2, 1, 3, 2][k % 8]]
        if m not in cache:
            f = 440 * 2 ** ((m - 69) / 12)
            w = (np.sin(2 * np.pi * f * tt) + 0.35 * np.sin(4 * np.pi * f * tt) + 0.12 * np.sin(6 * np.pi * f * tt)) * envl
            cache[m] = w.astype(np.float32)
        i0 = int(t * sr)
        seg = cache[m][:n - i0]
        out[i0:i0 + len(seg)] += seg
        if k % 8 == 0:
            fb = 440 * 2 ** ((ch[0] - 12 - 69) / 12)
            bl = int(sr * beat * 8)
            tb = np.arange(bl) / sr
            bass = np.sin(2 * np.pi * fb * tb) * np.exp(-tb * 0.8) * 0.6
            seg = bass[:n - i0]
            out[i0:i0 + len(seg)] += seg.astype(np.float32)
        t += beat
        k += 1
    fade = int(sr * 2)
    out[:fade] *= np.linspace(0, 1, fade)
    out[-fade:] *= np.linspace(1, 0, fade)
    return out / (np.abs(out).max() + 1e-9)


def build_audio(clips, shots, total, out):
    sr = 44100
    mix = np.zeros(int((total + 1) * sr), dtype=np.float32)
    for c in clips:
        raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', c['path'], '-ac', '1', '-ar', str(sr), '-f', 'f32le', '-'])
        a = np.frombuffer(raw, dtype=np.float32)
        i0 = int(c['t0'] * sr)
        mix[i0:i0 + len(a)] += a
    pop = sfx_pop(sr)
    for s in shots:
        dur = s['t1'] - s['t0']
        for cid, (start, kf) in s['bars'].items():
            prev = start
            for frac, val in kf:
                if val != prev:
                    ts = s['t0'] + frac * dur + (0.25 if frac == 0 else 0)
                    i0 = int(ts * sr)
                    mix[i0:i0 + len(pop)] += pop[:len(mix) - i0]
                prev = val
    mix += music_bed(len(mix), sr) * 0.055
    mix = np.clip(mix, -1, 1)
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(sr), '-ac', '1', '-i', '-', '-c:a', 'aac', '-b:a', '192k', out], stdin=subprocess.PIPE)
    p.stdin.write(mix.tobytes())
    p.stdin.close()
    p.wait()


def main():
    ep_mod, ep_id = sys.argv[1], sys.argv[2]
    args = sys.argv[3:]
    _init(ep_mod, ep_id)
    total = _G['total']
    nframes = int(total * FPS)
    bdir = f'build/{ep_id}'
    os.makedirs(bdir, exist_ok=True)
    if '--stills' in args:
        times = [float(x) for x in args[args.index('--stills') + 1].split(',')]
        surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H)
        ctx = cairo.Context(surf)
        for tt in times:
            ctx.save(); draw_frame(ctx, _G['ep'], _G['clips'], _G['shots'], _G['envs'], tt); ctx.restore()
            surf.write_to_png(f'{bdir}/still_{tt:07.2f}.png')
        return
    if '--shots' in args:
        print(json.dumps([dict(k=k, t0=round(s['t0'], 2), t1=round(s['t1'], 2), bg=s['scene']['bg'], lines=s['lines']) for k, s in enumerate(_G['shots'])]))
        print('total', total)
        return
    f0, f1 = 0, nframes
    if '--frames' in args:
        a, b = args[args.index('--frames') + 1].split(':')
        f0, f1 = int(float(a) * FPS), int(float(b) * FPS)
    nproc = 2
    step = (f1 - f0 + nproc - 1) // nproc
    jobs = [(ep_mod, ep_id, f0 + k * step, min(f1, f0 + (k + 1) * step), f'{bdir}/part{k}.mp4') for k in range(nproc)]
    with Pool(nproc) as pool:
        parts = pool.map(_render_range, jobs)
    with open(f'{bdir}/parts.txt', 'w') as fh:
        for pth in parts:
            fh.write(f"file '{os.path.abspath(pth)}'\n")
    subprocess.check_call(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{bdir}/parts.txt', '-c', 'copy', f'{bdir}/video.mp4'])
    build_audio(_G['clips'], _G['shots'], total, f'{bdir}/audio.m4a')
    out = f'{bdir}/{ep_id}.mp4' if f0 == 0 and f1 == nframes else f'{bdir}/{ep_id}_trecho.mp4'
    ss = f0 / FPS
    subprocess.check_call(['ffmpeg', '-v', 'error', '-y', '-i', f'{bdir}/video.mp4', '-ss', str(ss), '-t', str((f1 - f0) / FPS), '-i', f'{bdir}/audio.m4a',
                           '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'copy', '-shortest', out])
    print('ok', out, total)


if __name__ == '__main__':
    main()
