#!/usr/bin/env python3
"""Render the 25 Nov 2026 news-image entry (1024x1024).

Fresh script written for this build. Layout: header, one lead story,
2x4 grid of story cards, a sport banner, an 'also today' footer strip.
All stories verified live on 25 Nov 2026 (Reuters/AFP/AP/BBC/TOI).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (11, 18, 32)
PANEL = (21, 30, 48)
PANEL2 = (27, 38, 60)
INK = (235, 238, 245)
MUTED = (168, 178, 196)
ACCENT = (255, 176, 32)   # amber
RED = (235, 87, 87)
TEAL = (64, 199, 180)
BLUE = (96, 165, 250)

FDIR = "/usr/share/fonts/truetype/dejavu/"
def font(name, size):
    return ImageFont.truetype(FDIR + name, size)

F_KICK = font("DejaVuSans-Bold.ttf", 21)
F_DATE = font("DejaVuSans-Bold.ttf", 56)
F_DAY = font("DejaVuSans.ttf", 22)
F_LEAD_TAG = font("DejaVuSans-Bold.ttf", 19)
F_LEAD_HEAD = font("DejaVuSans-Bold.ttf", 30)
F_LEAD_BODY = font("DejaVuSans.ttf", 20)
F_TAG = font("DejaVuSans-Bold.ttf", 15)
F_HEAD = font("DejaVuSans-Bold.ttf", 20)
F_BODY = font("DejaVuSans.ttf", 17)
F_SPORT = font("DejaVuSans-Bold.ttf", 20)
F_SPORT_BODY = font("DejaVuSans.ttf", 18)
F_FOOT_TAG = font("DejaVuSans-Bold.ttf", 16)
F_FOOT = font("DejaVuSans.ttf", 16)
F_SRC = font("DejaVuSans.ttf", 14)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def wrap(text, fnt, width_px):
    """Greedy word wrap to pixel width; returns list of lines."""
    lines = []
    for para in text.split("\n"):
        line = ""
        for word in para.split():
            trial = (line + " " + word).strip()
            if d.textlength(trial, font=fnt) <= width_px:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
    return lines

def draw_lines(x, y, lines, fnt, fill, leading):
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y

# ---------- header ----------
d.rectangle([0, 0, W, 108], fill=(13, 22, 40))
d.rectangle([0, 108, W, 112], fill=ACCENT)
d.text((36, 26), "THE WORLD IN ONE PAGE", font=F_KICK, fill=ACCENT)
d.text((36, 52), "25 NOVEMBER 2026", font=F_DATE, fill=INK)
day = "WEDNESDAY"
dw = d.textlength(day, font=F_DAY)
d.text((W - 36 - dw, 40), day, font=F_DAY, fill=MUTED)
d.text((W - 36 - d.textlength("make.fun — news-image-20261125", font=F_SRC),
        72), "make.fun — news-image-20261125", font=F_SRC, fill=MUTED)

# ---------- lead story ----------
LX, LY, LW, LH = 36, 132, 952, 172
d.rounded_rectangle([LX, LY, LX + LW, LY + LH], radius=14, fill=PANEL)
d.rounded_rectangle([LX, LY, LX + 10, LY + LH], radius=5, fill=RED)
d.text((LX + 28, LY + 14), "LEAD  •  MIDDLE EAST", font=F_LEAD_TAG, fill=RED)
head = "Houthis strike Riyadh's tallest tower — 11 wounded"
y = draw_lines(LX + 28, LY + 42, wrap(head, F_LEAD_HEAD, LW - 56),
               F_LEAD_HEAD, INK, 36)
body = ("Second drone strike on the PIF Tower in under a week; the Saudi-led "
        "coalition calls it a \"terrorist attack\". Houthi forces are also "
        "within 60 km of Aden.")
draw_lines(LX + 28, y + 4, wrap(body, F_LEAD_BODY, LW - 56),
           F_LEAD_BODY, MUTED, 26)

# ---------- grid of 8 cards ----------
cards = [
    ("TECH  •  US TRIAL", BLUE,
     "Huawei convicted in US trial",
     "Guilty of stealing trade secrets over its Iran business; acquitted "
     "of racketeering."),
    ("USA  •  SECURITY", RED,
     "CIA & ODNI breached",
     "Cyber breach hits US intelligence; some unclassified info "
     "compromised, Reuters reports."),
    ("UKRAINE", TEAL,
     "Zelenskiy confirms ship strike",
     "Kyiv hit a Russian cargo ship in the Gulf of Finland; ally Norway "
     "urges caution."),
    ("RUSSIA", RED,
     "Putin: retaliation 'inevitable'",
     "Moscow vows a response after Ukraine struck Russian oil plants; "
     "UN accusations traded."),
    ("FRANCE", ACCENT,
     "Sarkozy case sent to trial",
     "Ex-president and wife Carla Bruni face a corruption trial; first "
     "hearing April 2027."),
    ("USA  •  TRADE", BLUE,
     "Trump set to unveil new tariffs",
     "New duties expected after a probe into excess factory capacity, "
     "sources say."),
    ("MARKETS", TEAL,
     "Anthropic slides below IPO price",
     "Stock falls under $83, on track to shed nearly $200bn in value "
     "since listing."),
    ("SPACE", ACCENT,
     "NATO vows space defence",
     "Alliance pledges to defend orbit threats amid reports of a Russian "
     "nuclear satellite."),
]
GX, GY = 36, 316
CW, CH, GAP = 466, 116, 20
for i, (tag, color, head, body) in enumerate(cards):
    cx = GX + (i % 2) * (CW + GAP)
    cy = GY + (i // 2) * (CH + 12)
    d.rounded_rectangle([cx, cy, cx + CW, cy + CH], radius=12, fill=PANEL2)
    d.rectangle([cx, cy + 12, cx + 5, cy + CH - 12], fill=color)
    d.text((cx + 18, cy + 10), tag, font=F_TAG, fill=color)
    y = draw_lines(cx + 18, cy + 32, wrap(head, F_HEAD, CW - 36),
                   F_HEAD, INK, 24)
    draw_lines(cx + 18, y + 2, wrap(body, F_BODY, CW - 36),
               F_BODY, MUTED, 21)

# ---------- sport banner ----------
SX, SY, SW, SH = 36, 828, 952, 60
d.rounded_rectangle([SX, SY, SX + SW, SY + SH], radius=12, fill=(24, 44, 34))
d.text((SX + 20, SY + 19), "SPORT", font=F_SPORT, fill=TEAL)
sport = ("England beat Australia in the 2nd T20I to level the series  •  "
         "Sooryavanshi smashes the fastest List A double hundred")
draw_lines(SX + 118, SY + 9, wrap(sport, F_SPORT_BODY, SW - 118 - 20),
           F_SPORT_BODY, INK, 22)

# ---------- footer: also today ----------
FX, FY, FW = 36, 898, 952
d.text((FX, FY), "ALSO TODAY", font=F_FOOT_TAG, fill=ACCENT)
items = [
    "North Korea threatens to shut Switzerland's Pyongyang office over youth-camp sanctions.",
    "Iraq's PM orders federal control of Kurdish oilfields; Kurds reject the move.",
    "25 Nov is the International Day for the Elimination of Violence against Women.",
]
y = FY + 26
for it in items:
    d.text((FX, y), "•", font=F_FOOT, fill=ACCENT)
    y = draw_lines(FX + 18, y, wrap(it, F_FOOT, FW - 18), F_FOOT, MUTED, 21)
    y += 2
d.rectangle([0, 1006, W, 1024], fill=(13, 22, 40))
d.text((36, 1008), "Sources: Reuters  •  AFP  •  AP  •  BBC  •  The Times of India",
       font=F_SRC, fill=MUTED)

img.save("/home/hatch/workspace/makefun/news-image-20261125/entry.png")
print("saved entry.png", img.size)
