#!/usr/bin/env python3
"""Generate assets/og-poster.png (1200x630) for the AIFF 2026 site — brand colors only, no fabricated photos."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG_TOP = (21, 21, 29)
BG_BOT = (14, 14, 19)
PAPER = (245, 241, 232)
RED = (199, 91, 75)
GOLD = (201, 169, 106)
MUTED = (178, 174, 188)

img = Image.new("RGBA", (W, H), BG_BOT + (255,))
d = ImageDraw.Draw(img)

# vertical gradient
for y in range(H):
    t = y / (H - 1)
    c = tuple(int(BG_TOP[i] * (1 - t) + BG_BOT[i] * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=c)

# glows
def glow(cx, cy, radius, color):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    steps = 60
    for i in range(steps, 0, -1):
        r = radius * i / steps
        a = int(40 * (1 - i / steps) ** 2)
        od.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, a))
    img.alpha_composite(overlay)

glow(int(W * 0.82), -80, 700, RED)
glow(40, H + 60, 620, (90, 84, 150))

# ---- film strip at bottom ----
strip_top = H - 108
d.rectangle([0, strip_top, W, H], fill=(22, 22, 30))
# sprocket holes
hole_y = strip_top + 14
for x in range(14, W, 34):
    d.ellipse([x, hole_y, x + 16, hole_y + 10], fill=BG_BOT)
# frames
fh = 54
fy = strip_top + 40
fx0, fw, gap = 14, 132, 8
hues = [258, 340, 200, 40, 285, 160, 25, 215]
for i, h in enumerate(hues):
    x = fx0 + i * (fw + gap)
    # approximate hsl -> rgb
    import colorsys
    rgb = colorsys.hls_to_rgb(h / 360, 0.34, 0.55)
    c1 = tuple(int(v * 255) for v in rgb)
    rgb2 = colorsys.hls_to_rgb(((h + 40) % 360) / 360, 0.22, 0.5)
    c2 = tuple(int(v * 255) for v in rgb2)
    d.rectangle([x, fy, x + fw, fy + fh], fill=c2)
    # fake gradient: draw lighter left-to-right band
    for k in range(fw):
        t = k / fw
        c = tuple(int(c1[j] * (1 - t) + c2[j] * t) for j in range(3))
        d.line([(x + k, fy), (x + k, fy + fh)], fill=c)
    d.rectangle([x, fy, x + fw, fy + fh], outline=(120, 118, 132), width=2)

# ---- type ----
def F(path, size, idx=0):
    return ImageFont.truetype(path, size, index=idx)

HI = "/System/Library/Fonts/Hiragino Sans GB.ttc"
HEL_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
HEL_R = "/System/Library/Fonts/Helvetica.ttc"
STHEITI = "/System/Library/Fonts/STHeiti Medium.ttc"

LX = 84
# kicker
kf = F(HI, 26, idx=2)
d.text((LX, 78), "2026 安徽文化中国行 · 开篇之作", font=kf, fill=GOLD)

# title: 2026 AI国际影展  (AI in red)
tf = F(HI, 118, idx=2)
title_cn = "国际影展"
t1 = "2026 "
d.text((LX, 118), t1, font=tf, fill=PAPER)
w1 = d.textlength(t1, font=tf)
d.text((LX + w1, 118), "AI", font=tf, fill=RED)
w2 = d.textlength("AI", font=tf)
d.text((LX + w1 + w2, 118), title_cn, font=tf, fill=PAPER)

# theme
th = F(HI, 44, idx=2)
d.text((LX, 278), "智绘未来 · 影动无界", font=th, fill=GOLD)

# latin tagline
lf = F(HEL_R, 26, idx=0)
d.text((LX, 352), "AI CHANGES CINEMA · YOUTH CREATES THE FUTURE", font=lf, fill=MUTED)

# meta
mf = F(HI, 32, idx=0)
d.text((LX, 408), "2026.11.12 – 11.15 · 合肥滨湖国际会展中心", font=mf, fill=PAPER)
# en meta small
ef = F(HEL_R, 24, idx=0)
d.text((LX, 458), "HEFEI BINHU INT'L CONVENTION & EXHIBITION CENTER", font=ef, fill=MUTED)

# bottom-right brand
bf = F(HEL_R, 24, idx=0)
d.text((W - 84 - d.textlength("AIFF 2026", font=bf), 462), "AIFF 2026", font=bf, fill=GOLD)

out = __import__("pathlib").Path(__file__).resolve().parent / "assets" / "og-poster.png"
img.convert("RGB").save(out)
print("saved", img.size, "->", out)
