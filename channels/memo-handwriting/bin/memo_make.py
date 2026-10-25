#!/usr/bin/env python3
"""Memo-handwriting composite generator (Wadded Paper Message trend).

Composites: background photo + crumpled lined-note paper + handwritten
Japanese message -> 9:16 (1080x1920) or 4:5 (1080x1350) image.

Usage:
  memo_make.py --bg photo.jpg --text "スクロール|ストップして" --out out.png
  memo_make.py --bg photo.jpg --text "見て！" --ink red --ratio 4:5 --out out.png

--text: lines separated by "|". --ink: blue|red|black (default blue).
"""
import argparse
import os
import random
import sys

from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER = os.path.join(BASE, "assets", "crumpled-note.png")
FONT = os.path.join(BASE, "assets", "fonts", "Yomogi-Regular.ttf")

INKS = {
    "blue": (26, 58, 160, 255),
    "red": (200, 30, 40, 255),
    "black": (35, 35, 40, 255),
    "pink": (230, 80, 140, 255),
}

RATIOS = {"9:16": (1080, 1920), "4:5": (1080, 1350)}


def cover_resize(bg, size):
    w, h = size
    bw, bh = bg.size
    scale = max(w / bw, h / bh)
    bg = bg.resize((int(bw * scale) + 1, int(bh * scale) + 1), Image.LANCZOS)
    x = (bg.width - w) // 2
    y = (bg.height - h) // 2
    return bg.crop((x, y, x + w, y + h)).convert("RGB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bg", required=True, help="background photo path")
    ap.add_argument("--text", required=True, help='message lines, "|" separated')
    ap.add_argument("--ink", default="blue", choices=list(INKS))
    ap.add_argument("--ratio", default="9:16", choices=list(RATIOS))
    ap.add_argument("--out", required=True)
    ap.add_argument("--tilt", type=float, default=-5.0, help="paper tilt degrees")
    ap.add_argument("--paper-y", type=float, default=0.46,
                    help="paper vertical center as fraction of height")
    ap.add_argument("--paper-x", type=float, default=0.50,
                    help="paper horizontal center as fraction of width")
    ap.add_argument("--paper-w", type=float, default=0.80,
                    help="paper width as fraction of canvas width")
    ap.add_argument("--seed", type=int, default=None)
    a = ap.parse_args()
    if a.seed is not None:
        random.seed(a.seed)

    W, H = RATIOS[a.ratio]
    bg = cover_resize(Image.open(a.bg), (W, H))

    # Paper: scale to ~80% width, keep aspect
    paper = Image.open(PAPER).convert("RGBA")
    pw = int(W * a.paper_w)
    ph = int(pw * paper.height / paper.width)
    paper = paper.resize((pw, ph), Image.LANCZOS)

    # Handwritten text on the paper (before rotation, so text stays level-ish)
    lines = [l.strip() for l in a.text.split("|") if l.strip()]
    if not lines:
        sys.exit("empty --text")
    ink = INKS[a.ink]
    # auto-fit font size to paper width
    size = 110
    while size > 20:
        f = ImageFont.truetype(FONT, size)
        d = ImageDraw.Draw(paper)
        widths = [d.textlength(l, font=f) for l in lines]
        if max(widths) <= pw * 0.72:
            break
        size -= 6
    f = ImageFont.truetype(FONT, size)
    d = ImageDraw.Draw(paper)
    lh = int(size * 1.35)
    total = lh * len(lines)
    y0 = (ph - total) // 2
    for i, line in enumerate(lines):
        tw = d.textlength(line, font=f)
        x = (pw - tw) // 2 + random.randint(-6, 6)
        y = y0 + i * lh + random.randint(-4, 4)
        # slight per-line wobble for hand feel
        d.text((x, y), line, font=f, fill=ink)

    # Soft drop shadow, then tilt + paste
    tilt = a.tilt + random.uniform(-2, 2)
    paper = paper.rotate(tilt, expand=True, resample=Image.BICUBIC)
    shadow = Image.new("RGBA", paper.size, (0, 0, 0, 0))
    smask = paper.split()[3].point(lambda v: int(v * 0.35))
    shadow.putalpha(smask)
    shadow = shadow.filter(ImageFilter.GaussianBlur(28))
    # offset shadow down-right a touch
    sh = Image.new("RGBA", paper.size, (0, 0, 0, 0))
    sh.alpha_composite(shadow, (14, 22))

    cx = int(W * a.paper_x) + random.randint(-20, 20)
    cy = int(H * a.paper_y)
    px, py = cx - paper.width // 2, cy - paper.height // 2
    canvas = bg.copy().convert("RGBA")
    canvas.alpha_composite(sh, (px, py))
    canvas.alpha_composite(paper, (px, py))
    canvas.convert("RGB").save(a.out, quality=95)
    print(f"saved {a.out} ({W}x{H}) tilt={tilt:.1f} fontsize={size}")


if __name__ == "__main__":
    main()
