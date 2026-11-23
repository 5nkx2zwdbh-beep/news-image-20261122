#!/usr/bin/env python3
"""Draw the news-image-20261122 entry: a 1024x1024 newspaper front page
summing up Sunday 22 November 2026, with Pillow only (stdlib + PIL).

Stories are all from the verified 2026-11-23 morning briefing
(Tesla, Reuters, WSJ, Lean/Mathlib, Tabbit) plus the 22 Nov-dated
developments confirmed by same-day reporting:
- LEAD: Tesla rolls out FSD V15 — rollout began 21 Nov to
  early-access drivers, wide release due in December; Reality View
  renders a live overhead view of the road; 25x better handling of
  safety-critical cases; brain 10x bigger (1B -> 10B params). Musk
  said on 22 Nov that AI5 goes to Optimus and cars stay on AI4.
- Nvidia: SEC is reviewing its accounting; shares fell 14% in a
  day, a seventh straight down day and -23% on the week, the worst
  week since 2008; Nasdaq -5.28%, S&P 500 -3.70%.
- Anthropic IPO, day two: -8.5% to $88.91, dipping to $83.05, five
  cents above the $83 issue price; greenshoe fully used; about
  $119.5bn raised in all.
- Riemann hypothesis: Lean & Mathlib are "fully confident" the
  proof is correct — 17,000,000 lines of Lean code checked; still
  no readable paper yet.
- Also: Laos picks MiniCPM 8B as its national model; OpenAI
  proposes perplexity as the shared model yardstick; Gestalt tops
  the design chart (Elo 1931, 90% win rate); OpenRouter cuts three
  providers on 22 Nov (125 endpoints).

No story is reused as a lead from the 21 Nov edition (Riemann led
that one; here it is a bottom strip). Nothing is invented for the
picture.

Deterministic: fixed coordinates, fixed palette, DejaVu fonts, no
timestamps, no randomness. Pillow PNG output is byte-stable for the
same input image.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 244, 232)
NAVY = (22, 35, 63)
NAVY_LIGHT = (38, 58, 96)
GOLD = (217, 164, 65)
RED = (180, 35, 24)
INK = (30, 30, 30)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)
GREEN = (31, 122, 74)
BLUE = (42, 100, 180)
SKY = (126, 196, 232)
LIGHT_BLUE = (214, 232, 245)
LIGHT_GREEN = (220, 240, 228)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)
REG = lambda s: font("DejaVuSans.ttf", s)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- outer border ------------------------------------------------------
d.rectangle([8, 8, 1015, 1015], outline=NAVY, width=3)

# ---- masthead ----------------------------------------------------------
d.rectangle([16, 16, 1007, 128], fill=NAVY)
title = "THE DAY IN ONE PICTURE"
tw = d.textlength(title, font=BOLD(52))
d.text(((W - tw) / 2, 28), title, font=BOLD(52), fill=WHITE)
sub = "SUNDAY, 22 NOVEMBER 2026  \u2014  THE WORLD'S NEWS IN A SINGLE FRAME"
sw = d.textlength(sub, font=REG(21))
d.text(((W - sw) / 2, 92), sub, font=REG(21), fill=GOLD)
d.line([16, 136, 1007, 136], fill=GOLD, width=4)


def wrap(text, f, width):
    """Greedy word wrap to a pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=f) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def panel(x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=WHITE, outline=NAVY, width=2)


def kicker(x, y, text):
    d.text((x, y), text, font=BOLD(19), fill=RED)


def centred(x, y, text, f, fill):
    w = d.textlength(text, font=f)
    d.text((x - w / 2, y), text, font=f, fill=fill)


def check_row(x, y, text):
    """A green square with a hand-drawn white tick, plus a label."""
    d.rectangle([x, y, x + 24, y + 24], fill=GREEN)
    d.line([x + 5, y + 13, x + 10, y + 19, x + 20, y + 7], fill=WHITE, width=3)
    d.text((x + 36, y + 1), text, font=REG(20), fill=INK)


# ---- lead story: Tesla FSD V15 -----------------------------------------
panel(24, 148, 660, 712)
kicker(40, 164, "TESLA ROLLS OUT FSD V15")
d.text((40, 190), "FSD V15", font=BOLD(46), fill=NAVY)
d.text((40, 240), "ARRIVES WITH", font=BOLD(46), fill=NAVY)
d.text((40, 290), "REALITY VIEW", font=BOLD(46), fill=NAVY)

y = 352
for line in wrap("Rollout began 21 Nov to early-access drivers; a wide "
                 "release is due in December.", REG(20), 596):
    d.text((40, y), line, font=REG(20), fill=INK)
    y += 26

# stat box: 25x better handling of safety-critical cases
d.rectangle([40, 420, 620, 492], fill=LIGHT_BLUE, outline=BLUE, width=2)
centred(330, 430, "25x better", BOLD(28), NAVY)
centred(330, 464, "handling of safety-critical cases", REG(18), INK)

y = 512
check_row(40, y, "Brain 10x bigger: 1B \u2192 10B params")
y += 34
check_row(40, y, "Musk, 22 Nov: AI5 goes to Optimus; cars stay on AI4")
y += 44
d.line([40, y, 620, y], fill=GOLD, width=3)
y += 12
for line in wrap("Reality View renders a live overhead view of the road "
                 "\u2014 generative video, on half the compute of one AI4 "
                 "accelerator.", REG(19), 596):
    d.text((40, y), line, font=REG(19), fill=INK)
    y += 25

# ---- right column, panel A: Nvidia rout --------------------------------
panel(676, 148, 1000, 420)
kicker(692, 162, "NVIDIA \u00b7 SEC PROBE")
d.text((692, 188), "NVIDIA", font=BOLD(30), fill=NAVY)
d.text((692, 222), "SINKS 14%", font=BOLD(30), fill=NAVY)
# stat box: one day -14%, worst week since 2008
d.rectangle([692, 262, 984, 322], fill=(250, 225, 220), outline=RED, width=2)
centred(838, 272, "-14% in a day", BOLD(24), RED)
centred(838, 300, "worst week since 2008: -23%", REG(16), INK)
y = 340
for line in wrap("SEC reviews its accounting; 7th straight down day.",
                 REG(19), 292):
    d.text((692, y), line, font=REG(19), fill=INK)
    y += 25
d.text((692, 392), "Nasdaq -5.28% \u00b7 S&P 500 -3.70%", font=REG(16), fill=GREY)

# ---- right column, panel B: Anthropic IPO, day two ---------------------
panel(676, 436, 1000, 712)
kicker(692, 450, "ANTHROPIC \u00b7 DAY TWO")
d.text((692, 476), "SLIDES 8.5%", font=BOLD(30), fill=NAVY)
d.text((692, 510), "DAY TWO", font=BOLD(30), fill=NAVY)
# two chips: the low, and the total raised
d.rectangle([692, 552, 984, 596], fill=LIGHT_GREEN, outline=GREEN, width=2)
centred(838, 564, "Low $83.05 \u2014 5\u00a2 above $83", BOLD(18), NAVY)
d.rectangle([692, 606, 984, 650], fill=LIGHT_GREEN, outline=GREEN, width=2)
centred(838, 616, "$119.5bn raised in all", BOLD(20), NAVY)
y = 662
for line in wrap("Greenshoe fully used; the biggest IPO ever wobbles.",
                 REG(17), 292):
    d.text((692, y), line, font=REG(17), fill=INK)
    y += 24

# ---- bottom row, panel C: Riemann confirmed ----------------------------
panel(24, 728, 500, 960)
kicker(40, 742, "MATH")
d.text((40, 768), "RIEMANN", font=BOLD(30), fill=NAVY)
d.text((40, 802), "CONFIRMED", font=BOLD(30), fill=NAVY)
y = 850
for line in wrap("Lean & Mathlib: \u201cfully confident\u201d the proof is "
                 "correct \u2014 17,000,000 lines of Lean code checked. "
                 "Still no readable paper.", REG(19), 440):
    d.text((40, y), line, font=REG(19), fill=INK)
    y += 25
d.text((40, 930), "Four checks passed \u2014 on many cores.", font=REG(16), fill=GREY)

# ---- bottom row, panel D: also on the day -------------------------------
panel(516, 728, 1000, 960)
kicker(532, 742, "ALSO ON THE DAY")
bullets = [
    "Laos picks MiniCPM 8B as its national model.",
    "OpenAI: make perplexity the shared yardstick.",
    "Gestalt tops the design chart: Elo 1931, 90% win rate.",
    "OpenRouter cuts three providers on 22 Nov.",
]
y = 776
for b in bullets:
    d.text((532, y), "\u2022", font=BOLD(18), fill=NAVY)
    for line in wrap(b, REG(18), 420):
        d.text((556, y), line, font=REG(18), fill=INK)
        y += 23
    y += 5

# ---- footer --------------------------------------------------------------
foot = ("Drawn from the verified news of 22 Nov 2026  \u00b7  Sources: Tesla, "
        "Reuters, WSJ, Lean/Mathlib, Tabbit")
fw = d.textlength(foot, font=REG(16))
d.text(((W - fw) / 2, 976), foot, font=REG(16), fill=GREY)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
