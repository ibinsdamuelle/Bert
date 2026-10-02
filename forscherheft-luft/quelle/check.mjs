// Prüft feste Seiten auf Überlauf und meldet die Höhe der Malfelder (in mm).
import { createRequire } from 'module';
import path from 'path';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('file://' + path.resolve(process.argv[2]), { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.emulateMedia({ media: 'print' });
const res = await page.evaluate(() => {
  const mm = v => Math.round(v / 3.7795 * 10) / 10;
  const out = [];
  document.querySelectorAll('.page').forEach((pg, i) => {
    const r = pg.getBoundingClientRect();
    const padB = parseFloat(getComputedStyle(pg).paddingBottom);
    const limit = r.bottom - padB + 1;
    const probs = [];
    pg.querySelectorAll(':scope > *:not(.fuss)').forEach(el => {
      const b = el.getBoundingClientRect().bottom;
      if (b > limit) probs.push(`${el.className} ragt ${mm(b - limit)}mm über`);
    });
    pg.querySelectorAll('.grow, .box, .malfeld, .karte, .kv').forEach(el => {
      if (el.scrollHeight > el.clientHeight + 3) probs.push(`${el.className} Inhalt zu hoch um ${mm(el.scrollHeight - el.clientHeight)}mm`);
    });
    const mal = [...pg.querySelectorAll('.malfeld')].map(m => mm(m.getBoundingClientRect().height));
    out.push(`S.${i + 1}: ${probs.length ? 'PROBLEM: ' + probs.join('; ') : 'ok'}${mal.length ? ' | Malfeld ' + mal.join(', ') + 'mm' : ''}`);
  });
  return out;
});
console.log(res.join('\n'));
await browser.close();
