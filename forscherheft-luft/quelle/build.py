"""Erzeugt die HTML-Dateien und druckt sie mit Chromium als PDF.

Aufruf (im Ordner quelle/):  python3 build.py
Benötigt: Python 3, Node.js mit Playwright (Chromium).
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import heft  # noqa: E402

JOBS = [("forscherheft.html", heft.build, "Forscherheft_Luft_Klasse2.pdf", "")]
try:
    import lehrer  # noqa: E402
    JOBS += [("lehrerhandreichung.html", lehrer.build_planung, "_planung.pdf", "fluss"),
             ("kopiervorlagen.html", lehrer.build_kopiervorlagen, "_kopiervorlagen.pdf", "")]
except ImportError:
    lehrer = None


def main():
    env = dict(os.environ)
    npm_root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    env["NODE_PATH"] = npm_root
    for html_name, fn, pdf_name, mode in JOBS:
        html_path = os.path.join(HERE, html_name)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(fn())
        pdf_path = os.path.join(OUT, pdf_name)
        subprocess.run(["node", os.path.join(HERE, "print.mjs"), html_path, pdf_path] + ([mode] if mode else []),
                       check=True, env=env)
    if lehrer is not None:
        final = os.path.join(OUT, "Lehrerhandreichung_Luft_Klasse2.pdf")
        parts = [os.path.join(OUT, "_planung.pdf"), os.path.join(OUT, "_kopiervorlagen.pdf")]
        subprocess.run(["pdfunite"] + parts + [final], check=True)
        for p in parts:
            os.remove(p)
        print("PDF geschrieben:", final)


if __name__ == "__main__":
    main()
