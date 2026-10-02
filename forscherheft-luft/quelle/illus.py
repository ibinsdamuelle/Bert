"""Aufbau-Zeichnungen und Malvorlagen für die einzelnen Versuche."""
import math
from icons import (svg, place, arrow, wave_up, bowl, glas, flasche, ballon, tuete_prall, spritze,
                   stuhl, heizung, spirale_icon, kind, uhr, taschenlampe, finger, papierkugel,
                   WATER, WATER_LINE, GLASS, WARM, COLD, INK, lufti, wolke, windrad, drachen)


def _strohhalm_im_glas(x1, y1, x2, y2, w=7):
    a = math.atan2(y2 - y1, x2 - x1)
    nx, ny = -math.sin(a) * w / 2, math.cos(a) * w / 2
    pts = [(x1 + nx, y1 + ny), (x2 + nx, y2 + ny), (x2 - nx, y2 - ny), (x1 - nx, y1 - ny)]
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"
    s = f'<path d="{d}" fill="#ffffff"/>'
    for i in range(1, 7):
        t = i / 7
        cx, cy = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        s += f'<path d="M{cx+nx:.1f} {cy+ny:.1f} L{cx-nx:.1f} {cy-ny:.1f}" stroke="#e86a6a" stroke-width="3"/>'
    s += f'<path d="{d}"/>'
    return s


def _blasen(pts):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" stroke="{WATER_LINE}" stroke-width="2"/>'
                   for x, y, r in pts)


def v1():
    s = place(tuete_prall(), 52, 2, 0.95)
    s += f'<path d="M14 86 Q14 40 50 20" stroke="{WATER_LINE}" stroke-width="2.6" stroke-dasharray="5 6"/>'
    s += arrow(40, 26, 50, 20, WATER_LINE, 2.6, 6)
    for y in (40, 56, 72):
        s += f'<path d="M126 {y} q7 -5 14 0 q7 5 14 0" stroke="{WATER_LINE}" stroke-width="2.6"/>'
    return svg(s, vb="0 0 160 100")


def v2():
    s = glas(True, 38)
    s += _strohhalm_im_glas(66, -6, 52, 84)
    s += _blasen([(47, 80, 3.2), (51, 70, 2.6), (46, 60, 3.4), (52, 50, 2.4), (48, 43, 2.8)])
    s += place(glas(True, 38), 100, 0)
    s += ('<g transform="rotate(-12 150 84)"><rect x="136" y="79" width="28" height="9" rx="3" fill="#ffffff"/></g>')
    s += _blasen([(146, 72, 2.4), (154, 64, 2), (149, 56, 2.8), (156, 48, 2.2), (147, 44, 1.8), (152, 76, 1.6)])
    return svg(s, vb="0 -8 200 104")


def glas_kopfueber(water_inside=True):
    body = "M38 12 L62 12 Q66 12 66.4 16 L72 84 L28 84 L33.6 16 Q34 12 38 12 Z"
    s = f'<path d="{body}" fill="{GLASS}" stroke="none"/>'
    if water_inside:
        s += f'<path d="M28.7 77 L71.3 77 L72 84 L28 84 Z" fill="{WATER}" stroke="none"/>'
        s += f'<path d="M29.5 77 L70.5 77" stroke="{WATER_LINE}" stroke-width="2.2"/>'
    s += ('<path d="M36 15 Q50 11 64 15 L65.5 31 Q50 37 34.5 31 Z" fill="#ffffff"/>'
          '<path d="M40 20 Q46 26 44 30 M54 18 Q52 24 58 29 M48 16 L50 22" stroke-width="1.6" stroke="#8aa3b6"/>')
    s += f'<path d="{body}"/>'
    return s


def v3():
    s = bowl(8, 46, 144, 60, wy=58)
    s += place(glas_kopfueber(), 30, 10)
    s += arrow(80, -6, 80, 16, INK, 3.2, 7)
    return svg(s, vb="0 -10 160 120")


def v4():
    s = flasche(cap=False)
    s += ('<path d="M45 22 Q41 40 44 54 Q50 62 56 54 Q59 40 55 22 Z" fill="#ff9f9f"/>'
          '<rect x="39" y="13" width="22" height="9" rx="3.5" fill="#ff9f9f"/>')
    for x1, y1, x2, y2 in ((50, 1, 50, 8), (38, 3, 42, 9), (62, 3, 58, 9)):
        s += f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{WATER_LINE}" stroke-width="2.6"/>'
    return svg(s, vb="0 -4 100 100")


def v5():
    s = place(spritze(), 14, 0)
    s += place(finger(), -4, 0)
    s += arrow(118, 80, 90, 80, INK, 3, 7)
    s += '<text x="104" y="96" font-size="11" text-anchor="middle" fill="#24323f" stroke="none">drücken</text>'
    return svg(s, vb="-6 20 128 82")


def _ballbild(cx, cy, r, ry, c):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{ry}" fill="{c}"/>'
            f'<path d="M{cx-r+1} {cy} Q{cx} {cy-ry*0.5} {cx+r-1} {cy}" stroke-width="2"/>'
            f'<path d="M{cx} {cy-ry} Q{cx-r*0.45} {cy} {cx} {cy+ry}" stroke-width="2"/>')


def v6():
    s = '<path d="M8 96 H152" stroke-width="3.4"/>'
    s += "".join(f'<path d="M{x} 96 l-6 7" stroke-width="2"/>' for x in range(16, 152, 12))
    s += f'<path d="M14 20 H146" stroke="#8aa3b6" stroke-width="2" stroke-dasharray="4 5"/>'
    s += f'<path d="M45 36 V92 M115 34 V92" stroke="#8aa3b6" stroke-width="2" stroke-dasharray="2 6"/>'
    s += _ballbild(45, 20, 15, 15, "#ffd27a")
    s += _ballbild(115, 22, 17, 12, "#a8e0b5")
    s += arrow(45, 50, 45, 66, INK, 2.6, 6) + arrow(115, 50, 115, 66, INK, 2.6, 6)
    return svg(s, vb="0 0 160 106")


def _stuehle_schnur():
    s = place(stuhl(), -6, 4, 0.8)
    s += f'<g transform="translate(206 4) scale(-0.8 0.8)">{stuhl()}</g>'
    s += '<path d="M24 14 L176 14" stroke="#b08a5a" stroke-width="2.4"/>'
    return s


def v7():
    s = _stuehle_schnur()
    s += '<rect x="74" y="10.5" width="34" height="7" rx="2" fill="#ffffff"/>'
    s += ('<ellipse cx="94" cy="34" rx="28" ry="15" fill="#ff9f9f"/>'
          '<path d="M66 34 L60 30 L60 38 Z" fill="#ff9f9f"/>'
          '<path d="M84 17.5 L84 22 M100 17.5 L100 21" stroke-width="5" stroke="#cfe3f2"/>'
          '<path d="M84 17.5 L84 22 M100 17.5 L100 21" stroke-width="1.4"/>')
    for y in (28, 34, 40):
        s += f'<path d="M54 {y} L40 {y+ (y-34)*0.6:.1f}" stroke="{WATER_LINE}" stroke-width="2.4" stroke-dasharray="4 4"/>'
    s += arrow(110, 58, 146, 58, INK, 3, 7)
    return svg(s, vb="0 0 200 76")


def v8():
    s = '<path d="M8 100 H152" stroke-width="3.4"/>'
    s += "".join(f'<path d="M{x} 100 l-6 7" stroke-width="2"/>' for x in range(16, 152, 12))
    s += '<path d="M8 20 H152" stroke="#8aa3b6" stroke-width="2" stroke-dasharray="4 5"/>'
    s += '<path d="M22 22 L58 14 L70 22 L34 30 Z" fill="#ffffff"/>'
    s += '<path d="M30 21 L56 15.5 M34 25 L60 19.5" stroke="#b9c9d6" stroke-width="1.6"/>'
    s += ('<path d="M46 34 Q64 44 46 54 Q28 64 46 74 Q64 84 48 94" stroke="#8aa3b6" stroke-width="2.2" '
          'stroke-dasharray="3 5"/>')
    s += place(papierkugel(), 92, -12, 0.6)
    s += '<path d="M122 38 V94" stroke="#8aa3b6" stroke-width="2.2" stroke-dasharray="3 5"/>'
    s += arrow(122, 70, 122, 92, "#8aa3b6", 2.2, 6)
    return svg(s, vb="0 0 160 110")


def _flasche_mit_ballon(x, y, s=0.62, balloon="schlapp", water_y=None, water=WATER):
    """Flasche (untere Kante bei y) mit Ballon oben drauf."""
    out = f'<g transform="translate({x} {y - 93*s}) scale({s})">{flasche(cap=False)}'
    if balloon == "schlapp":
        out += ('<path d="M42 19 Q30 14 20 18 Q10 24 18 30 Q28 33 42 25 Z" fill="#ff9f9f"/>'
                '<rect x="39" y="15" width="22" height="9" rx="3.5" fill="#ff9f9f"/>')
    elif balloon == "rand":
        out += '<rect x="39" y="15" width="22" height="9" rx="3.5" fill="#ff9f9f"/>'
    out += '</g>'
    if water_y is not None:
        bx0 = x + 27 * s
        bx1 = x + 73 * s
        out += (f'<rect x="{bx0:.1f}" y="{water_y}" width="{bx1-bx0:.1f}" height="{y - water_y - 0.5:.1f}" '
                f'fill="{water}" fill-opacity="0.6" stroke="none"/>')
    return out


def v9():
    s = bowl(6, 58, 88, 36, wy=66, water="#ffd9cc", line=WARM)
    s += _flasche_mit_ballon(19, 91, 0.6, "schlapp", water_y=66, water="#ffd9cc")
    s += f'<path d="M37 66 H55" stroke="{WARM}" stroke-width="2.4"/>'
    for x in (12, 86):
        s += f'<path d="M{x} 52 q-5 -6 0 -12 q5 -6 0 -12" stroke="{WARM}" stroke-width="2.8"/>'
    return svg(s, vb="0 0 100 100")


def v10():
    s = place(heizung(), 0, 22)
    for x in (22, 78):
        s += wave_up(x, 48, 30)
    s += wave_up(50, 48, 14)
    s += '<path d="M50 -4 V14" stroke-width="2"/>'
    s += place(spirale_icon(), 30, -6, 0.42)
    return svg(s, vb="0 -6 100 122")


def v11():
    s = kind("bauch")
    for i, y in enumerate((28, 34)):
        s += f'<path d="M62 {y} q5 -3 10 0 q5 3 10 0" stroke="{WATER_LINE}" stroke-width="2.4"/>'
    s += place(uhr(), 92, 26, 0.6)
    return svg(s, vb="0 4 160 94")


def v12():
    s = '<rect x="0" y="4" width="100" height="92" rx="8" fill="#e4e8ed" stroke="none"/>'
    s += taschenlampe(True)
    return svg(s, vb="0 4 100 92")


# ------------------------------------------------------------ Malvorlagen (Gerüste)

def scaff_v2():
    return svg(glas(True, 30), vb="10 4 80 92")


def scaff_v3():
    return svg(bowl(8, 30, 184, 64, wy=44), vb="0 0 200 100")


def scaff_v4():
    return svg(flasche(cap=False), vb="0 -30 100 128")


def scaff_v7():
    return svg(_stuehle_schnur(), vb="0 -16 200 92")


def scaff_v9():
    s = bowl(6, 70, 92, 34, wy=78, water="#ffd9cc", line=WARM)
    s += _flasche_mit_ballon(20, 101, 0.62, "rand", water_y=78, water="#ffd9cc")
    s += bowl(122, 70, 92, 34, wy=78, water="#d6efff", line=COLD)
    s += _flasche_mit_ballon(136, 101, 0.62, "rand", water_y=78, water="#d6efff")
    for cx, cy, r in ((134, 88, 12), (198, 86, -10)):
        s += (f'<rect x="{cx-5}" y="{cy-5}" width="10" height="10" rx="2" fill="#ffffff" '
              f'stroke="{COLD}" stroke-width="2" transform="rotate({r} {cx} {cy})"/>')
    s += (f'<text x="52" y="122" font-size="15" font-weight="700" text-anchor="middle" fill="{WARM}" stroke="none">warm</text>'
          f'<text x="168" y="122" font-size="15" font-weight="700" text-anchor="middle" fill="{COLD}" stroke="none">kalt</text>')
    return svg(s, vb="0 0 220 128")


def scaff_v10():
    return svg(heizung(), vb="0 -34 104 128")


# ------------------------------------------------------------ Deckblatt

def deckblatt():
    s = ''
    s += place(wolke(), 4, 10, 0.55)
    s += place(wolke(), 150, 0, 0.45)
    s += place(drachen(), 160, 40, 0.42, rot=14)
    s += f'<path d="M186 82 Q178 100 190 112 Q200 124 190 140" stroke-width="1.6"/>'
    for bx, by in ((190, 112), (191, 127)):
        s += (f'<path d="M{bx} {by} L{bx-8} {by-5} L{bx-8} {by+5} Z M{bx} {by} L{bx+8} {by-5} L{bx+8} {by+5} Z" '
              f'fill="#ff9f9f" stroke-width="2"/>')
    s += place(windrad(), 6, 66, 0.62)
    s += place(lufti(), 44, 22, 1.25)
    s += f'<path d="M150 104 q8 -6 16 0 q8 6 16 0" stroke="{WATER_LINE}" stroke-width="3"/>'
    s += f'<path d="M140 116 q8 -6 16 0 q8 6 16 0" stroke="{WATER_LINE}" stroke-width="3"/>'
    s += place(ballon("#ffe27a"), 34, 112, 0.5, rot=-8)
    s += place(ballon("#9ccbf0"), 56, 106, 0.56)
    s += place(ballon("#a8e0b5"), 80, 114, 0.5, rot=8)
    return svg(s, vb="0 0 210 168")


def forscherbild():
    """Kleine Szene für die Regel-Seite: zwei Forscherkinder mit Lupe und Ballon."""
    from icons import lupe as _lupe
    s = place(kind("hoch", shirt="#a8e0b5", hair="#3b2a20"), 0, 6)
    s += place(_lupe(), 64, 0, 0.45, rot=-20)
    s += place(kind("bauch", shirt="#ffd27a", hair="#c98b3a"), 110, 6)
    s += place(ballon("#9ccbf0"), 176, -4, 0.62)
    s += place(lufti(), 196, 14, 0.8)
    return svg(s, vb="0 0 280 104")
