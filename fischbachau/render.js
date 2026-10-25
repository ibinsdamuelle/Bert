const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [html, pdf, pngPrefix] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  // Report overflow per page: bottom of last content block vs footer top
  const info = await page.evaluate(() => [...document.querySelectorAll('.page')].map(p => {
    const pr = p.getBoundingClientRect();
    const content = p.querySelector('.content');
    const kids = [...content.children];
    const bottom = Math.max(...kids.map(k => k.getBoundingClientRect().bottom)) - pr.top;
    const foot = p.querySelector('.foot').getBoundingClientRect().top - pr.top;
    return { pageH: pr.height, contentBottom: Math.round(bottom), footTop: Math.round(foot), freePx: Math.round(foot - bottom) };
  }));
  console.log(JSON.stringify(info));
  console.log('fonts:', await page.evaluate(() => [...document.fonts].map(f => f.family + ' ' + f.style + ' ' + f.status).join(', ')));
  await page.emulateMedia({ media: 'print' });
  await page.pdf({ path: pdf, format: 'A4', printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  const pages = await page.$$('.page');
  for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: `${pngPrefix}-${i + 1}.png` });
  await browser.close();
})();
