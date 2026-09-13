#!/usr/bin/env python3
"""Render the committed trajectory CSV as a grayscale PNG for the paper."""

import csv
from collections import defaultdict
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader((ROOT / "results/trajectories.csv").open(encoding="utf-8")))
series = defaultdict(list)
for row in rows:
    if row["model"] == "endogenous":
        series[row["scenario"]].append(row)

W, H = 1600, 1000
image = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(image)
font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
bold_path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
font = ImageFont.truetype(font_path, 22)
small = ImageFont.truetype(font_path, 17)
title = ImageFont.truetype(bold_path, 30)
colors = {"unconditional_protection": 15, "conditional_support": 80,
          "open_exposure": 145, "sequenced_transition": 205}
labels = {"unconditional_protection": "Unconditional protection",
          "conditional_support": "Conditional support", "open_exposure": "Open exposure",
          "sequenced_transition": "Sequenced transition"}
draw.text((W / 2, 24), "Endogenous-capability trajectories", fill="black", font=title, anchor="ma")

for panel, (metric, label) in enumerate((("protection_share", "Protection-seeking share"), ("capability", "Capability stock"))):
    left, right = 160, 1500
    top = 95 + panel * 390
    bottom = top + 305
    draw.text((left, top - 34), label, fill="black", font=font, anchor="la")
    for tick in range(6):
        value = tick / 5
        y = bottom - value * (bottom - top)
        draw.line((left, y, right, y), fill=(220, 220, 220), width=1)
        draw.text((left - 15, y), f"{value:.1f}", fill="black", font=small, anchor="rm")
    draw.line((left, top, left, bottom), fill="black", width=2)
    draw.line((left, bottom, right, bottom), fill="black", width=2)
    for name, values in series.items():
        pts = []
        for row in values:
            x = left + int(row["step"]) / 120 * (right - left)
            y = bottom - float(row[metric]) * (bottom - top)
            pts.append((x, y))
        shade = colors[name]
        draw.line(pts, fill=(shade, shade, shade), width=5)

legend_y = 925
for idx, name in enumerate(labels):
    x = 130 + idx * 365
    shade = colors[name]
    draw.line((x, legend_y, x + 55, legend_y), fill=(shade, shade, shade), width=6)
    draw.text((x + 68, legend_y), labels[name], fill="black", font=small, anchor="lm")
image.save(ROOT / "results/trajectories.png", dpi=(180, 180))
