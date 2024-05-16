import puppeteer from 'puppeteer';
import {KnownDevices} from 'puppeteer';


describe('Emulando disposirtivos', () => {
    
    let browser;
    let page;
    let iPhone = KnownDevices['iPhone 6'];
    let tablet = KnownDevices['iPad Pro landscape'];

    beforeAll(async()=>{
        browser = await puppeteer.launch({
            headless : false,
            defaultViewport: null,
            //executablePath:'app/com.brave.Browser/x86_64/stable',
        });

        page = await browser.newPage()
    }, 100000)

    afterAll(async() =>{
        await browser.close();
    }, 100000)

    it('Emulando disposiitivos de forma manual', async () => {
        await page.emulate(iPhone);
        await page.goto('https://demoqa.com/modal-dialogs', {waitUntil: 'networkidle0'});
    }, 350000);

    it('Emulando un sitio en una tablet', async () => {
        await page.emulate(tablet);
        //! Para que espere 5 segunditos
        await page.goto('https://demoqa.com/modal-dialogs', {waitUntil: 'networkidle0'});
        await new Promise((resolve) => setTimeout(resolve, 5000));
    }, 35000);
});