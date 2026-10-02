"""Gemeinsame Bausteine (CSS + HTML-Helfer) für Forscherheft und Lehrermaterial."""
from icons import svg, lufti, denkblase, lupe, gluehbirne, kiste, kolben, frage

FONT_CSS = """
@font-face { font-family: 'Andika'; font-weight: 400; font-style: normal;
  src: url('fonts/andika-latin-400-normal.woff2') format('woff2');
  unicode-range: U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD; }
@font-face { font-family: 'Andika'; font-weight: 700; font-style: normal;
  src: url('fonts/andika-latin-700-normal.woff2') format('woff2');
  unicode-range: U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD; }
@font-face { font-family: 'Andika'; font-weight: 400; font-style: normal;
  src: url('fonts/andika-latin-ext-400-normal.woff2') format('woff2');
  unicode-range: U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113; }
@font-face { font-family: 'Andika'; font-weight: 700; font-style: normal;
  src: url('fonts/andika-latin-ext-700-normal.woff2') format('woff2');
  unicode-range: U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113; }
"""

BASE_CSS = FONT_CSS + """
:root {
  --ink:#24323f; --muted:#6c7f8f; --blue:#1f6fae; --sky:#e8f4fc; --sky2:#cfe7f7;
  --yellow:#ffd54a; --yellow-t:#fff8d9; --orange:#e07b22; --orange-t:#fff3e4;
  --violet:#6f52b8; --violet-t:#f3effb; --green:#2b8a50; --green-t:#e7f5ec;
  --red:#d9534f; --line:#9db9cf;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #ffffff; }
body { font-family: 'Andika', 'DejaVu Sans', sans-serif; color: var(--ink);
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
svg.ic { display: block; width: 100%; height: 100%; overflow: visible; }
"""

HEFT_CSS = BASE_CSS + """
@page { size: A4; margin: 0; }
body { font-size: 14pt; line-height: 1.32; }
.page { width: 210mm; height: 297mm; padding: 11mm 14mm 13mm; position: relative;
  overflow: hidden; break-after: page; display: flex; flex-direction: column; }
.page:last-child { break-after: auto; }
.fuss { position: absolute; left: 14mm; right: 14mm; bottom: 5.5mm; display: flex;
  justify-content: space-between; font-size: 9pt; color: var(--muted); }
.fuss .nr { font-weight: 700; color: var(--blue); }

/* Kopfzeile eines Versuchs */
.vhead { display: flex; justify-content: space-between; align-items: center;
  background: var(--sky); border-radius: 3mm; padding: 1.4mm 4mm; font-size: 11pt;
  color: var(--blue); font-weight: 700; }
.vhead .vnum { background: var(--blue); color: #fff; border-radius: 10mm; padding: 0.4mm 3.5mm; }
.titel { display: flex; align-items: center; gap: 3mm; margin: 2.4mm 0 1.4mm; }
.titel .ico { width: 12mm; height: 12mm; flex: none; }
.titel h1 { font-size: 20.5pt; line-height: 1.12; margin: 0; }

.kopf { display: flex; align-items: center; gap: 2mm; font-weight: 700; font-size: 13.5pt; margin-bottom: 1.2mm; }
.kopf .ico { width: 8.5mm; height: 8.5mm; flex: none; }
.kopf .hint { font-weight: 400; font-size: 11.5pt; color: var(--muted); }

.oben { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; margin-top: 1mm; }
.box { border: 0.6mm solid var(--line); border-radius: 4mm; padding: 1.8mm 3.4mm 2.2mm; margin-top: 2.2mm; background: #fff; }
.oben .box { margin-top: 0; }
.box.material { background: var(--sky); border-color: var(--sky2); }
.box.illu { display: flex; align-items: center; justify-content: center; padding: 2mm; border-style: dashed; }
.box.illu svg { width: 100%; height: auto; max-height: 46mm; }
.matstrip { display: flex; align-items: center; gap: 3mm; background: var(--sky); border: 0.6mm solid var(--sky2);
  border-radius: 4mm; padding: 1.4mm 3.4mm; margin-top: 0.6mm; }
.matstrip .kopf { margin: 0; flex: none; }
.chips { display: flex; flex-wrap: wrap; gap: 1.2mm 4.5mm; }
.chip { display: flex; align-items: center; gap: 1.6mm; font-size: 12.5pt; line-height: 1.1; }
.chip .pic { width: 10mm; height: 10mm; flex: none; background: #fff; border-radius: 2.2mm; padding: 0.7mm; }
.mitte { display: grid; grid-template-columns: 1.7fr 1fr; gap: 3mm; margin-top: 2.2mm; }
.mitte .box { margin-top: 0; }
.ekopf { display: flex; align-items: center; justify-content: space-between; gap: 3mm; flex-wrap: wrap; }
.ekopf .kopf { margin-bottom: 0.6mm; }
.mat { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5mm 2.5mm; }
.mat.eins { grid-template-columns: 1fr; }
.mat .it { display: flex; align-items: center; gap: 2mm; font-size: 12.5pt; line-height: 1.15; }
.mat .it .pic { width: 11mm; height: 11mm; flex: none; background: #fff; border-radius: 2.5mm; padding: 0.8mm; }

ol.steps { list-style: none; counter-reset: s; margin: 0; padding: 0; }
ol.steps li { counter-increment: s; position: relative; padding-left: 9mm; margin: 0.8mm 0; line-height: 1.25; }
ol.steps li::before { content: counter(s); position: absolute; left: 0; top: 0.2mm; width: 6.6mm; height: 6.6mm;
  border-radius: 50%; background: var(--blue); color: #fff; font-weight: 700; font-size: 11.5pt;
  display: flex; align-items: center; justify-content: center; }

.box.vermutung { background: var(--orange-t); border-color: #f5c99a; }
.box.beobachtung { background: var(--violet-t); border-color: #cbbbeb; display: flex; flex-direction: column; }
.box.beobachtung > * { flex: none; }
.box.beobachtung > .malfeld { flex: 1 1 auto; min-height: 20mm; }
.box.ergebnis { background: var(--green-t); border-color: #a9d8ba; }
.grow { flex: 1 1 auto; min-height: 0; }

.ck { display: inline-block; width: 5.4mm; height: 5.4mm; border: 0.55mm solid var(--ink); border-radius: 1.2mm;
  background: #fff; vertical-align: -0.9mm; margin-right: 2mm; flex: none; }
.opts { display: flex; flex-wrap: wrap; gap: 1mm 7mm; }
.opts.col { flex-direction: column; }
.opt { white-space: nowrap; }

.malfeld { flex: 1 1 auto; min-height: 20mm; border: 0.5mm solid #b7a7de; border-radius: 3mm; background: #fff;
  position: relative; overflow: hidden; }
.malfeld .scaff { position: absolute; left: 0; right: 0; bottom: 0; top: 0; display: flex; align-items: flex-end; justify-content: center; }
.malfeld .scaff svg { height: 92%; width: auto; }
.malfeld .ecke { position: absolute; left: 3mm; top: 2mm; font-size: 10.5pt; color: var(--muted); }

.luecke { display: inline-block; min-width: 30mm; height: 6.2mm; border-bottom: 0.45mm solid var(--ink);
  margin: 0 1mm; vertical-align: -1.6mm; }
.luecke.kurz { min-width: 20mm; }
.luecke.lang { min-width: 42mm; }
.satz { margin: 0.6mm 0; line-height: 1.5; }
.wortkasten { display: flex; flex-wrap: wrap; gap: 1.4mm 2.2mm; align-items: center; font-size: 12.5pt; }
.wortkasten .lbl { font-size: 10.5pt; color: var(--green); font-weight: 700; }
.wort { border: 0.45mm dashed var(--green); border-radius: 2mm; padding: 0.1mm 2.6mm; background: #fff; }

.tipp { display: flex; align-items: center; gap: 2.5mm; margin-top: 2mm; }
.tipp .lufti { width: 14mm; height: 12mm; flex: none; }
.tipp .blase { position: relative; background: var(--yellow-t); border: 0.5mm solid #e8c64a; border-radius: 4mm;
  padding: 1.6mm 3.5mm; font-size: 12pt; line-height: 1.25; }
.tipp .blase b { color: #9a6b00; }
.profi { border: 0.6mm dashed #e8c64a; background: #fffdf2; }
.profi .kopf .stern { width: 7.5mm; height: 7.5mm; }

/* Lineatur (Klasse 2): Ober-, Mittel- und Unterband, Mittelband hinterlegt */
.lin { height: 12.6mm; margin: 0 0 2.6mm;
  background:
    linear-gradient(#9db9cf,#9db9cf) 0 0 / 100% 0.28mm no-repeat,
    linear-gradient(#9db9cf,#9db9cf) 0 4.1mm / 100% 0.28mm no-repeat,
    linear-gradient(#eaf3f9,#eaf3f9) 0 4.38mm / 100% 3.95mm no-repeat,
    linear-gradient(#5f87a6,#5f87a6) 0 8.33mm / 100% 0.4mm no-repeat,
    linear-gradient(#9db9cf,#9db9cf) 0 12.32mm / 100% 0.28mm no-repeat; }

table.tab { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 12.5pt; }
table.tab th, table.tab td { border: 0.4mm solid #c4b6e6; padding: 1.4mm 2.2mm; text-align: left; vertical-align: middle; background: #fff; }
table.tab th { background: #e9e2f8; font-size: 11.5pt; }
table.tab td.c, table.tab th.c { text-align: center; }
table.tab .pic { width: 10mm; height: 10mm; display: inline-block; vertical-align: middle; margin-right: 2mm; }
"""


def icon_box(inner, cls="ico", vb="0 0 100 100"):
    return f'<span class="{cls}">{svg(inner, vb=vb)}</span>'


def kopf(icon_inner, text, hint=""):
    h = f' <span class="hint">{hint}</span>' if hint else ""
    return f'<div class="kopf">{icon_box(icon_inner)}<span>{text}{h}</span></div>'


def ck(text):
    return f'<span class="opt"><span class="ck"></span>{text}</span>'


def luecke(cls=""):
    return f'<span class="luecke {cls}"></span>'


def lineatur(n=1):
    return '<div class="lin"></div>' * n


def tipp(text, mood="froh"):
    return (f'<div class="tipp"><span class="lufti">{svg(lufti(mood), vb="4 18 92 74")}</span>'
            f'<div class="blase">{text}</div></div>')


def fuss(nr, links="Forscherheft Luft · Klasse 2"):
    return f'<div class="fuss"><span>{links}</span><span class="nr">{nr}</span></div>'


ICON_FRAGE = frage()
ICON_MATERIAL = kiste()
ICON_VERSUCH = kolben()
ICON_VERMUTUNG = denkblase()
ICON_BEOBACHTUNG = lupe()
ICON_ERGEBNIS = gluehbirne()
