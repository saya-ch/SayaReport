#!/usr/bin/env python3
"""
Generate a hero illustration for a job information report page.
Style: Fresh modern illustration, watercolor/flat design mix
Content: Cute cat girl character at a desk with data charts, code, laptop, trophies
Tones: Warm (coral pink, cream white, light gold, light purple accents)
Size: 1920x1080 (16:9 landscape)
"""

import math
import random
from PIL import Image, ImageDraw, ImageFilter

random.seed(42)

WIDTH = 1920
HEIGHT = 1080

def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def create_smooth_gradient(width, height, colors):
    """Create gradient using line-by-line approach"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    num_colors = len(colors)
    segment_height = height / (num_colors - 1)
    for y in range(height):
        seg = min(int(y / segment_height), num_colors - 2)
        local_t = (y - seg * segment_height) / segment_height
        color = lerp_color(colors[seg], colors[seg + 1], local_t)
        draw.line([(0, y), (width, y)], fill=color)
    return img

def draw_rounded_rect(draw, bbox, radius, fill):
    x1, y1, x2, y2 = bbox
    r = min(radius, (x2 - x1) // 2, (y2 - y1) // 2)
    draw.rectangle([x1 + r, y1, x2 - r, y2], fill=fill)
    draw.rectangle([x1, y1 + r, x2, y2 - r], fill=fill)
    draw.pieslice([x1, y1, x1 + 2*r, y1 + 2*r], 180, 270, fill=fill)
    draw.pieslice([x2 - 2*r, y1, x2, y1 + 2*r], 270, 360, fill=fill)
    draw.pieslice([x1, y2 - 2*r, x1 + 2*r, y2], 90, 180, fill=fill)
    draw.pieslice([x2 - 2*r, y2 - 2*r, x2, y2], 0, 90, fill=fill)

def draw_star(draw, cx, cy, r, color):
    points = []
    for i in range(10):
        angle = math.radians(i * 36 - 90)
        rad = r if i % 2 == 0 else r * 0.4
        px = cx + rad * math.cos(angle)
        py = cy + rad * math.sin(angle)
        points.append((px, py))
    draw.polygon(points, fill=color)

def main():
    print("Creating gradient background...")
    img = create_smooth_gradient(WIDTH, HEIGHT, [
        (255, 240, 230),
        (255, 220, 215),
        (250, 205, 215),
        (235, 195, 225),
        (215, 185, 235),
    ])
    img = img.convert('RGBA')

    # Soft circles overlay
    overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    soft_circles = [
        (300, 280, 280, (255, 180, 160, 35)),
        (1650, 200, 320, (200, 180, 255, 30)),
        (180, 750, 220, (255, 200, 180, 25)),
        (1700, 800, 260, (180, 200, 255, 25)),
        (960, 120, 200, (255, 220, 180, 20)),
        (1100, 950, 220, (220, 180, 255, 22)),
        (500, 500, 180, (255, 200, 200, 18)),
        (1400, 500, 200, (200, 180, 255, 18)),
    ]
    for cx, cy, r, color in soft_circles:
        od.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    img = Image.alpha_composite(img, overlay)

    draw = ImageDraw.Draw(img)

    # Floating stars
    star_data = [
        (180, 130, 14, (255, 220, 80, 180)),
        (380, 180, 10, (255, 180, 180, 150)),
        (1700, 130, 12, (200, 180, 255, 180)),
        (1800, 350, 9, (255, 200, 100, 130)),
        (120, 950, 11, (180, 220, 255, 150)),
        (1600, 920, 8, (255, 180, 200, 130)),
        (850, 80, 7, (200, 255, 200, 100)),
        (1200, 1000, 10, (255, 200, 255, 130)),
    ]
    star_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    sd = ImageDraw.Draw(star_overlay)
    for sx, sy, sr, sc in star_data:
        draw_star(sd, sx, sy, sr, sc)
    img = Image.alpha_composite(img, star_overlay)

    draw = ImageDraw.Draw(img)

    # Floating info cards
    card_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card_overlay)
    cards = [
        (1470, 420, 170, 100, (255, 255, 255, 160)),
        (80, 680, 150, 85, (255, 255, 255, 140)),
        (1580, 660, 140, 80, (255, 255, 255, 130)),
    ]
    for cx, cy, cw, ch, ccolor in cards:
        cd.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=14, fill=ccolor)
        for j in range(4):
            ly = cy + 15 + j * 18
            lw = random.randint(40, cw - 20)
            cd.rounded_rectangle([cx + 10, ly, cx + 10 + lw, ly + 5], radius=2, fill=(190, 180, 210, 110))
    img = Image.alpha_composite(img, card_overlay)

    draw = ImageDraw.Draw(img)

    # Desk
    desk_color = (210, 175, 145)
    desk_hl = (225, 200, 175)
    draw_rounded_rect(draw, [480, 610, 1440, 635], 8, desk_color)
    draw.rectangle([490, 613, 1430, 617], fill=desk_hl)
    draw_rounded_rect(draw, [530, 635, 565, 795], 4, (180, 150, 115))
    draw_rounded_rect(draw, [1355, 635, 1390, 795], 4, (180, 150, 115))
    draw.line([565, 730, 1355, 730], fill=(180, 150, 115), width=8)

    # Laptop on desk
    draw_rounded_rect(draw, [560, 440, 780, 585], 10, (60, 60, 80))
    draw_rounded_rect(draw, [568, 448, 772, 577], 6, (40, 50, 70))
    # Code lines on laptop screen
    code_colors = [(100, 220, 150), (100, 160, 255), (255, 220, 100), (255, 150, 180)]
    for i in range(7):
        indent = 5 if i == 0 else random.randint(5, 30)
        lw = random.randint(50, 170)
        ly = 460 + i * 16
        if ly < 575:
            draw_rounded_rect(draw, [568 + indent, ly, 568 + indent + lw, ly + 5], 2,
                               (*code_colors[i % 4], 200))
    # Keyboard
    draw_rounded_rect(draw, [545, 585, 795, 603], 5, (185, 185, 200))
    for i in range(12):
        draw_rounded_rect(draw, [550 + i * 18, 589, 560 + i * 18, 599], 2, (170, 170, 185))

    # Bar chart
    bar_chart_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    bc = ImageDraw.Draw(bar_chart_overlay)
    bc.rounded_rectangle([820, 420, 1020, 575], radius=10, fill=(255, 255, 255, 150))
    bar_colors = [(255, 150, 150), (150, 200, 255), (255, 200, 100), (180, 150, 255), (150, 230, 180)]
    for i, color in enumerate(bar_colors):
        bh = random.randint(40, 120)
        bx = 835 + i * 34
        by = 565 - bh
        bc.rounded_rectangle([bx, by, bx + 24, 565], radius=5, fill=color)
    img = Image.alpha_composite(img, bar_chart_overlay)
    draw = ImageDraw.Draw(img)

    # Pie chart
    pie_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    pd2 = ImageDraw.Draw(pie_overlay)
    pd2.rounded_rectangle([1040, 460, 1165, 585], radius=12, fill=(255, 255, 255, 150))
    pie_colors = [(255, 150, 150), (150, 200, 255), (255, 200, 100), (180, 150, 255)]
    pie_portions = [0.3, 0.25, 0.25, 0.2]
    start_angle = -90
    pie_cx, pie_cy, pie_r = 1102, 522, 48
    for color, portion in zip(pie_colors, pie_portions):
        end_angle = start_angle + portion * 360
        pd2.pieslice([pie_cx - pie_r, pie_cy - pie_r, pie_cx + pie_r, pie_cy + pie_r],
                      start_angle, end_angle, fill=color)
        start_angle = end_angle
    # Center circle (donut)
    pd2.ellipse([pie_cx - 22, pie_cy - 22, pie_cx + 22, pie_cy + 22], fill=(255, 255, 255, 200))
    img = Image.alpha_composite(img, pie_overlay)
    draw = ImageDraw.Draw(img)

    # Line chart
    line_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    ld = ImageDraw.Draw(line_overlay)
    ld.rounded_rectangle([1165, 415, 1345, 530], radius=10, fill=(255, 255, 255, 150))
    points = []
    for i in range(8):
        px = 1180 + int(i * 140 / 7)
        py = 430 + random.randint(15, 85)
        points.append((px, py))
    # Area fill
    area_points = points + [(1320, 520), (1180, 520)]
    ld.polygon(area_points, fill=(150, 130, 220, 40))
    # Line
    for i in range(len(points) - 1):
        ld.line([points[i], points[i + 1]], fill=(150, 130, 220, 200), width=3)
    # Dots
    for px, py in points:
        ld.ellipse([px - 5, py - 5, px + 5, py + 5], fill=(255, 255, 255, 220))
        ld.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(150, 130, 220, 200))
    img = Image.alpha_composite(img, line_overlay)
    draw = ImageDraw.Draw(img)

    # Desk items
    # Notebook
    draw_rounded_rect(draw, [900, 565, 980, 608], 6, (255, 150, 180, 200))
    draw_rounded_rect(draw, [905, 558, 985, 601], 6, (255, 184, 210, 200))
    # Pencil holder
    draw_rounded_rect(draw, [850, 570, 875, 610], 4, (160, 192, 255, 200))
    draw.rectangle([853, 555, 856, 585], fill=(128, 128, 128, 200))
    draw.rectangle([857, 558, 860, 585], fill=(128, 128, 128, 200))
    draw.rectangle([861, 553, 864, 585], fill=(128, 128, 128, 200))
    draw.rectangle([853, 548, 856, 558], fill=(255, 204, 100, 200))
    draw.rectangle([857, 551, 860, 558], fill=(255, 100, 100, 200))

    # Coffee mug
    draw_rounded_rect(draw, [1380, 568, 1410, 608], 5, (255, 255, 255, 200))
    draw.arc([1410, 578, 1425, 598], -30, 150, fill=(200, 200, 200, 200), width=2)
    # Steam
    for i in range(3):
        sx = 1386 + i * 8
        draw.arc([sx - 4, 530, sx + 4, 555], 200, 340, fill=(200, 200, 200, 100), width=2)

    # Cat character
    print("Drawing cat character...")
    cx, cy, hr = 420, 340, 85

    # Hair behind head
    hair_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    hd = ImageDraw.Draw(hair_overlay)
    hd.ellipse([cx - hr - 18, cy - hr - 10, cx + hr + 18, cy + hr + 5], fill=(122, 74, 40, 240))
    hd.ellipse([cx - hr - 30, cy - 5, cx - hr + 10, cy + hr + 60], fill=(122, 74, 40, 240))
    hd.ellipse([cx + hr - 10, cy - 5, cx + hr + 30, cy + hr + 60], fill=(122, 74, 40, 240))
    img = Image.alpha_composite(img, hair_overlay)
    draw = ImageDraw.Draw(img)

    # Cat ears
    # Left ear
    draw.polygon([(cx - 55, cy - hr + 10), (cx - 25, cy - hr - 55), (cx + 5, cy - hr + 15)],
                  fill=(255, 228, 196, 245))
    draw.polygon([(cx - 45, cy - hr + 15), (cx - 25, cy - hr - 35), (cx - 5, cy - hr + 18)],
                  fill=(255, 176, 176, 200))
    # Right ear
    draw.polygon([(cx + 55, cy - hr + 10), (cx + 25, cy - hr - 55), (cx - 5, cy - hr + 15)],
                  fill=(255, 228, 196, 245))
    draw.polygon([(cx + 45, cy - hr + 15), (cx + 25, cy - hr - 35), (cx + 5, cy - hr + 18)],
                  fill=(255, 176, 176, 200))

    # Head
    draw.ellipse([cx - hr, cy - hr, cx + hr, cy + hr], fill=(255, 228, 196, 245))

    # Hair bangs
    draw.ellipse([cx - hr - 5, cy - hr - 15, cx + hr + 5, cy - hr + 30], fill=(122, 74, 40, 240))
    draw.ellipse([cx - 30, cy - hr - 10, cx - 5, cy - hr + 20], fill=(122, 74, 40, 240))
    draw.ellipse([cx + 5, cy - hr - 10, cx + 30, cy - hr + 20], fill=(122, 74, 40, 240))

    # Hair highlight
    draw.ellipse([cx - 40, cy - hr + 10, cx - 25, cy - hr + 35], fill=(160, 104, 48, 180))

    # Eyes
    eye_y = cy + 10
    for dx in [-32, 32]:
        ex = cx + dx
        # Eye white
        draw.ellipse([ex - 20, eye_y - 16, ex + 20, eye_y + 16], fill=(255, 255, 255, 245))
        # Iris
        draw.ellipse([ex - 15, eye_y - 14, ex + 15, eye_y + 14], fill=(110, 61, 158, 240))
        # Pupil
        draw.ellipse([ex - 7, eye_y - 5, ex + 7, eye_y + 9], fill=(42, 16, 64, 240))
        # Highlights
        draw.ellipse([ex - 8, eye_y - 10, ex - 1, eye_y - 3], fill=(255, 255, 255, 230))
        draw.ellipse([ex + 2, eye_y + 3, ex + 6, eye_y + 7], fill=(200, 180, 255, 160))
        # Eye outline
        draw.arc([ex - 20, eye_y - 16, ex + 20, eye_y + 16], 0, 360, fill=(80, 50, 30, 200), width=2)

    # Eyelashes
    draw.line([(cx - 52, eye_y - 8), (cx - 58, eye_y - 16)], fill=(80, 50, 30, 200), width=2)
    draw.line([(cx - 12, eye_y - 14), (cx - 8, eye_y - 22)], fill=(80, 50, 30, 200), width=2)
    draw.line([(cx + 12, eye_y - 14), (cx + 8, eye_y - 22)], fill=(80, 50, 30, 200), width=2)
    draw.line([(cx + 52, eye_y - 8), (cx + 58, eye_y - 16)], fill=(80, 50, 30, 200), width=2)

    # Blush
    blush_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    bl = ImageDraw.Draw(blush_overlay)
    bl.ellipse([cx - 65, eye_y + 5, cx - 25, eye_y + 22], fill=(255, 150, 150, 65))
    bl.ellipse([cx + 25, eye_y + 5, cx + 65, eye_y + 22], fill=(255, 150, 150, 65))
    img = Image.alpha_composite(img, blush_overlay)
    draw = ImageDraw.Draw(img)

    # Nose
    draw.polygon([(cx, cy + 28), (cx - 6, cy + 36), (cx + 6, cy + 36)], fill=(255, 176, 176, 220))

    # Mouth
    draw.arc([cx - 12, cy + 36, cx, cy + 50], 0, 180, fill=(208, 128, 128, 200), width=2)
    draw.arc([cx, cy + 36, cx + 12, cy + 50], 0, 180, fill=(208, 128, 128, 200), width=2)

    # Whiskers
    for i in range(3):
        offset = (i - 1) * 10
        draw.line([(cx - 40, cy + 30 + offset), (cx - 78, cy + 24 + offset * 1.5)],
                  fill=(180, 140, 100, 150), width=2)
        draw.line([(cx + 40, cy + 30 + offset), (cx + 78, cy + 24 + offset * 1.5)],
                  fill=(180, 140, 100, 150), width=2)

    # Body (purple dress)
    body_top = cy + hr - 10
    body_bot = cy + hr + 110
    draw.polygon([
        (cx - 50, body_top),
        (cx - 90, body_bot),
        (cx + 90, body_bot),
        (cx + 50, body_top),
    ], fill=(184, 120, 208, 230))

    # Dress highlight
    draw.polygon([
        (cx - 30, body_top),
        (cx - 55, body_bot - 10),
        (cx - 10, body_bot - 10),
        (cx - 10, body_top),
    ], fill=(200, 140, 220, 60))

    # Collar
    draw.polygon([(cx - 22, body_top + 5), (cx, body_top + 35), (cx + 22, body_top + 5)],
                  fill=(255, 228, 196, 230))

    # Bow
    draw.ellipse([cx - 32, body_top + 6, cx - 4, body_top + 24], fill=(255, 140, 140, 220))
    draw.ellipse([cx + 4, body_top + 6, cx + 32, body_top + 24], fill=(255, 140, 140, 220))
    draw.ellipse([cx - 6, body_top + 10, cx + 6, body_top + 20], fill=(255, 96, 96, 220))

    # Arms
    arm_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    ad = ImageDraw.Draw(arm_overlay)
    ad.ellipse([cx - 95, body_top + 30, cx - 50, body_top + 85], fill=(255, 228, 196, 230))
    ad.ellipse([cx + 50, body_top + 25, cx + 95, body_top + 80], fill=(255, 228, 196, 230))
    # Hand
    ad.ellipse([cx + 65, body_top + 5, cx + 95, body_top + 35], fill=(255, 228, 196, 230))
    img = Image.alpha_composite(img, arm_overlay)
    draw = ImageDraw.Draw(img)

    # Floating icons
    # Trophy
    trophy_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    td = ImageDraw.Draw(trophy_overlay)
    tx, ty, ts = 1500, 210, 80
    # Cup body
    td.rounded_rectangle([tx - ts*0.3, ty - ts*0.6, tx + ts*0.3, ty + ts*0.2], radius=12, fill=(255, 200, 50, 210))
    td.ellipse([tx - ts*0.35, ty - ts*0.65, tx + ts*0.35, ty - ts*0.15], fill=(255, 230, 120, 210))
    # Handles
    td.arc([tx - ts*0.55, ty - ts*0.5, tx - ts*0.1, ty + ts*0.05], 90, 270, fill=(204, 152, 0, 210), width=6)
    td.arc([tx + ts*0.1, ty - ts*0.5, tx + ts*0.55, ty + ts*0.05], 270, 90, fill=(204, 152, 0, 210), width=6)
    # Base
    td.rounded_rectangle([tx - ts*0.08, ty + ts*0.2, tx + ts*0.08, ty + ts*0.35], radius=2, fill=(204, 152, 0, 210))
    td.rounded_rectangle([tx - ts*0.2, ty + ts*0.35, tx + ts*0.2, ty + ts*0.45], radius=4, fill=(184, 136, 0, 210))
    # Star on cup
    draw_star(td, tx, ty - ts*0.3, ts*0.12, (255, 255, 255, 150))
    img = Image.alpha_composite(img, trophy_overlay)
    draw = ImageDraw.Draw(img)

    # Second trophy (smaller)
    trophy_overlay2 = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    td2 = ImageDraw.Draw(trophy_overlay2)
    tx2, ty2, ts2 = 280, 850, 50
    td2.rounded_rectangle([tx2 - ts2*0.3, ty2 - ts2*0.6, tx2 + ts2*0.3, ty2 + ts2*0.2], radius=8, fill=(255, 200, 50, 180))
    td2.ellipse([tx2 - ts2*0.35, ty2 - ts2*0.65, tx2 + ts2*0.35, ty2 - ts2*0.15], fill=(255, 230, 120, 180))
    td2.arc([tx2 - ts2*0.5, ty2 - ts2*0.4, tx2 - ts2*0.1, ty2], 90, 270, fill=(204, 152, 0, 180), width=4)
    td2.arc([tx2 + ts2*0.1, ty2 - ts2*0.4, tx2 + ts2*0.5, ty2], 270, 90, fill=(204, 152, 0, 180), width=4)
    td2.rounded_rectangle([tx2 - ts2*0.15, ty2 + ts2*0.35, tx2 + ts2*0.15, ty2 + ts2*0.45], radius=3, fill=(184, 136, 0, 180))
    img = Image.alpha_composite(img, trophy_overlay2)
    draw = ImageDraw.Draw(img)

    # Briefcase icon
    bc_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    bcd = ImageDraw.Draw(bc_overlay)
    bx, by, bs = 1660, 360, 60
    bcd.rounded_rectangle([bx - bs*0.4, by - bs*0.25, bx + bs*0.4, by + bs*0.35], radius=8, fill=(100, 140, 200, 200))
    bcd.arc([bx - bs*0.12, by - bs*0.5, bx + bs*0.12, by - bs*0.15], 180, 360, fill=(74, 109, 160, 200), width=4)
    bcd.rounded_rectangle([bx - 4, by - 3, bx + 4, by + 5], radius=2, fill=(255, 220, 100, 200))
    # Second briefcase
    bx2, by2, bs2 = 1580, 820, 45
    bcd.rounded_rectangle([bx2 - bs2*0.4, by2 - bs2*0.25, bx2 + bs2*0.4, by2 + bs2*0.35], radius=6, fill=(100, 140, 200, 160))
    bcd.arc([bx2 - bs2*0.12, by2 - bs2*0.5, bx2 + bs2*0.12, by2 - bs2*0.15], 180, 360, fill=(74, 109, 160, 160), width=3)
    img = Image.alpha_composite(img, bc_overlay)
    draw = ImageDraw.Draw(img)

    # Code icon
    ci_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    cid = ImageDraw.Draw(ci_overlay)
    ix, iy, is_ = 220, 350, 55
    cid.line([(ix - is_*0.3, iy), (ix - is_*0.05, iy - is_*0.25)], fill=(100, 220, 150, 200), width=3)
    cid.line([(ix - is_*0.05, iy - is_*0.25), (ix - is_*0.05, iy + is_*0.25)], fill=(100, 220, 150, 200), width=3)
    cid.line([(ix - is_*0.05, iy + is_*0.25), (ix - is_*0.3, iy)], fill=(100, 220, 150, 200), width=3)
    cid.line([(ix + is_*0.3, iy), (ix + is_*0.05, iy - is_*0.25)], fill=(100, 220, 150, 200), width=3)
    cid.line([(ix + is_*0.05, iy - is_*0.25), (ix + is_*0.05, iy + is_*0.25)], fill=(100, 220, 150, 200), width=3)
    cid.line([(ix + is_*0.05, iy + is_*0.25), (ix + is_*0.3, iy)], fill=(100, 220, 150, 200), width=3)
    cid.line([(ix - is_*0.08, iy - is_*0.3), (ix + is_*0.08, iy + is_*0.3)], fill=(255, 255, 255, 180), width=3)
    img = Image.alpha_composite(img, ci_overlay)
    draw = ImageDraw.Draw(img)

    # Check marks
    check_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    ck = ImageDraw.Draw(check_overlay)
    # Check 1
    ck.ellipse([1698, 508, 1742, 552], fill=(100, 220, 150, 200))
    ck.line([(1712, 530), (1720, 540), (1734, 518)], fill=(255, 255, 255, 220), width=3)
    # Check 2
    ck.ellipse([352, 182, 388, 218], fill=(150, 200, 255, 200))
    ck.line([(364, 200), (370, 208), (382, 190)], fill=(255, 255, 255, 220), width=3)
    img = Image.alpha_composite(img, check_overlay)
    draw = ImageDraw.Draw(img)

    # Document icon
    draw_rounded_rect(draw, [1730, 250, 1770, 300], 5, (255, 255, 255, 180))
    for i in range(4):
        draw.rectangle([1738, 260 + i * 10, 1762, 264 + i * 10], fill=(176, 176, 192, 180))

    # Lightbulb icon
    lb_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    lbd = ImageDraw.Draw(lb_overlay)
    lbd.ellipse([102, 162, 138, 198], fill=(255, 220, 80, 180))
    lbd.ellipse([90, 150, 150, 210], fill=(255, 220, 80, 60))
    lbd.arc([90, 150, 150, 210], 0, 360, fill=(255, 200, 80, 120), width=2)
    img = Image.alpha_composite(img, lb_overlay)
    draw = ImageDraw.Draw(img)

    # Heart icon
    heart_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    htd = ImageDraw.Draw(heart_overlay)
    hx, hy, hs = 1750, 480, 14
    # Simple heart shape
    htd.ellipse([hx - hs*1.2, hy - hs*0.8, hx - hs*0.1, hy + hs*0.3], fill=(255, 150, 170, 120))
    htd.ellipse([hx + hs*0.1, hy - hs*0.8, hx + hs*1.2, hy + hs*0.3], fill=(255, 150, 170, 120))
    htd.polygon([(hx - hs*1.1, hy - hs*0.1), (hx, hy + hs*1.0), (hx + hs*1.1, hy - hs*0.1)],
                 fill=(255, 150, 170, 120))
    img = Image.alpha_composite(img, heart_overlay)

    # Apply watercolor effect - slight blur + blend
    print("Applying watercolor effect...")
    bg_blur = img.filter(ImageFilter.GaussianBlur(radius=1.2))
    img = Image.blend(bg_blur, img, 0.72)

    # Warm overlay
    warm = Image.new('RGBA', (WIDTH, HEIGHT), (255, 225, 205, 15))
    img = Image.alpha_composite(img, warm)

    # Vignette
    vignette = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vignette)
    for i in range(50):
        alpha = int(30 * (i / 50.0) ** 2)
        margin = int(50 * (1 - i / 50.0))
        vd.rectangle([margin, margin, WIDTH - margin, HEIGHT - margin],
                      outline=(40, 20, 20, alpha), width=3)
    img = Image.alpha_composite(img, vignette)

    # Convert to RGB
    final = img.convert('RGB')

    output_path = '/workspace/SayaReport/assets/hero-illustration.png'
    final.save(output_path, 'PNG', quality=95)
    print(f"\nImage saved to: {output_path}")
    print(f"Size: {final.size[0]}x{final.size[1]}")
    print("Done!")

if __name__ == '__main__':
    main()
