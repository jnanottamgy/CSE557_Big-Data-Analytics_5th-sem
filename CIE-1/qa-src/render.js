const { chromium } = require(process.env.PW || 'playwright');
(async () => {
  const [,, inHtml, outPdf] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + inHtml, { waitUntil: 'networkidle' });
  await page.pdf({
    path: outPdf, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: `<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5pt;color:#8a93a8;padding:0 15mm;display:flex;justify-content:space-between">
      <span>BDA · CIE-1 Expected Questions &amp; Answers · CSE557</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
  });
  await browser.close();
})();
