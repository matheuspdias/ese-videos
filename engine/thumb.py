"""Thumbnail do ep01: 'só 3%..' — protagonista em choque, tia Marta com 3%, linha neon ligando os dois."""
import sys
import math
import cairo
from .chars import draw_char, Pose, TAU
from .scenes import bg_jantar, fg_jantar, text, W, H, vignette
from .render import neon_bar, heart


def neon_line(ctx, pts, glow=(1, 0.25, 0.7)):
    for lw, a in ((60, 0.06), (40, 0.1), (24, 0.18), (12, 0.6), (5, 1.0)):
        ctx.set_line_width(lw)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        if lw == 5:
            ctx.set_source_rgba(1, 0.92, 0.98, 1)
        else:
            ctx.set_source_rgba(glow[0], glow[1], glow[2], a)
        ctx.move_to(*pts[0])
        ctx.curve_to(*pts[1], *pts[2], *pts[3])
        ctx.stroke()


def main(out):
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H)
    ctx = cairo.Context(surf)
    ctx.save()
    # fundo: casa da vó, mais escuro e quente
    ctx.translate(W / 2, H / 2)
    ctx.scale(1.35, 1.35)
    ctx.translate(-W / 2, -H / 2 - 40)
    bg_jantar(ctx, 0)
    ctx.restore()
    ctx.rectangle(0, 0, W, H)
    ctx.set_source_rgba(0.1, 0.0, 0.15, 0.6)
    ctx.fill()
    # tia (direita), sorrindo
    tia = draw_char(ctx, 'tia', 1420, 1330, 1.55, Pose(mouth='grin', eyes='happy', arms='wave', facing=-1))
    # protagonista (esquerda), em choque
    voce = draw_char(ctx, 'voce', 520, 1370, 1.75, Pose(eyes='wide', mouth='o', arms='face', sweat=True, facing=1))
    # linha neon do protagonista até a tia
    hx, hy = voce['head']
    tx, ty = tia['head']
    neon_line(ctx, [(hx + 120, hy - 10), (hx + 400, hy - 260), (tx - 420, ty - 300), (tx - 150, ty - 120)])
    # barra 3%
    neon_bar(ctx, tx, tia['top'][1] - 70, 2.0, 3)
    # texto
    ctx.select_font_face('Poppins', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(190)
    w1 = ctx.text_extents('só ').x_advance
    w2 = ctx.text_extents('3%..').x_advance
    x0 = W / 2 - (w1 + w2) / 2
    text(ctx, 'só ', x0, 230, 190, '#FFFFFF', align='left', outline='#120018', lw=24)
    text(ctx, '3%..', x0 + w1, 230, 190, '#FFD23F', align='left', outline='#120018', lw=24)
    vignette(ctx, 0.45)
    surf.write_to_png(out)


if __name__ == '__main__':
    main(sys.argv[1])
