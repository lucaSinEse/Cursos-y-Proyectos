const puppeteer = require('puppeteer');

describe('Extraer info', () => {
    
    let browser;
    let page;

    beforeAll(async()=>{
        browser = await puppeteer.launch({
            headless:false,
            defaultViewport:null,
            executablePath:'/usr/bin/brave-browser',
            //slowMo:250,
        });

        page = await browser.newPage();
        await page.goto('https://demoqa.com/modal-dialogs', {waitUntil:'networkidle0'});
    }, 100000);

    afterAll(async()=>{
        (await browser).close();
    }, 100000)

    it('Extraer el título de la página',async () => {

        const titulo = await page.title();
        const url = await page.url();

        console.log('titulo: ',titulo);
        console.log('url: ',url);

    }, 500000);

    it('Extraer la informacion de un elemento', async() => {

        await page.waitForSelector('#showLargeModal');

        //!devuelve el priemr elemento que encuentre
        const boton = await page.$eval('#showLargeModal', element => {
            return element.textContent;
        });

        console.log('Boton : ', boton);

    }, 50000);

    it('Contar los elementos de una pagina', async () => {
        page.goto('https://www.docappoint.com.mx/', {waitUntil: 'networkidle0'});

        //! Devuelve el arreglo de elementos que encuentre
        await page.waitForSelector('#root > div:nth-child(3) > div > div:nth-child(2) > section > div:nth-child(1) > article:nth-child(5) > div > ul.react-multi-carousel-track > li.react-multi-carousel-item.react-multi-carousel-item--active > img')
        
        const images = await page.$$eval('img', imagenes => {
            return imagenes.length
        });
        console.log('cantidad de imagenes: ', images);

    }, 50000);
});