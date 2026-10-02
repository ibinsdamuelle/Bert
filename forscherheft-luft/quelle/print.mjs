// HTML -> PDF mit Chromium (Playwright).
// Aufruf: node print.mjs <eingabe.html> <ausgabe.pdf> [fluss]
import { createRequire } from 'module';
import path from 'path';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const [, , input, output, mode] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('file://' + path.resolve(input), { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
const opts = { path: output, printBackground: true, format: 'A4' };
if (mode === 'fluss') {
  // Fließtext mit Seitenzahlen im Fuß
  opts.displayHeaderFooter = true;
  opts.headerTemplate = '<span></span>';
  opts.footerTemplate =
    '<div style="width:100%;font-size:8px;color:#6c7f8f;font-family:DejaVu Sans,sans-serif;padding:0 16mm;display:flex;justify-content:space-between">' +
    '<span>Forscherheft Luft · Klasse 2 · Lehrerhandreichung</span><span>Seite <span class="pageNumber"></span> von <span class="totalPages"></span></span></div>';
  opts.margin = { top: '15mm', bottom: '16mm', left: '16mm', right: '16mm' };
} else {
  opts.preferCSSPageSize = true;
  opts.margin = { top: '0', bottom: '0', left: '0', right: '0' };
}
await page.pdf(opts);
await browser.close();
console.log('PDF geschrieben:', output);
