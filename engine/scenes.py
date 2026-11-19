"""Cenários (fundo + primeiro plano) e posições (slots) dos personagens."""
import math
import random
import cairo
from .chars import hexc, setc, rrect, fill_stroke, OUT, TAU, star

W, H = 1920, 1080


def rect(ctx, x, y, w, h, col, outline=True, lw=5):
    ctx.rectangle(x, y, w, h)
    if outline:
        fill_stroke(ctx, col, lw)
    else:
        setc(ctx, col)
        ctx.fill()


def rr(ctx, x, y, w, h, r, col, lw=5):
    rrect(ctx, x, y, w, h, r)
    fill_stroke(ctx, col, lw)


def window(ctx, x, y, w, h, sky='#9ED8F5', night=False):
    rr(ctx, x - 14, y - 14, w + 28, h + 28, 10, '#FFFFFF')
    g = cairo.LinearGradient(0, y, 0, y + h)
    if night:
        g.add_color_stop_rgb(0, 0.08, 0.1, 0.25)
        g.add_color_stop_rgb(1, 0.2, 0.18, 0.4)
    else:
        a = hexc(sky)
        g.add_color_stop_rgb(0, a[0], a[1], a[2])
        g.add_color_stop_rgb(1, 0.85, 0.95, 1)
    ctx.rectangle(x, y, w, h)
    ctx.set_source(g)
    ctx.fill()
    if night:
        ctx.arc(x + w * 0.7, y + h * 0.3, 26, 0, TAU)
        ctx.set_source_rgba(1, 0.97, 0.8, 1)
        ctx.fill()
    else:
        # nuvem
        for dx, dy, r in ((0.3, 0.35, 26), (0.38, 0.3, 32), (0.47, 0.36, 24)):
            ctx.arc(x + w * dx, y + h * dy, r, 0, TAU)
            ctx.set_source_rgba(1, 1, 1, 0.95)
            ctx.fill()
    ctx.set_source_rgba(1, 1, 1, 1)
    ctx.set_line_width(10)
    ctx.move_to(x + w / 2, y)
    ctx.line_to(x + w / 2, y + h)
    ctx.move_to(x, y + h / 2)
    ctx.line_to(x + w, y + h / 2)
    ctx.stroke()
    ctx.rectangle(x, y, w, h)
    ctx.set_source_rgba(*OUT)
    ctx.set_line_width(5)
    ctx.stroke()


def frame_pic(ctx, x, y, w, h, col):
    rr(ctx, x, y, w, h, 4, '#8B5E3C')
    rect(ctx, x + 10, y + 10, w - 20, h - 20, col, lw=3)


def floor(ctx, y, col, col2=None, tiles=False):
    rect(ctx, 0, y, W, H - y, col, outline=False)
    ctx.set_source_rgba(*OUT)
    ctx.set_line_width(5)
    ctx.move_to(0, y)
    ctx.line_to(W, y)
    ctx.stroke()
    if tiles:
        ctx.set_source_rgba(0, 0, 0, 0.08)
        ctx.set_line_width(3)
        for i in range(-10, 30):
            ctx.move_to(W / 2 + i * 140 - (H - y) * 1.2 * (i - 10) / 10, H)
            ctx.line_to(W / 2 + (i - 10) * 70 + 700, y)
            ctx.stroke()
        for k in range(1, 5):
            yy = y + (H - y) * (k / 5) ** 1.4
            ctx.move_to(0, yy)
            ctx.line_to(W, yy)
            ctx.stroke()


def wall(ctx, col, y1, col2=None, ybreak=None):
    rect(ctx, 0, 0, W, y1, col, outline=False)
    if col2 and ybreak:
        rect(ctx, 0, ybreak, W, y1 - ybreak, col2, outline=False)
        ctx.set_source_rgba(0, 0, 0, 0.35)
        ctx.set_line_width(6)
        ctx.move_to(0, ybreak)
        ctx.line_to(W, ybreak)
        ctx.stroke()


def vignette(ctx, a=0.28):
    g = cairo.RadialGradient(W / 2, H / 2, H * 0.35, W / 2, H / 2, H * 1.05)
    g.add_color_stop_rgba(0, 0, 0, 0, 0)
    g.add_color_stop_rgba(1, 0, 0, 0, a)
    ctx.rectangle(0, 0, W, H)
    ctx.set_source(g)
    ctx.fill()


def text(ctx, s, x, y, size, col='#FFFFFF', align='center', bold=True, outline=None, lw=10, font='Poppins'):
    ctx.select_font_face(font, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(size)
    ext = ctx.text_extents(s)
    if align == 'center':
        tx = x - ext.width / 2 - ext.x_bearing
    elif align == 'right':
        tx = x - ext.width - ext.x_bearing
    else:
        tx = x
    ty = y
    ctx.move_to(tx, ty)
    ctx.text_path(s)
    if outline:
        setc(ctx, outline)
        ctx.set_line_width(lw)
        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
        ctx.stroke_preserve()
    setc(ctx, col)
    ctx.fill()
    return ext


# ---------------------------------------------------------------- cenários
def bg_jantar(ctx, t):
    wall(ctx, '#F6E7C8', 760, '#E9C99A', 520)
    window(ctx, 1480, 120, 300, 260)
    frame_pic(ctx, 250, 140, 200, 150, '#7FB3D5')
    frame_pic(ctx, 520, 170, 130, 170, '#F5B7B1')
    # relógio
    ctx.arc(1080, 200, 60, 0, TAU)
    fill_stroke(ctx, '#FFFFFF')
    ctx.set_source_rgba(*OUT)
    ctx.set_line_width(6)
    ctx.move_to(1080, 200); ctx.line_to(1080, 160); ctx.move_to(1080, 200); ctx.line_to(1110, 210); ctx.stroke()
    # filtro de barro
    rr(ctx, 120, 560, 120, 200, 40, '#C8763E')
    floor(ctx, 760, '#B9855A')


def fg_jantar(ctx, t):
    # mesa com toalha xadrez
    rr(ctx, 160, 760, 1600, 90, 12, '#FFFFFF')
    ctx.save()
    rrect(ctx, 160, 760, 1600, 90, 12)
    ctx.clip()
    ctx.set_source_rgba(0.85, 0.2, 0.2, 0.55)
    for i in range(0, 1600, 60):
        ctx.rectangle(160 + i, 760, 30, 90)
    ctx.fill()
    ctx.restore()
    rrect(ctx, 160, 760, 1600, 90, 12)
    ctx.set_source_rgba(*OUT)
    ctx.set_line_width(5)
    ctx.stroke()
    rect(ctx, 180, 850, 1560, 230, '#8B5A2B')
    # comida
    for x, col in ((420, '#F4D35E'), (760, '#FFFFFF'), (1130, '#C46A2B'), (1460, '#7FB800')):
        ctx.save(); ctx.translate(x, 752); ctx.scale(1, 0.32); ctx.arc(0, 0, 90, 0, TAU); ctx.restore()
        fill_stroke(ctx, '#FFFFFF', 4)
        ctx.save(); ctx.translate(x, 735); ctx.scale(1, 0.45); ctx.arc(0, 0, 56, math.pi, TAU); ctx.restore()
        fill_stroke(ctx, col, 4)
    # jarra de suco
    rr(ctx, 560, 700, 56, 70, 12, '#FFB347')


def bg_sala(ctx, t):
    wall(ctx, '#CDE7E3', 780)
    window(ctx, 200, 140, 320, 280)
    # TV
    rr(ctx, 1260, 240, 460, 280, 16, '#1E1E24')
    g = cairo.LinearGradient(0, 260, 0, 500)
    g.add_color_stop_rgb(0, 0.3, 0.6, 1)
    g.add_color_stop_rgb(1, 0.6, 0.3, 0.9)
    ctx.rectangle(1280, 260, 420, 240)
    ctx.set_source(g)
    ctx.fill()
    text(ctx, 'GOL!', 1490, 410, 90, '#FFD23F', outline='#1E1E24', lw=12)
    rect(ctx, 1240, 520, 500, 260, '#8B5E3C')
    floor(ctx, 780, '#D9B38C', tiles=True)
    rr(ctx, 240, 560, 1000, 280, 40, '#E76F51')


def fg_sala(ctx, t):
    rr(ctx, 200, 640, 90, 280, 40, '#E76F51')
    rr(ctx, 1190, 640, 90, 280, 40, '#E76F51')
    rr(ctx, 260, 810, 960, 110, 30, '#C65A3F')


def bg_portao(ctx, t):
    g = cairo.LinearGradient(0, 0, 0, 700)
    g.add_color_stop_rgb(0, 0.55, 0.8, 0.98)
    g.add_color_stop_rgb(1, 0.85, 0.94, 1)
    ctx.rectangle(0, 0, W, 700)
    ctx.set_source(g)
    ctx.fill()
    # prédio da escola
    rect(ctx, 0, 180, W, 560, '#F2C14E')
    rect(ctx, 0, 560, W, 180, '#2A9D8F', outline=False)
    for i in range(6):
        window(ctx, 120 + i * 300, 250, 170, 140)
    text(ctx, 'E.E. PROF. ANTÔNIO CARLOS', 960, 230, 44, '#FFFFFF', outline='#1E1E24', lw=10)
    # muro + portão
    rect(ctx, 0, 600, W, 160, '#D9D9D9')
    rect(ctx, 600, 520, 720, 260, '#6C757D')
    ctx.set_source_rgba(*OUT)
    ctx.set_line_width(10)
    for i in range(16):
        ctx.move_to(620 + i * 46, 530); ctx.line_to(620 + i * 46, 770)
    ctx.stroke()
    # guarita
    rr(ctx, 1450, 420, 300, 360, 10, '#FFFFFF')
    window(ctx, 1490, 470, 220, 130)
    text(ctx, 'PORTARIA', 1600, 700, 38, '#1E1E24')
    floor(ctx, 760, '#A3A3A3')
    ctx.set_source_rgba(0, 0, 0, 0.12)
    for i in range(0, W, 160):
        ctx.rectangle(i, 760, 6, 320)
    ctx.fill()


def bg_classe(ctx, t):
    wall(ctx, '#FDF1D6', 720, '#7FB069', 500)
    # quadro verde
    rr(ctx, 520, 110, 880, 330, 10, '#2D6A4F', 8)
    rect(ctx, 520, 430, 880, 20, '#B08968')
    ctx.set_source_rgba(1, 1, 1, 0.85)
    ctx.select_font_face('Poppins', cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(54)
    ctx.move_to(600, 220); ctx.show_text('2x + 6 = 14')
    ctx.move_to(600, 320); ctx.show_text('x = ?')
    window(ctx, 1560, 140, 260, 300)
    window(ctx, 100, 140, 260, 300)
    floor(ctx, 720, '#C9A27E', tiles=True)
    # mesa do professor
    rr(ctx, 120, 640, 320, 140, 8, '#8B5E3C')


def fg_classe(ctx, t):
    for x in (700, 1100, 1500):
        rr(ctx, x - 150, 820, 300, 40, 8, '#D4A373')
        rect(ctx, x - 130, 860, 18, 220, '#6C757D', lw=3)
        rect(ctx, x + 112, 860, 18, 220, '#6C757D', lw=3)


def bg_patio(ctx, t):
    g = cairo.LinearGradient(0, 0, 0, 600)
    g.add_color_stop_rgb(0, 0.5, 0.78, 0.98)
    g.add_color_stop_rgb(1, 0.82, 0.93, 1)
    ctx.rectangle(0, 0, W, 760)
    ctx.set_source(g)
    ctx.fill()
    for x, y, r in ((300, 140, 50), (360, 120, 64), (430, 145, 46), (1400, 100, 40), (1450, 90, 54)):
        ctx.arc(x, y, r, 0, TAU)
        ctx.set_source_rgba(1, 1, 1, 0.95)
        ctx.fill()
    rect(ctx, 0, 330, W, 450, '#F4A261')
    rect(ctx, 0, 600, W, 180, '#E76F51', outline=False)
    # cantina
    rr(ctx, 760, 380, 420, 240, 8, '#FFFFFF')
    rect(ctx, 790, 420, 360, 160, '#3D405B')
    text(ctx, 'CANTINA', 970, 370, 46, '#FFFFFF', outline='#1E1E24', lw=10)
    for i in range(7):
        ctx.move_to(780 + i * 60, 380)
        ctx.line_to(810 + i * 60, 330)
        ctx.line_to(840 + i * 60, 380)
        ctx.close_path()
        fill_stroke(ctx, '#E63946' if i % 2 else '#FFFFFF', 4)
    # árvore
    rect(ctx, 260, 420, 60, 360, '#8B5E3C')
    for dx, dy, r in ((0, 0, 140), (-90, 50, 100), (100, 50, 110)):
        ctx.arc(290 + dx, 380 + dy, r, 0, TAU)
        fill_stroke(ctx, '#52B788')
    floor(ctx, 780, '#BFBFBF')
    ctx.set_source_rgba(1, 1, 1, 0.6)
    ctx.set_line_width(8)
    ctx.move_to(0, 900); ctx.line_to(W, 900); ctx.stroke()
    # banco
    rr(ctx, 1450, 720, 360, 40, 8, '#8B5E3C')


def bg_corredor(ctx, t):
    wall(ctx, '#FFFFFF', 760, '#3A86FF', 500)
    for x in (180, 1520):
        rr(ctx, x, 230, 220, 530, 6, '#8B5E3C')
        ctx.arc(x + 190, 500, 12, 0, TAU)
        fill_stroke(ctx, '#FFD23F', 3)
        rr(ctx, x + 40, 260, 140, 90, 6, '#BDE0FE')
    # mural
    rr(ctx, 620, 160, 680, 300, 8, '#DDA15E')
    for i, col in enumerate(('#FFFFFF', '#FFD6A5', '#CAFFBF', '#9BF6FF', '#FFC6FF')):
        ctx.save(); ctx.translate(680 + i * 125, 220 + (i % 2) * 40); ctx.rotate((i % 3 - 1) * 0.08)
        rect(ctx, 0, 0, 100, 120, col, lw=3); ctx.restore()
    text(ctx, 'FESTA JUNINA - SÁB', 960, 430, 40, '#9D0208')
    floor(ctx, 760, '#E9D8A6', tiles=True)


def fx_estojo(ctx, t):
    random.seed(4)
    for i in range(9):
        x = 760 + random.random() * 520
        y = 960 + random.random() * 80
        ctx.save(); ctx.translate(x, y); ctx.rotate(random.random() * 3)
        rrect(ctx, -6, -40, 12, 80, 5)
        fill_stroke(ctx, random.choice(['#E63946', '#2F7DE1', '#2A9D8F', '#FFB703', '#9B5DE5']), 3)
        ctx.restore()


def bg_biblioteca(ctx, t):
    wall(ctx, '#E9EDC9', 760)
    for sx in (60, 1360):
        rect(ctx, sx, 120, 500, 640, '#7F5539')
        for row in range(5):
            y = 150 + row * 120
            rect(ctx, sx + 20, y + 90, 460, 14, '#5C3D2E', lw=3)
            random.seed(row + sx)
            x = sx + 30
            while x < sx + 460:
                w = 20 + random.random() * 22
                h = 60 + random.random() * 28
                rect(ctx, x, y + 90 - h, w, h, random.choice(['#E63946', '#457B9D', '#F4A261', '#2A9D8F', '#E9C46A', '#8338EC']), lw=3)
                x += w + 3
    text(ctx, 'SILÊNCIO', 960, 200, 64, '#9D0208', outline='#FFFFFF', lw=10)
    floor(ctx, 760, '#B08968')


def fg_biblioteca(ctx, t):
    rr(ctx, 380, 800, 640, 40, 8, '#A47148')
    rect(ctx, 420, 840, 20, 240, '#6C584C', lw=3)
    rect(ctx, 960, 840, 20, 240, '#6C584C', lw=3)


def bg_quarto(ctx, t):
    wall(ctx, '#BDB2FF', 780)
    window(ctx, 1300, 140, 360, 300, night=False)
    # pôster
    rr(ctx, 260, 140, 260, 340, 6, '#FFD166')
    star(ctx, 390, 260, 70, '#EF476F')
    text(ctx, 'FUTEBOL', 390, 420, 40, '#073B4C')
    # cama
    rr(ctx, 1150, 620, 680, 160, 20, '#118AB2')
    rr(ctx, 1170, 590, 200, 70, 30, '#FFFFFF')
    floor(ctx, 780, '#C9A27E')


def bg_banheiro(ctx, t):
    wall(ctx, '#E0FBFC', 780)
    # azulejos
    ctx.set_source_rgba(0.6, 0.75, 0.8, 0.5)
    ctx.set_line_width(3)
    for x in range(0, W, 90):
        ctx.move_to(x, 0); ctx.line_to(x, 780)
    for y in range(0, 780, 90):
        ctx.move_to(0, y); ctx.line_to(W, y)
    ctx.stroke()
    # espelho (moldura); o reflexo é desenhado pelo render
    rr(ctx, 1010, 120, 460, 600, 30, '#C9ADA7', 8)
    floor(ctx, 780, '#9DB4C0', tiles=True)


MIRROR = (1040, 150, 400, 540)  # área do reflexo


def fg_banheiro(ctx, t):
    # pia
    rr(ctx, 980, 740, 520, 70, 20, '#FFFFFF')
    rect(ctx, 1180, 810, 120, 270, '#FFFFFF')
    rr(ctx, 1210, 700, 60, 50, 10, '#ADB5BD')


def bg_sofa_vo(ctx, t):
    wall(ctx, '#FFE5D9', 780, '#F4ACB7', 560)
    frame_pic(ctx, 300, 160, 240, 180, '#B5E48C')
    frame_pic(ctx, 1380, 150, 200, 240, '#FFCAD4')
    # santo / crucifixo simples e paninho de crochê
    rr(ctx, 860, 160, 200, 200, 100, '#FFFFFF')
    ctx.set_source_rgba(0.9, 0.6, 0.7, 0.6)
    for i in range(12):
        a = i * TAU / 12
        ctx.arc(960 + math.cos(a) * 80, 260 + math.sin(a) * 80, 14, 0, TAU)
        ctx.fill()
    floor(ctx, 780, '#A98467')
    rr(ctx, 420, 560, 1080, 290, 40, '#6D597A')
    rr(ctx, 860, 540, 200, 40, 8, '#FFFFFF')


def fg_sofa_vo(ctx, t):
    rr(ctx, 380, 650, 90, 270, 40, '#6D597A')
    rr(ctx, 1450, 650, 90, 270, 40, '#6D597A')
    rr(ctx, 440, 810, 1040, 110, 30, '#56445D')


def bg_festa(ctx, t):
    g = cairo.LinearGradient(0, 0, 0, 760)
    g.add_color_stop_rgb(0, 0.05, 0.06, 0.2)
    g.add_color_stop_rgb(1, 0.25, 0.15, 0.35)
    ctx.rectangle(0, 0, W, 760)
    ctx.set_source(g)
    ctx.fill()
    random.seed(7)
    for i in range(70):
        ctx.arc(random.random() * W, random.random() * 420, 1.5 + random.random() * 2.5, 0, TAU)
        ctx.set_source_rgba(1, 1, 1, 0.5 + 0.5 * math.sin(t * 2 + i))
        ctx.fill()
    ctx.arc(1650, 140, 60, 0, TAU)
    ctx.set_source_rgba(1, 0.97, 0.85, 1)
    ctx.fill()
    # barracas
    for x, name, col in ((120, 'PESCARIA', '#E63946'), (720, 'PIPOCA', '#FFB703'), (1340, 'FANTASIA', '#2A9D8F')):
        rect(ctx, x, 420, 460, 340, '#FFF3E0')
        for i in range(8):
            ctx.move_to(x - 20 + i * 62.5, 420)
            ctx.line_to(x + 11 + i * 62.5, 340)
            ctx.line_to(x + 42 + i * 62.5, 420)
            ctx.close_path()
            fill_stroke(ctx, col if i % 2 else '#FFFFFF', 4)
        rr(ctx, x + 60, 450, 340, 70, 10, col)
        text(ctx, name, x + 230, 503, 46, '#FFFFFF', outline='#1E1E24', lw=8)
        rect(ctx, x + 30, 600, 400, 30, '#8B5E3C')
    floor(ctx, 760, '#7A6A53')
    ctx.set_source_rgba(1, 1, 1, 0.35)
    ctx.set_line_width(8)
    ctx.arc(960, 1250, 420, math.pi * 1.1, math.pi * 1.9)
    ctx.stroke()


def fg_festa(ctx, t):
    # bandeirinhas
    random.seed(3)
    for k, (y0, sag) in enumerate(((60, 120), (150, 90))):
        pts = []
        for i in range(0, 41):
            x = i * W / 40
            y = y0 + sag * math.sin(math.pi * i / 40) + 4 * math.sin(t * 2 + i + k)
            pts.append((x, y))
        ctx.set_source_rgba(0.9, 0.9, 0.9, 0.9)
        ctx.set_line_width(3)
        ctx.move_to(*pts[0])
        for p in pts[1:]:
            ctx.line_to(*p)
        ctx.stroke()
        cols = ['#E63946', '#FFB703', '#2A9D8F', '#8338EC', '#06D6A0', '#FF006E']
        for i, (x, y) in enumerate(pts[:-1]):
            ctx.move_to(x, y)
            ctx.line_to(x + 40, y)
            ctx.line_to(x + 40, y + 46)
            ctx.line_to(x + 20, y + 34)
            ctx.line_to(x, y + 46)
            ctx.close_path()
            fill_stroke(ctx, cols[(i + k) % len(cols)], 3)
    # fogueira
    fx = 1780
    for i in range(4):
        ctx.save(); ctx.translate(fx, 1010); ctx.rotate((i - 1.5) * 0.4)
        rr(ctx, -110, -14, 220, 28, 12, '#7F4F24')
        ctx.restore()
    for i, col in enumerate(('#E85D04', '#FAA307', '#FFD60A')):
        s = 1 - i * 0.28
        fl = 1 + 0.08 * math.sin(t * 9 + i)
        ctx.move_to(fx - 90 * s, 1000)
        ctx.curve_to(fx - 100 * s, 900, fx - 20 * s, 860 - 60 * s * fl, fx, 760 + 80 * i - 40 * fl)
        ctx.curve_to(fx + 20 * s, 860 - 60 * s * fl, fx + 100 * s, 900, fx + 90 * s, 1000)
        ctx.close_path()
        setc(ctx, col)
        ctx.fill()


def bg_meiofio(ctx, t):
    g = cairo.LinearGradient(0, 0, 0, 760)
    g.add_color_stop_rgb(0, 0.04, 0.05, 0.16)
    g.add_color_stop_rgb(1, 0.18, 0.12, 0.3)
    ctx.rectangle(0, 0, W, 800)
    ctx.set_source(g)
    ctx.fill()
    random.seed(11)
    for i in range(90):
        ctx.arc(random.random() * W, random.random() * 500, 1.2 + random.random() * 2.4, 0, TAU)
        ctx.set_source_rgba(1, 1, 1, 0.4 + 0.6 * abs(math.sin(t * 1.5 + i)))
        ctx.fill()
    # casas ao fundo
    for i, col in enumerate(('#3D348B', '#7678ED', '#5E548E', '#3D348B', '#7678ED')):
        rect(ctx, i * 400 - 40, 470, 380, 300, col)
        window(ctx, i * 400 + 60, 540, 110, 90, night=True)
        ctx.rectangle(i * 400 + 60, 540, 110, 90)
        ctx.set_source_rgba(1, 0.85, 0.4, 0.55)
        ctx.fill()
    # poste
    rect(ctx, 1600, 200, 26, 600, '#4A4E69')
    ctx.arc(1613, 200, 40, 0, TAU)
    ctx.set_source_rgba(1, 0.92, 0.6, 1)
    ctx.fill()
    g2 = cairo.RadialGradient(1613, 260, 10, 1613, 600, 500)
    g2.add_color_stop_rgba(0, 1, 0.9, 0.6, 0.35)
    g2.add_color_stop_rgba(1, 1, 0.9, 0.6, 0)
    ctx.rectangle(0, 0, W, H)
    ctx.set_source(g2)
    ctx.fill()
    # calçada e rua
    rect(ctx, 0, 770, W, 120, '#8D99AE')
    rect(ctx, 0, 870, W, 30, '#EDF2F4')
    rect(ctx, 0, 900, W, 180, '#2B2D42', outline=False)
    ctx.set_source_rgba(1, 0.85, 0.2, 0.9)
    for i in range(0, W, 220):
        ctx.rectangle(i, 1000, 120, 14)
    ctx.fill()


def bg_ciencia(ctx, t):
    g = cairo.LinearGradient(0, 0, W, H)
    g.add_color_stop_rgb(0, 0.12, 0.16, 0.32)
    g.add_color_stop_rgb(1, 0.22, 0.1, 0.35)
    ctx.rectangle(0, 0, W, H)
    ctx.set_source(g)
    ctx.fill()
    ctx.set_source_rgba(1, 1, 1, 0.05)
    ctx.set_line_width(2)
    for x in range(0, W, 60):
        ctx.move_to(x, 0); ctx.line_to(x, H)
    for y in range(0, H, 60):
        ctx.move_to(0, y); ctx.line_to(W, y)
    ctx.stroke()
    floor(ctx, 860, '#2B2D42')


def bg_plain(col1, col2):
    def f(ctx, t):
        g = cairo.LinearGradient(0, 0, 0, H)
        a, b = hexc(col1), hexc(col2)
        g.add_color_stop_rgb(0, a[0], a[1], a[2])
        g.add_color_stop_rgb(1, b[0], b[1], b[2])
        ctx.rectangle(0, 0, W, H)
        ctx.set_source(g)
        ctx.fill()
    return f


def bg_feira(ctx, t):
    g = cairo.LinearGradient(0, 0, 0, 700)
    g.add_color_stop_rgb(0, 0.52, 0.8, 0.98)
    g.add_color_stop_rgb(1, 0.85, 0.94, 1)
    ctx.rectangle(0, 0, W, 780); ctx.set_source(g); ctx.fill()
    for x, y, r in ((260, 120, 46), (320, 100, 60), (390, 125, 44), (1500, 90, 40), (1560, 80, 52)):
        ctx.arc(x, y, r, 0, TAU); ctx.set_source_rgba(1, 1, 1, 0.95); ctx.fill()
    # prédios ao fundo
    for i, col in enumerate(('#F4A261', '#E9C46A', '#E76F51', '#2A9D8F', '#F4A261', '#E9C46A')):
        rect(ctx, i * 330 - 20, 220 + (i % 2) * 60, 320, 560, col)
        for k in range(3):
            window(ctx, i * 330 + 50 + k * 90, 300 + (i % 2) * 60, 50, 60)
    floor(ctx, 780, '#9C9C9C')
    # barracas
    for x, col, prod in ((80, '#E63946', '#E63946'), (720, '#2A9D8F', '#F4A261'), (1360, '#FFB703', '#8AC926')):
        rect(ctx, x + 20, 430, 14, 360, '#6C757D', lw=3)
        rect(ctx, x + 446, 430, 14, 360, '#6C757D', lw=3)
        ctx.move_to(x - 20, 470); ctx.line_to(x + 240, 380); ctx.line_to(x + 500, 470); ctx.close_path()
        fill_stroke(ctx, col)
        for k in range(6):
            ctx.move_to(x - 20 + k * 87, 470); ctx.line_to(x + 23 + k * 87, 500); ctx.line_to(x + 67 + k * 87, 470); ctx.close_path()
            fill_stroke(ctx, '#FFFFFF' if k % 2 else col, 3)
        rr(ctx, x, 640, 480, 70, 8, '#8B5E3C')
        random.seed(x)
        for k in range(14):
            ctx.arc(x + 30 + k * 32 + random.random() * 6, 625 - (k % 2) * 18, 20, 0, TAU)
            fill_stroke(ctx, prod, 3)
    rr(ctx, 1500, 540, 200, 70, 8, '#FFFFFF')
    text(ctx, 'R$ 5', 1600, 592, 46, '#C1121F')


def bg_quadra(ctx, t):
    g = cairo.LinearGradient(0, 0, 0, 600)
    g.add_color_stop_rgb(0, 0.5, 0.78, 0.98)
    g.add_color_stop_rgb(1, 0.85, 0.94, 1)
    ctx.rectangle(0, 0, W, 700); ctx.set_source(g); ctx.fill()
    # alambrado
    ctx.set_source_rgba(0.35, 0.4, 0.45, 0.55); ctx.set_line_width(3)
    for i in range(-40, 80):
        ctx.move_to(i * 40, 160); ctx.line_to(i * 40 + 540, 700)
        ctx.move_to(i * 40, 160); ctx.line_to(i * 40 - 540, 700)
    ctx.stroke()
    rect(ctx, 0, 150, W, 14, '#6C757D', lw=3)
    rect(ctx, 0, 680, W, 780 - 680, '#5C677D')
    floor(ctx, 760, '#4D908E')
    ctx.set_source_rgba(1, 1, 1, 0.85); ctx.set_line_width(8)
    ctx.move_to(0, 960); ctx.line_to(W, 960); ctx.stroke()
    ctx.arc(1000, 1100, 260, math.pi, TAU); ctx.stroke()
    # gol à direita
    ctx.set_source_rgba(1, 1, 1, 1); ctx.set_line_width(16)
    ctx.move_to(1560, 1000); ctx.line_to(1560, 640); ctx.line_to(1880, 640); ctx.line_to(1880, 1000); ctx.stroke()
    ctx.set_source_rgba(1, 1, 1, 0.35); ctx.set_line_width(2)
    for k in range(1600, 1880, 24):
        ctx.move_to(k, 640); ctx.line_to(k, 1000)
    for k in range(660, 1000, 24):
        ctx.move_to(1560, k); ctx.line_to(1880, k)
    ctx.stroke()


def bg_salao(ctx, t):
    wall(ctx, '#FFF1E6', 780, '#E8C2CA', 560)
    # faixa
    rr(ctx, 460, 70, 1000, 120, 16, '#C9184A')
    text(ctx, '80 ANOS DA VÓ CIDA', 960, 152, 66, '#FFFFFF', outline='#590D22', lw=10)
    # balões dourados e rosa
    for k, (x, y) in enumerate(((150, 160), (260, 120), (1660, 150), (1780, 110), (360, 230), (1560, 230))):
        bob = 8 * math.sin(t * 1.5 + k)
        ctx.set_source_rgba(0.4, 0.4, 0.4, 0.8); ctx.set_line_width(2)
        ctx.move_to(x, y + 70 + bob); ctx.line_to(x + 10, y + 260); ctx.stroke()
        ctx.save(); ctx.translate(x, y + bob); ctx.scale(0.85, 1.0); ctx.arc(0, 0, 70, 0, TAU); ctx.restore()
        fill_stroke(ctx, '#F4C430' if k % 2 == 0 else '#FF8FAB', 4)
    floor(ctx, 780, '#C9A27E', tiles=True)
    # mesa com bolo
    rr(ctx, 1440, 640, 420, 140, 10, '#FFFFFF')
    ctx.save(); ctx.translate(1650, 640); ctx.scale(1, 0.3); ctx.arc(0, 0, 110, 0, TAU); ctx.restore()
    fill_stroke(ctx, '#FFFFFF', 4)
    rect(ctx, 1570, 520, 160, 120, '#FFB5C2')
    text(ctx, '80', 1650, 610, 70, '#C9184A')


def bg_salao_posse(ctx, t):
    """ep04: salão da escola na posse do representante de turma (faixa azul, bandeirinhas, púlpito)."""
    wall(ctx, '#EAF4FF', 780, '#BBD3EE', 560)
    rr(ctx, 380, 70, 1160, 120, 16, '#1D4E89')
    text(ctx, 'POSSE DO REPRESENTANTE', 960, 152, 62, '#FFFFFF', outline='#0B2545', lw=10)
    # bandeirinhas
    cols = ['#E63946', '#FFB703', '#2A9D8F', '#8338EC', '#06D6A0']
    for row, y0 in ((0, 250), (1, 330)):
        ctx.set_source_rgba(0.3, 0.3, 0.3, 1); ctx.set_line_width(3)
        ctx.move_to(0, y0); ctx.curve_to(640, y0 + 50, 1280, y0 + 50, 1920, y0); ctx.stroke()
        for k in range(16):
            x = 40 + k * 120 + row * 60
            y = y0 + 50 * math.sin(math.pi * x / 1920) * 0.75
            ctx.move_to(x - 28, y); ctx.line_to(x + 28, y); ctx.line_to(x, y + 50 + 3 * math.sin(t * 2 + k)); ctx.close_path()
            fill_stroke(ctx, cols[(k + row) % len(cols)], 3)
    floor(ctx, 780, '#C9A27E', tiles=True)
    # palco ao fundo
    rect(ctx, 0, 700, 1920, 80, '#8D5A3B')
    # púlpito com microfone
    rect(ctx, 1590, 560, 140, 220, '#A47148')
    rect(ctx, 1570, 540, 180, 30, '#7F5539')
    ctx.set_source_rgba(0.15, 0.15, 0.18, 1); ctx.set_line_width(6)
    ctx.move_to(1660, 540); ctx.line_to(1640, 470); ctx.stroke()
    ctx.arc(1636, 462, 14, 0, TAU); fill_stroke(ctx, '#495057', 3)


def bg_quarto_noite(ctx, t):
    wall(ctx, '#3C3A6B', 780)
    window(ctx, 1300, 140, 360, 300, night=True)
    rr(ctx, 260, 140, 260, 340, 6, '#5A5891')
    star(ctx, 390, 260, 70, '#8D8BC4')
    rr(ctx, 1150, 620, 680, 160, 20, '#2B2D5E')
    rr(ctx, 1170, 590, 200, 70, 30, '#8D8BC4')
    floor(ctx, 780, '#2E2C52')
    ctx.rectangle(0, 0, W, H); ctx.set_source_rgba(0.05, 0.05, 0.2, 0.25); ctx.fill()


def bg_onibus(ctx, t):
    wall(ctx, '#DDE5ED', 780)
    # janelas com paisagem passando
    for k in range(4):
        x = 120 + k * 450
        rr(ctx, x - 10, 130, 380, 300, 16, '#ADB5BD')
        ctx.save(); rrect(ctx, x, 140, 360, 280, 12); ctx.clip()
        g = cairo.LinearGradient(0, 140, 0, 420)
        g.add_color_stop_rgb(0, 0.95, 0.75, 0.55); g.add_color_stop_rgb(1, 0.98, 0.9, 0.75)
        ctx.rectangle(x, 140, 360, 280); ctx.set_source(g); ctx.fill()
        off = (t * 400) % 300
        for b in range(-1, 4):
            bx = x - off + b * 150
            ctx.rectangle(bx, 260 + (b % 2) * 30, 110, 200); ctx.set_source_rgba(0.45, 0.4, 0.55, 0.9); ctx.fill()
        ctx.restore()
    # barra de apoio
    ctx.set_source_rgba(0.75, 0.76, 0.78, 1); ctx.set_line_width(14)
    ctx.move_to(0, 90); ctx.line_to(W, 90); ctx.stroke()
    for k in range(6):
        ctx.arc(150 + k * 330, 130, 26, 0, TAU); ctx.set_source_rgba(0.95, 0.75, 0.2, 1); ctx.set_line_width(8); ctx.stroke()
    floor(ctx, 780, '#495057')
    # bancos
    for x in (420, 1150):
        rr(ctx, x - 230, 560, 460, 260, 30, '#1D3557')


def fg_onibus(ctx, t):
    for x in (420, 1150):
        rr(ctx, x - 250, 800, 500, 90, 20, '#274472')


BG = {
    'jantar': (bg_jantar, fg_jantar),
    'sala': (bg_sala, fg_sala),
    'portao': (bg_portao, None),
    'classe': (bg_classe, fg_classe),
    'patio': (bg_patio, None),
    'corredor': (bg_corredor, None),
    'biblioteca': (bg_biblioteca, fg_biblioteca),
    'quarto': (bg_quarto, None),
    'banheiro': (bg_banheiro, fg_banheiro),
    'sofa_vo': (bg_sofa_vo, fg_sofa_vo),
    'festa': (bg_festa, fg_festa),
    'meiofio': (bg_meiofio, None),
    'ciencia': (bg_ciencia, None),
    'caderno': (bg_plain('#3D405B', '#22223B'), None),
    'ranking': (bg_plain('#1B1B3A', '#3A0CA3'), None),
    'placar': (bg_plain('#10002B', '#3C096C'), None),
    'whatsapp': (bg_plain('#0B3D2E', '#081C15'), None),
    'final': (bg_plain('#3A0CA3', '#7209B7'), None),
    'feira': (bg_feira, None),
    'onibus': (bg_onibus, fg_onibus),
    'quadra': (bg_quadra, None),
    'salao': (bg_salao, None),
    'salao_posse': (bg_salao_posse, None),
    'quarto_noite': (bg_quarto_noite, None),
    'desenho': (bg_plain('#6D4C41', '#4E342E'), None),
    'lista': (bg_plain('#1B1B3A', '#3A0CA3'), None),
}

# slots: (x, y_pés, escala)
SLOTS = {
    'jantar': dict(m1=(380, 850, 0.8), m2=(680, 840, 0.8), m3=(960, 850, 0.8), m4=(1250, 850, 0.8), m5=(1560, 850, 0.84)),
    'sala': dict(a=(560, 875, 0.9), b=(960, 875, 0.9)),
    'portao': dict(a=(1300, 1000, 0.95), b=(700, 1000, 0.95)),
    'classe': dict(prof=(330, 980, 0.85), d1=(700, 930, 0.8), d2=(1100, 930, 0.8), d3=(1500, 930, 0.8)),
    'patio': dict(a=(620, 1010, 0.95), b=(1250, 1010, 0.95), c=(960, 1010, 0.95), d=(330, 1010, 0.9)),
    'corredor': dict(a=(700, 1000, 0.95), b=(1220, 1000, 0.95)),
    'biblioteca': dict(a=(700, 930, 0.85), b=(1300, 1010, 0.95)),
    'quarto': dict(a=(760, 1010, 1.0)),
    'banheiro': dict(a=(650, 1050, 1.05)),
    'sofa_vo': dict(a=(760, 875, 0.9), b=(1160, 875, 0.9)),
    'festa': dict(f1=(380, 1010, 0.85), f2=(1240, 1010, 0.9), c=(840, 1010, 0.9), f4=(1460, 1010, 0.85)),
    'meiofio': dict(a=(760, 960, 0.9), b=(1130, 960, 0.9)),
    'ciencia': dict(a=(620, 1000, 0.9), b=(1300, 1000, 0.9)),
    'final': dict(c=(560, 1020, 1.0)),
    'feira': dict(a=(560, 1010, 0.95), b=(980, 1010, 0.95), c=(1560, 1010, 0.95)),
    'quadra': dict(a=(500, 1010, 0.9), b=(1000, 1010, 0.95), gol=(1720, 1000, 0.85), gol2=(1640, 980, 0.85),
                   alto=(1520, 680, 0.8), c=(1330, 1010, 0.9)),  # alto (alguém erguido no ar) e c: ep05
    'salao': dict(a=(330, 1010, 0.9), b=(700, 1010, 0.9), c=(1060, 1010, 0.95), d=(1400, 1010, 0.8), e=(1700, 1010, 0.9)),
    'salao_posse': dict(a=(330, 1010, 0.9), b=(700, 1010, 0.9), c=(1060, 1010, 0.95), d=(1400, 1010, 0.8), e=(1700, 1010, 0.9)),
    'quarto_noite': dict(a=(760, 1010, 1.0)),
    'onibus': dict(a=(300, 870, 0.85), b=(1030, 870, 0.9), c=(1290, 870, 0.9)),
}


# ---------------------------------------------------------------- ep03: porão-bunker da escola
def dog_doodle(ctx, x, y, s, col='#FFFFFF', ink=(0.12, 0.1, 0.2), crown=False):
    """cachorrinho em giz (o desenho da Bia)."""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.set_line_width(6); ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.arc(0, 0, 40, 0, TAU); setc(ctx, col); ctx.fill_preserve()
    ctx.set_source_rgba(*ink, 1); ctx.stroke()
    for sx in (-1, 1):
        ctx.save(); ctx.translate(sx * 36, -6); ctx.rotate(sx * 0.35); ctx.scale(0.45, 1)
        ctx.arc(0, 0, 30, 0, TAU); ctx.restore()
        ctx.set_source_rgba(0.55, 0.35, 0.2, 1); ctx.fill_preserve(); ctx.set_source_rgba(*ink, 1); ctx.stroke()
        ctx.arc(sx * 14, -8, 5, 0, TAU); ctx.fill()
    ctx.arc(0, 10, 8, 0, TAU); ctx.fill()
    ctx.arc(0, 18, 12, 0.2, TAU / 2 - 0.2); ctx.stroke()
    if crown:
        ctx.move_to(-26, -38); ctx.line_to(-26, -66); ctx.line_to(-12, -50); ctx.line_to(0, -72)
        ctx.line_to(12, -50); ctx.line_to(26, -66); ctx.line_to(26, -38); ctx.close_path()
        fill_stroke(ctx, '#FFD23F', 4)
    ctx.restore()


MURAL = [(660, 250, 'MÃE', 1.1), (820, 300, 'VÓ CIDA', 1.1), (1110, 300, 'DAVI', 1.1), (1270, 250, 'SEU JORGE', 1.1),
         (660, 455, 'PROF. NEIDE', 1.0), (1330, 450, 'SEU VALDIR', 1.1), (810, 565, 'TIA MARTA', 0.95),
         (1150, 565, 'PADARIA', 0.95), (965, 420, 'LARI', 1.7)]


def porao(rotina=False, mural=0, night=False):
    def f(ctx, t):
        # parede de blocos
        wall(ctx, '#6C7A89', 800)
        ctx.set_source_rgba(0, 0, 0, 0.12); ctx.set_line_width(3)
        for r in range(0, 11):
            y = 40 + r * 75
            ctx.move_to(0, y); ctx.line_to(W, y); ctx.stroke()
            for k in range(0, 14):
                x = k * 160 + (80 if r % 2 else 0)
                ctx.move_to(x, y); ctx.line_to(x, y + 75); ctx.stroke()
        # canos no teto
        for y, c in ((30, '#9E2A2B'), (62, '#ADB5BD')):
            rect(ctx, 0, y, W, 22, c, lw=4)
        # janelinha alta com grade
        rr(ctx, 230, 110, 330, 170, 6, '#3D405B')
        g = cairo.LinearGradient(0, 120, 0, 270)
        if night:
            g.add_color_stop_rgb(0, 0.08, 0.1, 0.25); g.add_color_stop_rgb(1, 0.2, 0.18, 0.4)
        else:
            g.add_color_stop_rgb(0, 0.55, 0.85, 1); g.add_color_stop_rgb(1, 0.6, 0.85, 0.5)
        ctx.rectangle(245, 125, 300, 140); ctx.set_source(g); ctx.fill()
        for k in range(1, 6):
            rect(ctx, 245 + k * 50 - 5, 125, 10, 140, '#495057', lw=2)
        if not night:
            ctx.move_to(245, 265); ctx.line_to(545, 265); ctx.line_to(900, 800); ctx.line_to(300, 800); ctx.close_path()
            ctx.set_source_rgba(1, 0.97, 0.8, 0.10); ctx.fill()
        # porta de cofre com o relógio
        ctx.arc(1660, 470, 240, 0, TAU); fill_stroke(ctx, '#8D99AE', 8)
        ctx.arc(1660, 470, 200, 0, TAU); fill_stroke(ctx, '#ADB5BD', 5)
        ctx.set_source_rgba(*OUT); ctx.set_line_width(14)
        for k in range(6):
            a = k * TAU / 6 + t * 0.0
            ctx.move_to(1660, 470); ctx.line_to(1660 + 110 * math.cos(a), 470 + 110 * math.sin(a)); ctx.stroke()
        ctx.arc(1660, 470, 34, 0, TAU); fill_stroke(ctx, '#495057', 5)
        rr(ctx, 1560, 190, 200, 70, 10, '#1B1B1E')
        text(ctx, '30 DIAS', 1660, 240, 40, '#FF4D4D')
        # prateleira com caixas
        rect(ctx, 20, 430, 300, 16, '#7F5539', lw=4)
        rect(ctx, 20, 600, 300, 16, '#7F5539', lw=4)
        for x, y, w, h, c in ((40, 340, 120, 90, '#D4A373'), (170, 370, 130, 60, '#E9C46A'), (50, 520, 250, 80, '#D4A373')):
            rect(ctx, x, y, w, h, c, lw=4)
        text(ctx, 'FESTA JUNINA', 175, 572, 26, '#5C3D2E', bold=True)
        if rotina:
            ctx.save(); ctx.translate(335, 330); ctx.rotate(-0.03)
            rect(ctx, 0, 0, 230, 290, '#FFFFFF', lw=4)
            for k, s in enumerate(('7h acordar', '8h aula', '12h marmita', '15h dama', '21h estrelas')):
                text(ctx, s, 115, 50 + k * 52, 26, '#1D3557', bold=True)
            ctx.restore()
        for k, (x, y, name, sc) in enumerate(MURAL[:mural]):
            dog_doodle(ctx, x, y, sc, crown=(name == 'LARI'))
            text(ctx, name, x, y + 50 + 30 * sc, 26 if sc < 1.5 else 34, '#FFFFFF', outline='#1B1B1E', lw=7)
        floor(ctx, 800, '#4A4E69')
        # colchonetes
        rr(ctx, 380, 880, 380, 60, 14, '#3A86FF')
        rr(ctx, 1100, 880, 380, 60, 14, '#FF5D8F')
        # lâmpada pendurada
        ctx.set_source_rgba(*OUT); ctx.set_line_width(4)
        ctx.move_to(960, 84); ctx.line_to(960, 170); ctx.stroke()
        ctx.arc(960, 185, 22, 0, TAU); fill_stroke(ctx, '#FFF3B0', 4)
        if night:
            ctx.rectangle(0, 0, W, H); ctx.set_source_rgba(0.04, 0.04, 0.18, 0.45); ctx.fill()
            rg = cairo.RadialGradient(960, 185, 10, 960, 185, 700)
            rg.add_color_stop_rgba(0, 1, 0.9, 0.6, 0.35); rg.add_color_stop_rgba(1, 1, 0.9, 0.6, 0)
            ctx.rectangle(0, 0, W, H); ctx.set_source(rg); ctx.fill()
    return f


def fg_cortina(ctx, t):
    """cortina de cobertores no meio do porão: o lado dela e o seu lado."""
    ctx.set_source_rgba(*OUT); ctx.set_line_width(5)
    ctx.move_to(880, 300); ctx.line_to(1040, 300); ctx.stroke()
    for k, c in enumerate(('#E76F51', '#2A9D8F', '#E9C46A')):
        x = 880 + k * 54
        sw = 4 * math.sin(t * 1.3 + k)
        ctx.move_to(x, 300); ctx.line_to(x + 54, 300); ctx.line_to(x + 58 + sw, 1000); ctx.line_to(x - 2 + sw, 1000); ctx.close_path()
        fill_stroke(ctx, c, 4)


def bg_grade(ctx, t):
    """lado de fora: a janelinha do porão rente ao chão, no fundo da escola."""
    g = cairo.LinearGradient(0, 0, 0, 500)
    g.add_color_stop_rgb(0, 0.5, 0.78, 0.98); g.add_color_stop_rgb(1, 0.82, 0.93, 1)
    ctx.rectangle(0, 0, W, 800); ctx.set_source(g); ctx.fill()
    for x, y, r in ((1500, 120, 50), (1560, 100, 64), (1630, 125, 46)):
        ctx.arc(x, y, r, 0, TAU); ctx.set_source_rgba(1, 1, 1, 0.95); ctx.fill()
    rect(ctx, -10, 200, W + 20, 640, '#F4D35E')
    rect(ctx, -10, 200, W + 20, 40, '#EE964B')
    for x in (200, 700, 1220, 1700):
        window(ctx, x - 110, 300, 220, 200)
    floor(ctx, 840, '#74C69D')
    # janelinha do porão
    rr(ctx, 820, 690, 280, 150, 6, '#3D405B')
    ctx.rectangle(835, 705, 250, 125); ctx.set_source_rgba(0.08, 0.08, 0.15, 1); ctx.fill()
    for k in range(1, 5):
        rect(ctx, 835 + k * 50 - 5, 705, 10, 125, '#6C757D', lw=2)
    # placa
    rr(ctx, 830, 560, 260, 100, 10, '#FFFFFF')
    text(ctx, 'NÃO ALIMENTE', 960, 602, 26, '#C9184A')
    text(ctx, 'OS ALUNOS', 960, 640, 26, '#C9184A')


BG.update({
    'porao': (porao(), None),
    'porao_cortina': (porao(), fg_cortina),
    'porao_rotina': (porao(rotina=True), fg_cortina),
    'porao_noite': (porao(rotina=True, night=True), fg_cortina),
    'porao_mural': (porao(rotina=True, mural=len(MURAL)), None),
    'porao_meio': (porao(rotina=True, mural=5), None),
    'grade': (bg_grade, None),
})
SLOTS.update({
    'porao': dict(a=(640, 960, 0.92), b=(1280, 960, 0.92), c=(960, 960, 0.92)),
    'grade': dict(a=(560, 1010, 0.95), b=(1360, 1010, 0.95), c=(1640, 1010, 0.9), d=(300, 1010, 0.9)),
})
SLOTS['porao_meio'] = SLOTS['porao']
for _k in ('porao_cortina', 'porao_rotina', 'porao_noite'):
    SLOTS[_k] = dict(a=(620, 960, 0.92), b=(1300, 960, 0.92))
SLOTS['porao_mural'] = dict(SLOTS['porao'], d=(360, 1000, 0.9), e=(1560, 1000, 0.9), f=(1780, 1010, 0.85), g=(160, 1010, 0.85))


# ---------------------------------------------------------------- ep06: shopping ilhado pela enchente
def rain(ctx, t, x0, y0, x1, y1, n=70, a=0.45, seed=21):
    random.seed(seed)
    ctx.set_source_rgba(0.85, 0.92, 1, a); ctx.set_line_width(3)
    for k in range(n):
        x = x0 + random.random() * (x1 - x0)
        y = y0 + ((random.random() * (y1 - y0) + t * 900) % (y1 - y0))
        ctx.move_to(x, y); ctx.line_to(x - 8, y + 34)
    ctx.stroke()


def storefront(ctx, x, y, w, h, col, name, kind):
    """vitrine de loja do shopping (sem marca)."""
    rect(ctx, x, y, w, h, '#FFFFFF', lw=5)
    rr(ctx, x + 14, y + 12, w - 28, 74, 12, col)
    text(ctx, name, x + w / 2, y + 66, 40 if len(name) < 11 else 34, '#FFFFFF', outline='#1B1B1E', lw=6)
    gx, gy, gw, gh = x + 20, y + 100, w - 40, h - 110
    g = cairo.LinearGradient(gx, gy, gx + gw, gy + gh)
    g.add_color_stop_rgb(0, 0.78, 0.9, 0.97); g.add_color_stop_rgb(1, 0.62, 0.78, 0.9)
    ctx.rectangle(gx, gy, gw, gh); ctx.set_source(g); ctx.fill()
    if kind == 'colchao':
        for k in range(3):
            rr(ctx, gx + 20, gy + gh - 60 - k * 52, gw - 40, 46, 14, ('#4CC9F0', '#F72585', '#FFFFFF')[k], 4)
    elif kind == 'brinquedo':
        for k, c in enumerate(('#FFD23F', '#8338EC', '#06D6A0', '#FF5D8F')):
            ctx.arc(gx + 45 + k * (gw - 90) / 3, gy + gh - 50, 30, 0, TAU); fill_stroke(ctx, c, 4)
        star(ctx, gx + gw / 2, gy + 70, 34, '#FFD23F')
    elif kind == 'pastel':
        rr(ctx, gx + 10, gy + gh - 90, gw - 20, 90, 8, '#F4A261', 4)
        for k in range(4):
            ctx.save(); ctx.translate(gx + 50 + k * (gw - 100) / 3, gy + gh - 110); ctx.scale(0.7, 0.7)
            ctx.move_to(-48, 10); ctx.curve_to(-46, -46, 46, -46, 48, 10); ctx.close_path(); fill_stroke(ctx, '#F2B84B', 4)
            ctx.restore()
    elif kind == 'cinema':
        rect(ctx, gx, gy, gw, gh, '#3C1053', lw=4)
        for k in range(10):
            ctx.arc(gx + 20 + k * (gw - 40) / 9, gy + 16, 7, 0, TAU)
            ctx.set_source_rgba(1, 0.85, 0.3, 1); ctx.fill()
        rr(ctx, gx + 30, gy + 50, gw - 60, gh - 90, 8, '#FFFFFF', 4)
        text(ctx, 'O PINGUIM', gx + gw / 2, gy + gh / 2, 30, '#3C1053')
        text(ctx, 'BOMBEIRO', gx + gw / 2, gy + gh / 2 + 36, 30, '#E63946')
    elif kind == 'roupa':
        for k, c in enumerate(('#E76F51', '#2A9D8F', '#E9C46A', '#8338EC')):
            cx = gx + 40 + k * (gw - 80) / 3
            ctx.move_to(cx - 30, gy + 60); ctx.line_to(cx + 30, gy + 60); ctx.line_to(cx + 36, gy + 150); ctx.line_to(cx - 36, gy + 150); ctx.close_path()
            fill_stroke(ctx, c, 4)
    # moldura do vidro
    ctx.rectangle(gx, gy, gw, gh); ctx.set_source_rgba(*OUT); ctx.set_line_width(4); ctx.stroke()
    ctx.set_source_rgba(1, 1, 1, 0.3)
    ctx.move_to(gx + 30, gy); ctx.line_to(gx + 80, gy); ctx.line_to(gx + 10, gy + gh); ctx.line_to(gx - 40 if gx > 40 else gx, gy + gh); ctx.close_path(); ctx.fill()


def shopping(night=False):
    def f(ctx, t):
        wall(ctx, '#F3E9DC', 800)
        # claraboia com chuva
        g = cairo.LinearGradient(0, 0, 0, 70)
        if night:
            g.add_color_stop_rgb(0, 0.1, 0.12, 0.25); g.add_color_stop_rgb(1, 0.2, 0.22, 0.35)
        else:
            g.add_color_stop_rgb(0, 0.55, 0.6, 0.68); g.add_color_stop_rgb(1, 0.72, 0.76, 0.82)
        ctx.rectangle(0, 0, W, 70); ctx.set_source(g); ctx.fill()
        rain(ctx, t, 0, 0, W, 70, n=40, a=0.5)
        for x in range(0, W, 160):
            rect(ctx, x, 0, 10, 70, '#ADB5BD', lw=2)
        rect(ctx, 0, 66, W, 14, '#ADB5BD', lw=3)
        # andar de cima: lojas pequenas + guarda-corpo de vidro
        for k, c in enumerate(('#90BE6D', '#F9844A', '#577590', '#F94144', '#43AA8B', '#F8961E')):
            rect(ctx, 20 + k * 320, 110, 300, 190, '#FFFFFF', lw=4)
            rr(ctx, 34 + k * 320, 120, 272, 46, 8, c, 4)
            ctx.rectangle(40 + k * 320, 176, 260, 116); ctx.set_source_rgba(0.7, 0.85, 0.95, 1); ctx.fill()
        rect(ctx, 0, 300, W, 26, '#D6CCC2', lw=4)
        ctx.rectangle(0, 326, W, 70); ctx.set_source_rgba(0.7, 0.88, 0.95, 0.55); ctx.fill()
        rect(ctx, 0, 326, W, 8, '#ADB5BD', lw=2)
        for x in range(0, W, 120):
            rect(ctx, x, 326, 6, 70, '#ADB5BD', lw=1)
        rect(ctx, 0, 396, W, 24, '#D6CCC2', lw=4)
        # lojas do térreo
        lojas = (('PASTELARIA', '#E76F51', 'pastel'), ('COLCHÕES', '#3A86FF', 'colchao'),
                 ('BRINQUEDOS', '#8338EC', 'brinquedo'), ('CINEMA', '#C9184A', 'cinema'))
        for k, (n, c, kd) in enumerate(lojas):
            storefront(ctx, 30 + k * 360, 440, 345, 360, c, n, kd)
        # escada rolante (parada)
        ctx.move_to(1500, 800); ctx.line_to(1580, 800); ctx.line_to(1920, 420); ctx.line_to(1920, 360); ctx.line_to(1840, 360); ctx.close_path()
        fill_stroke(ctx, '#ADB5BD', 5)
        ctx.set_source_rgba(0.3, 0.3, 0.35, 0.5); ctx.set_line_width(3)
        for k in range(1, 12):
            px = 1540 + k * 32; py = 800 - k * 36
            ctx.move_to(px - 30, py); ctx.line_to(px + 30, py)
        ctx.stroke()
        ctx.move_to(1490, 780); ctx.line_to(1860, 340); ctx.set_source_rgba(*OUT); ctx.set_line_width(10); ctx.stroke()
        rr(ctx, 1620, 560, 150, 44, 8, '#FFD23F', 3)
        text(ctx, 'PARADA', 1695, 594, 28, '#1B1B1E')
        floor(ctx, 800, '#E9E3D5', tiles=True)
        # vaso de planta
        rr(ctx, 1450, 860, 90, 90, 10, '#BC6C25', 4)
        for a in (-0.6, -0.2, 0.2, 0.6):
            ctx.save(); ctx.translate(1495, 860); ctx.rotate(a); ctx.scale(0.35, 1)
            ctx.arc(0, -70, 70, 0, TAU); ctx.restore(); fill_stroke(ctx, '#2D6A4F', 3)
        if night:
            ctx.rectangle(0, 0, W, H); ctx.set_source_rgba(0.03, 0.04, 0.2, 0.62); ctx.fill()
            for x in (300, 960, 1620):
                rg = cairo.RadialGradient(x, 70, 10, x, 70, 500)
                rg.add_color_stop_rgba(0, 0.6, 1, 0.7, 0.25); rg.add_color_stop_rgba(1, 0.6, 1, 0.7, 0)
                ctx.rectangle(0, 0, W, H); ctx.set_source(rg); ctx.fill()
    return f


def bg_praca(ctx, t):
    """praça de alimentação vazia."""
    wall(ctx, '#FFE8D6', 780, '#FFD6BA', 560)
    balcoes = (('PASTEL', '#E76F51'), ('SUCO', '#2A9D8F'), ('PRATO FEITO', '#F4A261'), ('SORVETE', '#FF8FAB'))
    for k, (n, c) in enumerate(balcoes):
        x = 40 + k * 470
        rect(ctx, x, 120, 440, 440, '#FFFFFF', lw=5)
        rr(ctx, x + 16, 136, 408, 80, 12, c)
        text(ctx, n, x + 220, 194, 46, '#FFFFFF', outline='#1B1B1E', lw=7)
        rect(ctx, x + 30, 236, 380, 120, '#22223B', lw=4)
        for r in range(3):
            ctx.rectangle(x + 50, 256 + r * 34, 200, 14); ctx.set_source_rgba(1, 1, 1, 0.75); ctx.fill()
            text(ctx, 'R$ ' + str(6 + r * 3 + k), x + 360, 272 + r * 34, 24, '#FFD23F')
        rect(ctx, x + 10, 470, 420, 110, c, lw=5)
    floor(ctx, 780, '#E9E3D5', tiles=True)
    # mesas ao fundo
    for x in (260, 760, 1660):
        ctx.save(); ctx.translate(x, 800); ctx.scale(1, 0.3); ctx.arc(0, 0, 110, 0, TAU); ctx.restore()
        fill_stroke(ctx, '#FFFFFF', 4)
        rect(ctx, x - 8, 800, 16, 80, '#6C757D', lw=3)


def fg_praca(ctx, t):
    # mesa no primeiro plano, entre os dois
    ctx.save(); ctx.translate(960, 900); ctx.scale(1, 0.32); ctx.arc(0, 0, 230, 0, TAU); ctx.restore()
    fill_stroke(ctx, '#FFFFFF', 5)
    rect(ctx, 945, 920, 30, 160, '#6C757D', lw=4)
    for dx in (-60, 60):
        ctx.save(); ctx.translate(960 + dx, 880); ctx.scale(0.75, 0.75)
        ctx.move_to(-48, 10); ctx.curve_to(-46, -46, 46, -46, 48, 10); ctx.close_path(); fill_stroke(ctx, '#F2B84B', 4)
        ctx.restore()


def bg_colchoes(ctx, t):
    wall(ctx, '#CFE8FF', 780, '#A9D2FF', 600)
    rr(ctx, 600, 185, 720, 84, 18, '#3A86FF')
    text(ctx, 'COLCHÕES', 960, 247, 58, '#FFFFFF', outline='#0B2545', lw=9)
    # colchões em pé encostados na parede
    for k, c in enumerate(('#FFFFFF', '#F72585', '#4CC9F0', '#FFD23F', '#FFFFFF', '#06D6A0')):
        x = 60 + k * 310
        if 560 < x + 125 < 1360:
            rr(ctx, x, 290, 250, 440, 30, c, 5)
        else:
            rr(ctx, x, 200, 250, 530, 30, c, 5)
        ctx.set_source_rgba(0, 0, 0, 0.08); ctx.set_line_width(3)
        for r in range(1, 6):
            ctx.move_to(x + 20, 260 + r * 78); ctx.line_to(x + 230, 260 + r * 78)
        ctx.stroke()
        rr(ctx, x + 60, 300, 130, 56, 8, '#FFFFFF', 3)
        text(ctx, str(8 + k * 3), x + 125, 342, 34, '#C9184A')
    floor(ctx, 780, '#B08968', tiles=True)
    # colchões deitados (onde se senta)
    for x, n, preco in ((380, '14', 'R$ 9.000'), (1060, '20', 'R$ 15.000')):
        rr(ctx, x, 870, 520, 90, 24, '#FFFFFF', 5)
        rr(ctx, x, 860, 520, 30, 14, '#E0E7FF', 4)
        rr(ctx, x + 380, 900, 120, 44, 8, '#FFD23F', 3)
        text(ctx, n, x + 440, 934, 30, '#1B1B1E')
        rr(ctx, x + 20, 900, 150, 44, 8, '#FFFFFF', 3)
        text(ctx, preco, x + 95, 932, 24, '#C9184A')


def bg_cinema(ctx, t):
    wall(ctx, '#3C1053', 1080)
    for x in range(0, W, 120):
        ctx.rectangle(x, 0, 60, 760); ctx.set_source_rgba(0, 0, 0, 0.12); ctx.fill()
    # tela com o desenho do pinguim bombeiro
    rr(ctx, 330, 70, 1260, 560, 10, '#E0F2FF', 8)
    g = cairo.RadialGradient(960, 350, 50, 960, 350, 800)
    g.add_color_stop_rgba(0, 1, 1, 1, 0.0); g.add_color_stop_rgba(1, 0.2, 0.4, 0.8, 0.35)
    ctx.rectangle(340, 80, 1240, 540); ctx.set_source(g); ctx.fill()
    bob = 8 * math.sin(t * 3)
    ctx.save(); ctx.translate(960, 380 + bob)
    ctx.save(); ctx.scale(0.8, 1); ctx.arc(0, 0, 150, 0, TAU); ctx.restore(); fill_stroke(ctx, '#1B1B2F', 6)
    ctx.save(); ctx.translate(0, 30); ctx.scale(0.55, 0.8); ctx.arc(0, 0, 140, 0, TAU); ctx.restore(); fill_stroke(ctx, '#FFFFFF', 4)
    for dx in (-36, 36):
        ctx.arc(dx, -60, 16, 0, TAU); fill_stroke(ctx, '#FFFFFF', 3)
        ctx.arc(dx + 3, -58, 7, 0, TAU); ctx.set_source_rgba(0, 0, 0, 1); ctx.fill()
    ctx.move_to(-22, -28); ctx.line_to(22, -28); ctx.line_to(0, 0); ctx.close_path(); fill_stroke(ctx, '#F4A261', 4)
    # capacete de bombeiro
    ctx.move_to(-110, -100); ctx.curve_to(-100, -200, 100, -200, 110, -100); ctx.close_path(); fill_stroke(ctx, '#E63946', 6)
    rect(ctx, -130, -108, 260, 20, '#E63946', lw=5)
    ctx.restore()
    floor(ctx, 760, '#240046')
    # fileira de trás
    for x in range(-40, W, 190):
        rr(ctx, x, 690, 170, 150, 26, '#9D0208', 5)


def fg_cinema(ctx, t):
    for x in range(-100, W, 200):
        rr(ctx, x, 900, 180, 200, 30, '#D00000', 5)
    ctx.rectangle(0, 0, W, H); ctx.set_source_rgba(0.05, 0.0, 0.15, 0.18); ctx.fill()


def enchente(dry=False):
    def f(ctx, t):
        g = cairo.LinearGradient(0, 0, 0, 700)
        if dry:
            g.add_color_stop_rgb(0, 0.5, 0.78, 0.98); g.add_color_stop_rgb(1, 0.85, 0.94, 1)
        else:
            g.add_color_stop_rgb(0, 0.42, 0.47, 0.55); g.add_color_stop_rgb(1, 0.66, 0.7, 0.76)
        ctx.rectangle(0, 0, W, 900); ctx.set_source(g); ctx.fill()
        if dry:
            ctx.arc(1700, 140, 70, 0, TAU); ctx.set_source_rgba(1, 0.85, 0.3, 1); ctx.fill()
        else:
            for x, y, r in ((300, 110, 80), (420, 90, 100), (560, 120, 70), (1300, 100, 90), (1450, 80, 110), (1600, 110, 80)):
                ctx.arc(x, y, r, 0, TAU); ctx.set_source_rgba(0.55, 0.58, 0.64, 1); ctx.fill()
        # morro e prédio do shopping
        ctx.move_to(-50, 900); ctx.curve_to(300, 650, 1600, 650, 1970, 900); ctx.close_path()
        fill_stroke(ctx, '#6A994E' if dry else '#52734D', 5)
        rect(ctx, 360, 260, 1200, 470, '#E9D8A6', lw=6)
        rect(ctx, 360, 260, 1200, 60, '#CA6702', lw=6)
        rr(ctx, 720, 205, 480, 100, 16, '#005F73')
        text(ctx, 'SHOPPING', 960, 278, 68, '#FFFFFF', outline='#001219', lw=10)
        for k in range(5):
            window(ctx, 420 + k * 230, 360, 150, 130)
        # porta de vidro
        rect(ctx, 820, 540, 280, 190, '#94D2BD', lw=6)
        rect(ctx, 955, 540, 10, 190, '#ADB5BD', lw=2)
        rect(ctx, 300, 730, 1320, 40, '#ADB5BD', lw=5)   # calçada da entrada
        if dry:
            floor(ctx, 770, '#8D6E63')
            for x, y, w in ((200, 900, 260), (900, 980, 340), (1500, 920, 220)):
                ctx.save(); ctx.translate(x, y); ctx.scale(1, 0.25); ctx.arc(0, 0, w / 2, 0, TAU); ctx.restore()
                ctx.set_source_rgba(0.42, 0.3, 0.2, 0.8); ctx.fill()
        else:
            ctx.rectangle(0, 860, W, H - 860); setc(ctx, '#7F5539'); ctx.fill()
            ctx.set_source_rgba(0.85, 0.7, 0.5, 0.6); ctx.set_line_width(5)
            for r in range(5):
                y = 880 + r * 45
                ctx.move_to(0, y)
                for x in range(0, W + 40, 40):
                    ctx.line_to(x, y + 8 * math.sin(x / 60 + t * 2 + r))
                ctx.stroke()
            # placa meio submersa
            rect(ctx, 150, 760, 12, 140, '#6C757D', lw=3)
            rr(ctx, 70, 700, 180, 70, 8, '#2D6A4F', 4)
            text(ctx, 'RUA 7', 160, 748, 34, '#FFFFFF')
            rain(ctx, t, 0, 0, W, H, n=120, a=0.4)
    return f


def fg_barco(ctx, t):
    bob = 6 * math.sin(t * 2)
    ctx.save(); ctx.translate(1560, 960 + bob)
    ctx.move_to(-270, -120); ctx.line_to(270, -120); ctx.line_to(210, 50); ctx.line_to(-210, 50); ctx.close_path()
    fill_stroke(ctx, '#F77F00', 6)
    rect(ctx, -270, -132, 540, 22, '#FFFFFF', lw=4)
    text(ctx, 'DEFESA CIVIL', 0, -20, 46, '#FFFFFF', outline='#1B1B1E', lw=6)
    ctx.restore()
    ctx.set_source_rgba(0.85, 0.7, 0.5, 0.7); ctx.set_line_width(5)
    ctx.move_to(1280, 1012 + bob); ctx.line_to(1840, 1012 + bob); ctx.stroke()


def bg_abrigo(ctx, t):
    """ginásio da escola virado abrigo."""
    wall(ctx, '#EADBC8', 780, '#D5BDAF', 520)
    for x in range(120, W, 330):
        window(ctx, x, 70, 200, 110)
    rr(ctx, 610, 220, 700, 100, 14, '#2A9D8F')
    text(ctx, 'ABRIGO • GINÁSIO DA ESCOLA', 960, 286, 40, '#FFFFFF', outline='#14213D', lw=7)
    # tabela de basquete
    rect(ctx, 1640, 200, 180, 120, '#FFFFFF', lw=5)
    ctx.arc(1730, 340, 34, 0, math.pi); ctx.set_source_rgba(0.9, 0.35, 0.1, 1); ctx.set_line_width(6); ctx.stroke()
    # varal de roupas
    ctx.set_source_rgba(*OUT); ctx.set_line_width(3)
    ctx.move_to(60, 420); ctx.curve_to(400, 470, 800, 470, 1100, 420); ctx.stroke()
    for k, c in enumerate(('#E76F51', '#8AC926', '#1982C4', '#FFCA3A', '#6A4C93', '#FF595E')):
        x = 120 + k * 160
        y = 420 + 45 * math.sin(math.pi * (x - 60) / 1040) * 0.9
        ctx.move_to(x - 40, y); ctx.line_to(x + 40, y); ctx.line_to(x + 46, y + 110); ctx.line_to(x - 46, y + 110); ctx.close_path()
        fill_stroke(ctx, c, 4)
    floor(ctx, 780, '#C68B59')
    ctx.set_source_rgba(1, 1, 1, 0.6); ctx.set_line_width(6)
    ctx.move_to(0, 830); ctx.line_to(W, 830); ctx.stroke()
    # colchonetes no chão
    for x, y, c in ((40, 800, '#3A86FF'), (420, 800, '#FF5D8F'), (1500, 800, '#06D6A0'), (180, 1000, '#FFBE0B'), (1600, 1000, '#8338EC')):
        rr(ctx, x, y + 40, 330, 50, 12, c, 4)


BG.update({
    'shopping': (shopping(), None),
    'shopping_noite': (shopping(night=True), None),
    'praca': (bg_praca, fg_praca),
    'colchoes': (bg_colchoes, None),
    'cinema': (bg_cinema, fg_cinema),
    'enchente': (enchente(), fg_barco),
    'frente': (enchente(dry=True), None),
    'abrigo': (bg_abrigo, None),
})
SLOTS.update({
    'shopping': dict(a=(560, 1000, 0.95), b=(1000, 1000, 0.95), c=(1330, 1000, 0.95), d=(250, 1000, 0.9)),
    'praca': dict(a=(600, 980, 0.95), b=(1320, 980, 0.95), c=(1700, 1000, 0.9), d=(240, 1000, 0.9)),
    'colchoes': dict(a=(620, 950, 0.92), b=(1300, 950, 0.92), c=(1720, 1000, 0.9), d=(200, 1000, 0.9)),
    'cinema': dict(a=(760, 1000, 0.9), b=(1160, 1000, 0.9), c=(1560, 1000, 0.9)),
    'enchente': dict(a=(620, 790, 0.62), b=(960, 790, 0.62), c=(1300, 790, 0.62), barco=(1560, 990, 0.8)),
    'frente': dict(a=(330, 1010, 0.9), b=(700, 1010, 0.9), c=(1060, 1010, 0.95), d=(1400, 1010, 0.85), e=(1700, 1010, 0.9), f=(560, 840, 0.6), g=(1300, 840, 0.6)),
    'abrigo': dict(a=(620, 980, 0.92), b=(1250, 980, 0.92), c=(960, 1000, 0.9), d=(300, 1010, 0.9), e=(1650, 1010, 0.9)),
})
SLOTS['shopping_noite'] = SLOTS['shopping']


# ---------------------------------------------------------------- ep08: cozinha, rua, quermesse
def geladeira(ctx, x, y, w=240, h=440, porta=True):
    """geladeira com os pés em y (x = centro). porta=False: sem a porta de baixo (arrancada)."""
    rr(ctx, x - w / 2, y - h, w, h, 22, '#F1F3F5')
    ctx.set_source_rgba(*OUT); ctx.set_line_width(5)
    ctx.move_to(x - w / 2, y - h * 0.68); ctx.line_to(x + w / 2, y - h * 0.68); ctx.stroke()
    rect(ctx, x + w / 2 - 34, y - h * 0.92, 12, 70, '#ADB5BD', lw=3)
    if porta:
        rect(ctx, x + w / 2 - 34, y - h * 0.6, 12, 110, '#ADB5BD', lw=3)
    else:
        # interior à mostra: prateleiras, leite, ovos, pote
        rr(ctx, x - w / 2 + 14, y - h * 0.66, w - 28, h * 0.62, 10, '#CFE8F3')
        for k in range(3):
            yy = y - h * 0.66 + (k + 1) * h * 0.155
            rect(ctx, x - w / 2 + 14, yy, w - 28, 8, '#FFFFFF', lw=3)
        rect(ctx, x - w / 2 + 34, y - h * 0.66 + h * 0.155 - 70, 40, 70, '#FFFFFF', lw=3)
        ctx.arc(x + 30, y - h * 0.66 + h * 0.31 - 22, 22, 0, TAU); fill_stroke(ctx, '#E63946', 3)
        rr(ctx, x - 40, y - h * 0.66 + h * 0.465 - 46, 90, 46, 8, '#FFD166', 3)
        # dobradiças tortas
        for yy in (y - h * 0.62, y - h * 0.1):
            rect(ctx, x - w / 2 - 12, yy, 18, 28, '#868E96', lw=3)


def cozinha(porta=True):
    def f(ctx, t):
        wall(ctx, '#FDF0D5', 780)
        # azulejos
        ctx.set_source_rgba(0.55, 0.75, 0.8, 0.35); ctx.set_line_width(3)
        for x in range(0, W, 70):
            ctx.move_to(x, 380); ctx.line_to(x, 780)
        for y in range(380, 780, 70):
            ctx.move_to(0, y); ctx.line_to(W, y)
        ctx.stroke()
        window(ctx, 640, 120, 380, 230)
        # pia e armários
        rect(ctx, 80, 560, 1200, 220, '#E07A5F')
        for k in range(4):
            rect(ctx, 100 + k * 295, 590, 270, 170, '#F2CC8F', lw=4)
            ctx.arc(235 + k * 295, 640, 9, 0, TAU); fill_stroke(ctx, '#3D405B', 3)
        rect(ctx, 60, 530, 1240, 40, '#ADB5BD')
        rect(ctx, 760, 500, 14, 40, '#868E96', lw=3)
        # armário de cima
        rect(ctx, 120, 120, 420, 190, '#81B29A')
        rect(ctx, 330, 120, 4, 190, '#3D405B', lw=2)
        # filtro de barro na bancada
        rr(ctx, 1110, 400, 120, 130, 30, '#C1665A')
        rr(ctx, 1130, 360, 80, 50, 18, '#C1665A')
        geladeira(ctx, 1600, 790, porta=porta)
        floor(ctx, 780, '#B5838D', tiles=True)
    return f


def onibus_escolar(ctx, x, y, w=820, h=300, tilt=0.0, buraco=False):
    """ônibus amarelo de lado; (x, y) = centro da base das rodas."""
    ctx.save(); ctx.translate(x, y); ctx.rotate(tilt)
    rr(ctx, -w / 2, -h, w, h * 0.86, 30, '#FFC300')
    rect(ctx, -w / 2, -h * 0.42, w, h * 0.1, '#1B1B1E', lw=3)
    for k in range(6):
        rr(ctx, -w / 2 + 40 + k * (w - 120) / 6, -h * 0.9, (w - 120) / 6 - 18, h * 0.32, 8, '#BDE0FE', 4)
    rr(ctx, w / 2 - 70, -h * 0.9, 50, h * 0.6, 8, '#BDE0FE', 4)   # porta/para-brisa
    text(ctx, 'ESCOLAR', -60, -h * 0.47, 44 * w / 820, '#1B1B1E')
    for wx in (-w * 0.3, w * 0.32):
        ctx.arc(wx, -h * 0.12, h * 0.15, 0, TAU); fill_stroke(ctx, '#2B2D42', 5)
        ctx.arc(wx, -h * 0.12, h * 0.06, 0, TAU); fill_stroke(ctx, '#ADB5BD', 3)
    rect(ctx, w / 2 - 8, -h * 0.3, 22, 30, '#FFF3B0', lw=3)   # farol
    ctx.restore()


def rua(bus=False):
    def f(ctx, t):
        g = cairo.LinearGradient(0, 0, 0, 700)
        g.add_color_stop_rgb(0, 0.52, 0.8, 0.98); g.add_color_stop_rgb(1, 0.86, 0.95, 1)
        ctx.rectangle(0, 0, W, 760); ctx.set_source(g); ctx.fill()
        for x, y, r in ((300, 120, 50), (360, 105, 60), (1500, 140, 55), (1570, 125, 45)):
            ctx.arc(x, y, r, 0, TAU); ctx.set_source_rgba(1, 1, 1, 0.95); ctx.fill()
        # casinhas (ladeira)
        cols = ('#F4A261', '#2A9D8F', '#E76F51', '#8AB17D', '#E9C46A', '#A06CD5')
        for i, col in enumerate(cols):
            x0 = i * 330 - 30
            top = 300 + i * 22
            rect(ctx, x0, top, 310, 760 - top, col)
            window(ctx, x0 + 60, top + 70, 90, 80)
            rect(ctx, x0 + 190, 760 - 170, 80, 170, '#7F5539', lw=4)
        # ponto de ônibus
        rect(ctx, 1640, 520, 14, 240, '#495057', lw=3)
        rr(ctx, 1600, 470, 120, 70, 10, '#1D3557')
        text(ctx, 'PONTO', 1660, 517, 30, '#FFFFFF')
        # calçada e rua
        rect(ctx, 0, 760, W, 70, '#ADB5BD')
        rect(ctx, 0, 830, W, H - 830, '#495057', outline=False)
        ctx.set_source_rgba(1, 0.85, 0.2, 0.9)
        for i in range(0, W, 240):
            ctx.rectangle(i, 1010, 130, 14)
        ctx.fill()
        if bus:
            # buraco e ônibus atolado ao fundo
            ctx.save(); ctx.translate(1180, 905); ctx.scale(1, 0.22); ctx.arc(0, 0, 130, 0, TAU); ctx.restore()
            ctx.set_source_rgba(0.15, 0.12, 0.1, 1); ctx.fill()
            onibus_escolar(ctx, 960, 900, tilt=0.06)
    return f


def bg_quermesse(ctx, t):
    wall(ctx, '#FFF3E0', 780, '#F4D6B0', 560)
    rr(ctx, 500, 60, 920, 120, 16, '#2D6A4F')
    text(ctx, 'QUERMESSE DA PARÓQUIA', 960, 142, 58, '#FFFFFF', outline='#081C15', lw=10)
    cols = ['#E63946', '#FFB703', '#2A9D8F', '#8338EC', '#06D6A0', '#FB5607']
    for row, y0 in ((0, 230), (1, 310)):
        ctx.set_source_rgba(0.3, 0.3, 0.3, 1); ctx.set_line_width(3)
        ctx.move_to(0, y0); ctx.curve_to(640, y0 + 50, 1280, y0 + 50, 1920, y0); ctx.stroke()
        for k in range(16):
            x = 40 + k * 120 + row * 60
            y = y0 + 50 * math.sin(math.pi * x / 1920) * 0.75
            ctx.move_to(x - 28, y); ctx.line_to(x + 28, y); ctx.line_to(x, y + 50 + 3 * math.sin(t * 2 + k)); ctx.close_path()
            fill_stroke(ctx, cols[(k + row) % len(cols)], 3)
    # barraquinhas ao fundo
    for x, lab, c in ((70, 'PESCARIA', '#E63946'), (1530, 'BINGO', '#3A86FF')):
        rect(ctx, x, 470, 320, 310, '#FFFFFF', lw=5)
        for k in range(5):
            ctx.move_to(x + k * 64, 470); ctx.line_to(x + k * 64 + 32, 430); ctx.line_to(x + k * 64 + 64, 470); ctx.close_path()
            fill_stroke(ctx, c, 3)
        rr(ctx, x + 40, 500, 240, 56, 10, c, 4)
        text(ctx, lab, x + 160, 541, 34, '#FFFFFF')
    floor(ctx, 780, '#C9A27E', tiles=True)


def mesa_bolo(ctx, x, y, estado='ok', bolo=True, k=1.0):
    """mesa velha do salão com o bolo de três andares. estado: 'ok' | 'cai' (perna quebrada, k = 0..1)."""
    tilt = 0.0 if estado == 'ok' else 0.22 * k
    ctx.save(); ctx.translate(x, y)
    # pernas
    rect(ctx, -170, -230, 24, 230, '#7F5539', lw=4)
    if estado == 'ok':
        rect(ctx, 146, -230, 24, 230, '#7F5539', lw=4)
    else:
        rect(ctx, 146, -60, 24, 60, '#7F5539', lw=4)
        ctx.save(); ctx.translate(200, -10); ctx.rotate(1.2); rect(ctx, -12, -80, 24, 90, '#7F5539', lw=4); ctx.restore()
    ctx.translate(-158, -230); ctx.rotate(tilt); ctx.translate(158, 0)
    rect(ctx, -200, -26, 400, 30, '#A47148', lw=5)
    if bolo:
        ctx.translate(0, -26)
        draw_bolo3(ctx, 0, 0, 1.0)
    ctx.restore()


def draw_bolo3(ctx, x, y, s):
    """bolo de três andares com a base em (x, y)."""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.save(); ctx.scale(1, 0.22); ctx.arc(0, -10, 170, 0, TAU); ctx.restore()
    fill_stroke(ctx, '#E9ECEF', 4)
    for k, (w, h, c) in enumerate(((280, 92, '#FFFFFF'), (210, 82, '#FFC8DD'), (140, 74, '#FFFFFF'))):
        yb = -10 - sum((92, 82, 74)[:k])
        rr(ctx, -w / 2, yb - h, w, h, 14, c, 5)
        # glacê escorrendo
        ctx.set_source_rgba(1, 0.55, 0.7, 1) if c == '#FFFFFF' else ctx.set_source_rgba(1, 1, 1, 1)
        ctx.move_to(-w / 2 + 6, yb - h + 8)
        for j in range(8):
            xx = -w / 2 + 6 + (j + 0.5) * (w - 12) / 8
            ctx.line_to(xx, yb - h + 26 + 10 * (j % 2))
        ctx.line_to(w / 2 - 6, yb - h + 8); ctx.close_path(); ctx.fill()
        for j in range(5):
            ctx.arc(-w / 2 + 20 + j * (w - 40) / 4, yb - h * 0.35, 8, 0, TAU); fill_stroke(ctx, '#E63946', 3)
    # cereja no topo
    ctx.arc(0, -10 - 248 - 14, 16, 0, TAU); fill_stroke(ctx, '#C1121F', 4)
    ctx.restore()


BG.update({
    'cozinha': (cozinha(), None),
    'cozinha_sem_porta': (cozinha(porta=False), None),
    'rua': (rua(), None),
    'rua_onibus': (rua(bus=True), None),
    'quermesse': (bg_quermesse, None),
    'braco': (bg_plain('#2B1B3A', '#5A189A'), None),
})
SLOTS.update({
    'cozinha': dict(a=(420, 1010, 0.95), b=(900, 1010, 0.95), c=(1280, 1010, 0.92)),
    'rua': dict(a=(330, 1010, 0.9), b=(760, 1010, 0.95), c=(1200, 1010, 0.9), d=(1600, 1010, 0.9)),
    'quermesse': dict(a=(300, 1010, 0.9), b=(660, 1010, 0.95), c=(1000, 1010, 0.9), d=(1320, 1010, 0.9), e=(1700, 1010, 0.88)),
})
SLOTS['cozinha_sem_porta'] = SLOTS['cozinha']
SLOTS['rua_onibus'] = dict(a=(260, 1030, 0.9), b=(560, 1030, 0.95), c=(1560, 1030, 0.9), d=(1780, 1030, 0.88))
