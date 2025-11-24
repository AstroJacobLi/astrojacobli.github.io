const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('http://localhost:8000/research/');

  // Click the first lightbox trigger
  await page.click('.lightbox-trigger');
  
  // Wait for overlay to be active
  await page.waitForSelector('#lightbox-overlay.active', { visible: true });
  console.log('Lightbox opened successfully');

  // Check if image src is correct
  const imgSrc = await page.('#lightbox-image', el => el.src);
  console.log('Lightbox image src:', imgSrc);

  // Close lightbox
  await page.click('.lightbox-close');
  
  // Wait for overlay to be inactive
  await page.waitForSelector('#lightbox-overlay', { hidden: true });
  console.log('Lightbox closed successfully');

  await browser.close();
})();
