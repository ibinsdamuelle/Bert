"""Einfache Strichzeichnungen (SVG) für das Forscherheft „Luft“.

Alle Symbole sind in einem 100x100-Raster gezeichnet und werden mit
svg(...) in ein <svg>-Element verpackt. Flächen sind hell gehalten,
damit die Seiten auch als Schwarz-Weiß-Kopie gut aussehen und die
Kinder sie anmalen können.
"""
import math

INK = "#24323f"
WATER = "#cfe9f8"
WATER_LINE = "#4f9fd3"
GLASS = "#f3fafe"
SKIN = "#ffe0c2"
WARM = "#e8643c"
COLD = "#3d8fd1"


def svg(inner, vb="0 0 100 100", cls="ic", style="", sw=3.2):
    st = f' style="{style}"' if style else ""
    return (
        f'<svg class="{cls}" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg"{st}>'
        f'<g fill="none" stroke="{INK}" stroke-width="{sw}" '
        f'stroke-linecap="round" stroke-linejoin="round">{inner}</g></svg>'
    )


def place(inner, x=0, y=0, s=1.0, rot=0):
    t = f"translate({x} {y})"
    if s != 1:
        t += f" scale({s})"
    if rot:
        t += f" rotate({rot} 50 50)"
    return f'<g transform="{t}">{inner}</g>'


def arrow(x1, y1, x2, y2, color=INK, w=3.2, head=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45))
    p2 = (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))
    return (
        f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" stroke="{color}" stroke-width="{w}"/>'
        f'<path d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}" '
        f'stroke="{color}" stroke-width="{w}"/>'
    )


def wave_up(x, y, h=24, color=WARM, w=2.6):
    """Gewellte Linie nach oben mit Pfeilspitze (aufsteigende warme Luft)."""
    d = f"M{x} {y} q-4 {-h/4} 0 {-h/2} q4 {-h/4} 0 {-h/2}"
    return (
        f'<path d="{d}" stroke="{color}" stroke-width="{w}"/>'
        f'<path d="M{x-3.5} {y-h+5} L{x} {y-h} L{x+3.5} {y-h+5}" stroke="{color}" stroke-width="{w}"/>'
    )


# ------------------------------------------------------------------ Grundformen

def bowl(x, y, w, h, wy=None, water=WATER, fill="#ffffff", line=WATER_LINE, rim=True):
    """Schüssel; wy = Höhe der Wasseroberfläche (absolut)."""
    P0 = (x + w, y)
    P1 = (x + w, y + h)
    P2 = (x + w / 2, y + h)
    out = (f'<path d="M{x} {y} L{x+w} {y} Q{x+w} {y+h} {x+w/2} {y+h} '
           f'Q{x} {y+h} {x} {y} Z" fill="{fill}" stroke="none"/>')
    if wy is not None:
        t = 1 - math.sqrt(max(0.0, 1 - (wy - y) / h))
        xr = x + w - t * t * w / 2
        xl = x + t * t * w / 2
        q1 = ((1 - t) * P1[0] + t * P2[0], (1 - t) * P1[1] + t * P2[1])
        q1m = (2 * (x + w / 2) - q1[0], q1[1])
        out += (f'<path d="M{xl:.1f} {wy} L{xr:.1f} {wy} Q{q1[0]:.1f} {q1[1]:.1f} {P2[0]:.1f} {P2[1]:.1f} '
                f'Q{q1m[0]:.1f} {q1m[1]:.1f} {xl:.1f} {wy} Z" fill="{water}" stroke="none"/>')
        out += f'<path d="M{xl+2:.1f} {wy} L{xr-2:.1f} {wy}" stroke="{line}" stroke-width="2.4"/>'
    out += f'<path d="M{x+w} {y} Q{x+w} {y+h} {x+w/2} {y+h} Q{x} {y+h} {x} {y}"/>'
    if rim:
        out += f'<path d="M{x-4} {y} L{x+w+4} {y}" stroke-width="4"/>'
    else:
        out += f'<path d="M{x} {y} L{x+w} {y}"/>'
    return out


def glas(water=True, wl=42):
    body = "M28 16 L72 16 L66 88 Q66 92 62 92 L38 92 Q34 92 34 88 Z"
    s = f'<path d="{body}" fill="{GLASS}" stroke="none"/>'
    if water:
        xl = 28 + (wl - 16) * (6 / 72)
        xr = 100 - xl
        s += (f'<path d="M{xl:.1f} {wl} L{xr:.1f} {wl} L66 88 Q66 92 62 92 L38 92 '
              f'Q34 92 34 88 Z" fill="{WATER}" stroke="none"/>')
        s += f'<path d="M{xl+1.5:.1f} {wl} L{xr-1.5:.1f} {wl}" stroke="{WATER_LINE}" stroke-width="2.4"/>'
    s += '<path d="M35 24 L38.5 80" stroke="#ffffff" stroke-width="3.5"/>'
    s += f'<path d="{body}"/>'
    return s


def flasche(cap=True, fill="#e9f6ee"):
    body = ("M42 26 Q28 32 27 46 L27 86 Q27 93 34 93 L66 93 Q73 93 73 86 L73 46 "
            "Q72 32 58 26 L58 18 L42 18 Z")
    s = f'<path d="{body}" fill="{fill}" stroke="none"/>'
    s += '<path d="M27 60 H73 M27 67 H73" stroke="#8cbfa0" stroke-width="2"/>'
    s += '<path d="M33 46 L33 84" stroke="#ffffff" stroke-width="3.5"/>'
    s += f'<path d="{body}"/>'
    s += '<path d="M40 22 H60" stroke-width="3"/>'
    if cap:
        s += '<rect x="40" y="8" width="20" height="11" rx="2" fill="#7fbde8"/>'
    return s


def ballon(c="#ff9f9f"):
    return (
        f'<ellipse cx="50" cy="38" rx="25" ry="29" fill="{c}"/>'
        f'<path d="M45 72 L55 72 L50 66.5 Z" fill="{c}"/>'
        '<path d="M50 72 Q44 82 51 89 Q57 95 50 99" stroke-width="2.4"/>'
        '<path d="M35 30 Q37 19 47 15" stroke="#ffffff" stroke-width="4"/>'
    )


def strohhalm(c="#e86a6a"):
    stripes = "".join(f"M44 {y} L56 {y-6} " for y in range(22, 92, 13))
    return (
        '<g transform="rotate(20 50 50)">'
        '<rect x="44" y="8" width="12" height="84" rx="3" fill="#ffffff" stroke="none"/>'
        f'<path d="{stripes}" stroke="{c}" stroke-width="4" stroke-linecap="butt"/>'
        '<rect x="44" y="8" width="12" height="84" rx="3"/>'
        '</g>'
    )


def kreide():
    return ('<g transform="rotate(-15 50 50)">'
            '<rect x="16" y="40" width="68" height="20" rx="6" fill="#ffffff"/>'
            '<path d="M28 41 V59" stroke-width="2"/></g>')


def schwamm():
    pores = "".join(f'<circle cx="{cx}" cy="{cy}" r="2.3" fill="#d9ad2e" stroke="none"/>'
                    for cx, cy in [(28, 52), (40, 60), (54, 51), (66, 62), (73, 50), (34, 65), (48, 66), (60, 56)])
    return ('<rect x="18" y="42" width="64" height="30" rx="4" fill="#ffe27a" stroke="none"/>'
            + pores +
            '<rect x="18" y="30" width="64" height="12" rx="3" fill="#8fd19e"/>'
            '<rect x="18" y="42" width="64" height="30" rx="4"/>')


def radiergummi():
    return ('<g transform="rotate(-12 50 50)">'
            '<rect x="20" y="36" width="60" height="28" rx="5" fill="#ffc2d1" stroke="none"/>'
            '<path d="M46 36 H75 Q80 36 80 41 V59 Q80 64 75 64 H46 Z" fill="#9ccbf0" stroke="none"/>'
            '<rect x="20" y="36" width="60" height="28" rx="5"/><path d="M46 36 V64"/></g>')


def tuete():
    return ('<path d="M26 20 L74 20 L78 88 Q78 92 74 92 L26 92 Q22 92 22 88 Z" fill="#f2f8fc"/>'
            '<path d="M27 30 L73 30" stroke="#4f9fd3" stroke-width="3"/>'
            '<path d="M31 40 L33 82" stroke="#d5e7f3" stroke-width="3"/>')


def tuete_prall():
    return ('<path d="M44 30 C 16 32, 10 58, 17 76 C 24 94, 76 94, 83 76 C 90 58, 84 32, 56 30 Z" fill="#f2f8fc"/>'
            '<path d="M44 30 L46 22 L54 22 L56 30" fill="#f2f8fc"/>'
            '<path d="M46 22 L38 9 L62 9 L54 22" fill="#f2f8fc"/>'
            '<path d="M46 25 L54 23 M46 23 L54 25" stroke-width="2"/>'
            '<path d="M28 52 Q30 42 38 38" stroke="#ffffff" stroke-width="4"/>')


def spritze(piston=58):
    return ('<rect x="22" y="38" width="48" height="24" rx="2" fill="#ffffff" stroke="none"/>'
            f'<rect x="{piston}" y="39.5" width="6" height="21" fill="#7d8e9c" stroke="none"/>'
            f'<path d="M{piston+6} 50 H92" stroke-width="4"/>'
            '<rect x="22" y="38" width="48" height="24" rx="2"/>'
            '<path d="M22 45 L12 47.5 L12 52.5 L22 55" fill="#ffffff"/>'
            '<rect x="68" y="31" width="5" height="38" rx="1.5" fill="#dfe8ef"/>'
            '<rect x="90" y="38" width="6" height="24" rx="2" fill="#c9d6e2"/>'
            '<path d="M30 38 v6 M38 38 v4 M46 38 v6 M54 38 v4" stroke-width="2"/>')


def ball(c="#ffd27a", squash=1.0):
    ry = 32 * squash
    rx = 32 if squash == 1 else 36
    cy = 84 - ry
    return (f'<ellipse cx="50" cy="{cy}" rx="{rx}" ry="{ry:.1f}" fill="{c}"/>'
            f'<path d="M19 {cy} Q50 {cy-ry*0.5:.1f} 81 {cy}" stroke-width="2.4"/>'
            f'<path d="M50 {cy-ry:.1f} Q36 {cy} 50 {cy+ry:.1f}" stroke-width="2.4"/>')


def schnur():
    return ('<circle cx="44" cy="54" r="24" fill="#f0dcc0"/>'
            '<path d="M24 44 Q44 36 64 48 M21 56 Q44 46 67 60 M28 68 Q46 58 62 71" stroke-width="2"/>'
            '<path d="M66 62 Q80 66 78 80 Q76 92 92 90" stroke-width="2.4"/>')


def klebeband():
    return ('<path d="M66 62 L88 76 L82 86 L60 72" fill="#e3eef6"/>'
            '<circle cx="46" cy="50" r="26" fill="#e3eef6"/>'
            '<circle cx="46" cy="50" r="12" fill="#ffffff"/>')


def stuhl():
    return ('<rect x="28" y="10" width="9" height="50" rx="2" fill="#e2c49a"/>'
            '<rect x="28" y="52" width="46" height="9" rx="2" fill="#e2c49a"/>'
            '<path d="M33 61 V92 M69 61 V92" stroke-width="4.5"/>')


def papier():
    return ('<path d="M26 12 L64 12 L78 26 L78 90 L26 90 Z" fill="#ffffff"/>'
            '<path d="M64 12 L64 26 L78 26"/>'
            '<path d="M34 42 H70 M34 52 H70 M34 62 H70 M34 72 H58" stroke-width="2" stroke="#b9c9d6"/>')


def papierkugel():
    return ('<path d="M50 20 L66 26 L78 40 L80 58 L70 74 L52 82 L34 76 L22 62 L20 44 L32 28 Z" fill="#ffffff"/>'
            '<path d="M32 28 L48 44 L66 26 M48 44 L50 60 L70 74 M50 60 L34 76 M48 44 L20 44 '
            'M50 60 L80 58 M48 44 L78 40" stroke-width="1.8" stroke="#8aa3b6"/>')


def schuessel(kind="wasser"):
    if kind == "warm":
        s = bowl(8, 44, 84, 42, wy=54, water="#ffd9cc", line=WARM)
        for x in (32, 50, 68):
            s += (f'<path d="M{x} 36 q-5 -6 0 -12 q5 -6 0 -12" stroke="{WARM}" stroke-width="2.8"/>')
        return s
    if kind == "kalt":
        s = bowl(8, 44, 84, 42, wy=54, water="#d6efff", line=COLD)
        for cx, cy, r in ((30, 60, 12), (52, 64, -8), (70, 59, 18)):
            s += (f'<rect x="{cx-7}" y="{cy-7}" width="14" height="14" rx="2.5" fill="#ffffff" '
                  f'stroke="{COLD}" stroke-width="2.4" transform="rotate({r} {cx} {cy})"/>')
        return s
    return bowl(8, 44, 84, 42, wy=54)


def schere():
    return ('<path d="M38 62 L60 10 L64 13 L45 64 Z" fill="#dfe8ef"/>'
            '<path d="M62 62 L40 10 L36 13 L55 64 Z" fill="#dfe8ef"/>'
            '<circle cx="34" cy="74" r="12" fill="#ffd27a"/><circle cx="34" cy="74" r="5" fill="#ffffff"/>'
            '<circle cx="66" cy="74" r="12" fill="#ffd27a"/><circle cx="66" cy="74" r="5" fill="#ffffff"/>'
            '<circle cx="50" cy="40" r="2.6" fill="#24323f" stroke="none"/>')


def faden():
    return ('<rect x="38" y="26" width="24" height="48" fill="#ff9f9f" stroke="none"/>'
            '<path d="M38 34 H62 M38 42 H62 M38 50 H62 M38 58 H62 M38 66 H62" stroke-width="1.6" stroke="#cf5f5f"/>'
            '<rect x="38" y="26" width="24" height="48"/>'
            '<rect x="32" y="18" width="36" height="8" rx="2" fill="#e2c49a"/>'
            '<rect x="32" y="74" width="36" height="8" rx="2" fill="#e2c49a"/>'
            '<path d="M62 60 Q82 64 84 80 Q86 94 72 94" stroke-width="2"/>')


def heizung():
    fins = "".join(f'<rect x="{x}" y="30" width="9" height="54" rx="4" fill="#eef1f4"/>' for x in range(12, 88, 10))
    return (fins +
            '<path d="M10 40 H90 M10 76 H90" stroke-width="2.4"/>'
            '<path d="M16 84 V92 M84 84 V92" stroke-width="4"/>'
            '<circle cx="95" cy="40" r="4" fill="#ffffff"/>')


def spirale_icon():
    pts = []
    for i in range(0, 260):
        th = i * 0.08
        r = 4 + 2.6 * th
        if r > 40:
            break
        pts.append((50 + r * math.cos(th), 50 + r * math.sin(th)))
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    return (f'<path d="{d}" stroke-width="2.6"/>'
            '<circle cx="50" cy="50" r="5" fill="#a8e0b5"/>'
            '<circle cx="51.5" cy="48.5" r="1.2" fill="#24323f" stroke="none"/>')


def uhr():
    ticks = "".join(
        f'<path d="M{50+26*math.cos(a):.1f} {56+26*math.sin(a):.1f} L{50+30*math.cos(a):.1f} {56+30*math.sin(a):.1f}" stroke-width="2"/>'
        for a in [i * math.pi / 6 for i in range(12)])
    return ('<rect x="43" y="10" width="14" height="9" rx="2" fill="#c9d6e2"/>'
            '<path d="M50 19 V24" stroke-width="4"/>'
            '<path d="M74 30 L80 24" stroke-width="5"/>'
            '<circle cx="50" cy="56" r="33" fill="#ffffff"/>' + ticks +
            '<path d="M50 56 L50 33" stroke-width="3.6"/>'
            f'<path d="M50 56 L65 63" stroke="{WARM}" stroke-width="3"/>'
            '<circle cx="50" cy="56" r="3" fill="#24323f" stroke="none"/>')


def taschenlampe(dust=True):
    s = '<path d="M38 42 L98 12 L98 88 L38 58 Z" fill="#fff6c2" stroke="none"/>'
    if dust:
        import random
        rnd = random.Random(7)
        for _ in range(26):
            x = rnd.uniform(46, 96)
            spread = (x - 38) / 60 * 36 + 8
            y = 50 + rnd.uniform(-spread, spread) * 0.95
            r = rnd.choice([1.1, 1.4, 1.8])
            s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#8a96a3" stroke="none"/>'
    s += ('<rect x="4" y="41" width="26" height="18" rx="3" fill="#7fbde8"/>'
          '<path d="M30 38 L40 34 L40 66 L30 62 Z" fill="#7fbde8"/>'
          '<rect x="12" y="45" width="8" height="5" rx="1.5" fill="#ffffff"/>')
    return s


def kind(arm="bauch", shirt="#9ccbf0", hair="#8a5a3b"):
    s = (f'<path d="M34 46 Q50 40 66 46 L69 76 L31 76 Z" fill="{shirt}"/>'
         '<path d="M42 76 V95 M58 76 V95" stroke-width="5"/>'
         f'<circle cx="50" cy="25" r="14" fill="{SKIN}"/>'
         f'<path d="M36 23 Q37 9 50 10 Q63 9 64 23 Q58 15 50 17 Q42 15 36 23 Z" fill="{hair}"/>'
         '<circle cx="45" cy="25" r="1.7" fill="#24323f" stroke="none"/>'
         '<circle cx="55" cy="25" r="1.7" fill="#24323f" stroke="none"/>'
         '<path d="M45 31 Q50 35 55 31" stroke-width="2"/>')
    if arm == "bauch":
        s += (f'<path d="M36 50 Q28 64 42 64 L52 63" stroke="{INK}" stroke-width="7.5"/>'
              f'<path d="M36 50 Q28 64 42 64 L52 63" stroke="{SKIN}" stroke-width="4.5"/>'
              f'<path d="M64 50 Q72 62 70 74" stroke="{INK}" stroke-width="7.5"/>'
              f'<path d="M64 50 Q72 62 70 74" stroke="{SKIN}" stroke-width="4.5"/>')
    elif arm == "hoch":
        s += (f'<path d="M36 50 Q24 40 22 26" stroke="{INK}" stroke-width="7.5"/>'
              f'<path d="M36 50 Q24 40 22 26" stroke="{SKIN}" stroke-width="4.5"/>'
              f'<path d="M64 50 Q76 40 78 26" stroke="{INK}" stroke-width="7.5"/>'
              f'<path d="M64 50 Q76 40 78 26" stroke="{SKIN}" stroke-width="4.5"/>')
    return s


def muenze():
    return ('<circle cx="50" cy="50" r="30" fill="#f6d77a"/>'
            '<circle cx="50" cy="50" r="22" fill="#e9eef2"/>'
            '<text x="50" y="59" font-size="26" font-weight="700" text-anchor="middle" fill="#24323f" stroke="none">1</text>')


def lupe():
    return ('<path d="M60 60 L84 84" stroke-width="9"/>'
            '<circle cx="42" cy="42" r="25" fill="#e8f4fc"/>'
            '<path d="M30 34 Q33 26 41 24" stroke="#ffffff" stroke-width="4"/>')


def gluehbirne():
    return ('<path d="M50 14 C 31 14, 23 33, 31 47 C 35 54, 39 58, 39 66 L61 66 C 61 58, 65 54, 69 47 C 77 33, 69 14, 50 14 Z" fill="#fff1a8"/>'
            '<path d="M40 72 H60 M42 79 H58 M45 86 H55" stroke-width="3.4"/>'
            '<path d="M44 62 L44 48 L50 54 L56 48 L56 62" stroke-width="2" stroke="#d99a1e"/>'
            '<path d="M50 3 V7 M18 18 L22 21 M82 18 L78 21 M8 44 H13 M87 44 H92" stroke="#e8a92b" stroke-width="3"/>')


def denkblase(fill="#fff2e2", color="#e07b22"):
    return (f'<path d="M24 52 C 10 50, 11 30, 26 29 C 28 15, 47 11, 55 21 C 65 11, 85 17, 83 33 '
            f'C 95 37, 93 57, 79 57 C 75 67, 57 67, 51 61 C 41 69, 25 65, 24 52 Z" fill="{fill}"/>'
            f'<circle cx="24" cy="75" r="6" fill="{fill}"/><circle cx="14" cy="89" r="4" fill="{fill}"/>'
            f'<text x="53" y="51" font-size="30" font-weight="700" text-anchor="middle" fill="{color}" stroke="none">?</text>')


def frage():
    return ('<circle cx="50" cy="50" r="40" fill="#e3f1fb"/>'
            '<text x="50" y="66" font-size="48" font-weight="700" text-anchor="middle" fill="#1f6fae" stroke="none">?</text>')


def kolben():
    outline = "M41 10 H59 M44 10 V38 L21 82 Q18 90 27 90 H73 Q82 90 79 82 L56 38 V10"
    return ('<path d="M44 10 V38 L21 82 Q18 90 27 90 H73 Q82 90 79 82 L56 38 V10 Z" fill="#ffffff" stroke="none"/>'
            '<path d="M31.5 62 H68.5 L79 82 Q82 90 73 90 H27 Q18 90 21 82 Z" fill="#a8e0b5" stroke="none"/>'
            '<circle cx="44" cy="74" r="3" fill="#ffffff" stroke="none"/><circle cx="56" cy="80" r="2.4" fill="#ffffff" stroke="none"/>'
            '<circle cx="52" cy="70" r="1.8" fill="#ffffff" stroke="none"/>'
            f'<path d="{outline}"/>')


def kiste():
    return ('<ellipse cx="34" cy="30" rx="11" ry="13" fill="#ff9f9f"/>'
            '<path d="M34 43 Q31 48 35 52" stroke-width="2"/>'
            '<rect x="52" y="12" width="9" height="36" rx="2" fill="#ffffff" transform="rotate(12 56 30)"/>'
            '<rect x="66" y="26" width="16" height="22" rx="3" fill="#e9f6ee"/>'
            '<path d="M12 44 H88 L81 90 H19 Z" fill="#f3dcb8"/>'
            '<path d="M16 56 H84" stroke-width="2"/>')


def stern(fill="#ffffff", sw=None):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        r = 44 if i % 2 == 0 else 19
        pts.append(f"{50 + r * math.cos(a):.1f},{54 + r * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'


def smiley(kind="gut"):
    s = '<circle cx="50" cy="50" r="40" fill="#ffffff"/>'
    s += '<circle cx="36" cy="40" r="4.5" fill="#24323f" stroke="none"/><circle cx="64" cy="40" r="4.5" fill="#24323f" stroke="none"/>'
    if kind == "gut":
        s += '<path d="M30 58 Q50 80 70 58" stroke-width="4"/>'
    elif kind == "mittel":
        s += '<path d="M33 63 Q50 70 67 63" stroke-width="4"/>'
    else:
        s += '<path d="M33 66 Q42 60 50 65 Q58 70 67 64" stroke-width="4"/>'
    return s


def lufti(mood="froh", fill="#dff0fb"):
    circles = [(28, 60, 19), (48, 44, 24), (70, 52, 20), (52, 66, 20), (36, 70, 14), (68, 68, 15)]
    out = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="#24323f" stroke-width="6.4"/>' for x, y, r in circles)
    out += ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="none"/>' for x, y, r in circles)
    out += ('<ellipse cx="41" cy="54" rx="3.6" ry="4.6" fill="#24323f" stroke="none"/>'
            '<ellipse cx="59" cy="54" rx="3.6" ry="4.6" fill="#24323f" stroke="none"/>'
            '<circle cx="42.2" cy="52.4" r="1.2" fill="#ffffff" stroke="none"/>'
            '<circle cx="60.2" cy="52.4" r="1.2" fill="#ffffff" stroke="none"/>'
            '<circle cx="33" cy="63" r="4.2" fill="#ffb8b8" stroke="none"/>'
            '<circle cx="67" cy="63" r="4.2" fill="#ffb8b8" stroke="none"/>')
    if mood == "staunen":
        out += '<ellipse cx="50" cy="66" rx="4" ry="5" fill="#24323f" stroke="none"/>'
    else:
        out += '<path d="M42 63 Q50 71 58 63" stroke-width="3"/>'
    return out


def wolke(fill="#ffffff"):
    circles = [(30, 58, 16), (48, 46, 21), (68, 54, 17), (50, 62, 16)]
    out = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="#24323f" stroke-width="6"/>' for x, y, r in circles)
    out += ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="none"/>' for x, y, r in circles)
    return out


def windrad():
    cols = ["#ff9f9f", "#ffe27a", "#9ccbf0", "#a8e0b5"]
    s = '<path d="M50 50 L50 98" stroke-width="4"/>'
    for i, c in enumerate(cols):
        s += (f'<path d="M50 50 L50 14 Q66 22 50 50 Z" fill="{c}" transform="rotate({i*90} 50 50)"/>')
    s += '<circle cx="50" cy="50" r="3.5" fill="#24323f" stroke="none"/>'
    return s


def drachen():
    return ('<path d="M50 6 L80 40 L50 92 L20 40 Z" fill="#ffe27a"/>'
            '<path d="M50 6 L50 92 M20 40 L80 40" stroke-width="2.2"/>'
            '<path d="M50 6 L80 40 L50 40 Z" fill="#ff9f9f"/>'
            '<path d="M50 40 L50 92 L20 40 Z" fill="#9ccbf0"/>')


def fahrrad():
    return ('<circle cx="24" cy="64" r="16" fill="#ffffff"/><circle cx="76" cy="64" r="16" fill="#ffffff"/>'
            '<path d="M24 64 L42 40 L68 40 L76 64 M42 40 L52 64 L68 40 M52 64 L24 64" stroke="#d9534f" stroke-width="3.4"/>'
            '<path d="M36 34 L48 34 M68 40 L64 28 L72 26" stroke-width="3.4"/>'
            '<circle cx="24" cy="64" r="2.5" fill="#24323f" stroke="none"/><circle cx="76" cy="64" r="2.5" fill="#24323f" stroke="none"/>')


def luftmatratze():
    return ('<rect x="6" y="38" width="88" height="32" rx="12" fill="#ffc2d1"/>'
            '<path d="M30 40 V68 M44 40 V68 M58 40 V68 M72 40 V68" stroke-width="2" stroke="#cf6f89"/>'
            '<path d="M6 54 Q6 40 18 38 L26 38 L26 70 L18 70 Q6 68 6 54 Z" fill="#ffd9e2"/>')


def schwimmring():
    s = '<circle cx="50" cy="52" r="34" fill="#ff9f9f"/>'
    for a in (0, 90, 180, 270):
        s += (f'<path d="M50 18 A34 34 0 0 1 74 28 L61 41 A15 15 0 0 0 50 37 Z" fill="#ffffff" '
              f'stroke="none" transform="rotate({a} 50 52)"/>')
    s += '<circle cx="50" cy="52" r="34"/><circle cx="50" cy="52" r="15" fill="#ffffff"/>'
    return s


def stein():
    return ('<path d="M16 72 Q12 52 28 42 Q44 30 62 36 Q84 40 86 60 Q88 78 64 82 Q34 86 16 72 Z" fill="#cfd4d9"/>'
            '<path d="M40 52 Q46 48 52 52 M60 64 Q66 60 72 64" stroke-width="2"/>')


def buch():
    return ('<path d="M12 26 Q31 20 50 28 Q69 20 88 26 L88 80 Q69 74 50 82 Q31 74 12 80 Z" fill="#ffffff"/>'
            '<path d="M50 28 V82"/>'
            '<path d="M20 38 Q31 35 42 38 M20 48 Q31 45 42 48 M20 58 Q31 55 42 58 M58 38 Q69 35 80 38 M58 48 Q69 45 80 48" '
            'stroke-width="2" stroke="#9fb6c7"/>')


def baum():
    circles = [(50, 30, 18), (34, 44, 16), (66, 44, 16), (50, 50, 18)]
    s = '<rect x="44" y="56" width="12" height="36" rx="2" fill="#c79a6b"/>'
    s += ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#9fdba5" stroke="#24323f" stroke-width="6.4"/>' for x, y, r in circles)
    s += ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#9fdba5" stroke="none"/>' for x, y, r in circles)
    return s


def fussgaenger():
    return (f'<path d="M50 44 L50 70" stroke="{INK}" stroke-width="12"/>'
            f'<path d="M50 44 L50 70" stroke="#a8e0b5" stroke-width="8"/>'
            '<path d="M50 70 L40 94 M50 70 L62 92" stroke-width="5"/>'
            f'<path d="M50 48 L36 64 M50 48 L64 60" stroke="{INK}" stroke-width="5"/>'
            '<rect x="56" y="40" width="16" height="22" rx="3" fill="#ff9f9f"/>'
            f'<circle cx="50" cy="28" r="12" fill="{SKIN}"/>'
            '<circle cx="54" cy="27" r="1.5" fill="#24323f" stroke="none"/>')


def fenster():
    s = ('<rect x="10" y="12" width="50" height="76" fill="#e8f4fc"/>'
         '<path d="M35 12 V88 M10 50 H60"/>'
         '<path d="M60 12 L82 22 L82 78 L60 88 Z" fill="#ffffff"/>')
    for y in (34, 50, 66):
        s += f'<path d="M66 {y} q6 -5 12 0 q6 5 12 0" stroke="{COLD}" stroke-width="2.6"/>'
    return s


def auto():
    return ('<circle cx="10" cy="62" r="7" fill="#cfd4d9"/><circle cx="6" cy="50" r="5" fill="#cfd4d9"/>'
            '<path d="M20 64 L20 50 Q22 44 30 44 L38 32 Q41 28 47 28 L66 28 Q71 28 75 33 L83 44 Q92 46 92 54 L92 64 Z" fill="#c9d6e2"/>'
            '<path d="M42 34 L37 44 H56 V34 Z M61 34 V44 H77 L71 34 Z" fill="#ffffff"/>'
            '<circle cx="36" cy="66" r="9" fill="#ffffff"/><circle cx="76" cy="66" r="9" fill="#ffffff"/>')


def fabrik():
    s = '<circle cx="80" cy="16" r="8" fill="#cfd4d9"/><circle cx="90" cy="8" r="6" fill="#cfd4d9"/><circle cx="70" cy="10" r="5" fill="#cfd4d9"/>'
    s += ('<path d="M8 88 V52 L28 64 V52 L48 64 V52 L68 64 V30 H84 V88 Z" fill="#e1e6eb"/>'
          '<rect x="18" y="72" width="10" height="10" fill="#ffffff"/><rect x="40" y="72" width="10" height="10" fill="#ffffff"/>')
    return s


def feder():
    return ('<path d="M24 86 Q40 50 78 14 Q82 40 60 62 Q46 76 24 86 Z" fill="#f2e7ff"/>'
            '<path d="M20 92 L66 32" stroke-width="2.4"/>')


def fallschirm():
    return ('<path d="M14 40 Q50 0 86 40 Q77 34 68 40 Q59 34 50 40 Q41 34 32 40 Q23 34 14 40 Z" fill="#ffe27a"/>'
            '<path d="M14 40 L46 76 M32 40 L47 76 M50 40 L50 76 M68 40 L53 76 M86 40 L54 76" stroke-width="1.8"/>'
            '<rect x="42" y="76" width="16" height="12" rx="3" fill="#ff9f9f"/>')


def finger():
    return (f'<path d="M0 44 L22 44 Q30 44 30 50 Q30 56 22 56 L0 56" fill="{SKIN}"/>'
            '<path d="M22 47 Q25 47 25 50" stroke-width="1.6"/>')
