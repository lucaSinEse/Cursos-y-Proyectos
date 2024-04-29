const puppeteer = require('puppeteer');

describe('Tipos de Espera', () => {

    jest.setTimeout(100000)
    it('Probamos los tipos de espera', async () => {
        const browser = await puppeteer.launch({
            headless: false,
            defaultViewport:null,
            executablePath:'/usr/bin/brave-browser',
            //slowMo: 500
        });

        const page = await browser.newPage();
        
        //! Espera a que cargue todo basicamente
        await page.goto('https://www.docappoint.com.mx/', {waitUntil: 'networkidle2'});

        //!Espera explicita (3 segundos)
        await new Promise((resolve) => setTimeout(resolve, 3000));

        //! Espera por un css selector
        await page.waitForSelector('#root > div:nth-child(3) > div > div:nth-child(2) > section > div:nth-child(1) > article:nth-child(5) > div > ul.react-multi-carousel-track > li.react-multi-carousel-item.react-multi-carousel-item--active > img');

        //! Espera por un xpath
        //! De igual forma xpath esta obsoleto che
        //await page.waitForXPath('[@id="root"]/div[3]/div/div[1]/section/div[1]/header/div[1]/img');

        await page.goto('https://demoqa.com/modal-dialogs', {waitUntil : 'networkidle2'});
        
        //!En se le puede pasar un ID pero recordar poner # y visible valida su visibilidad, tambien esta el hidden.
        await page.waitForSelector('#showSmallModal',{visible : true});
        
        await page.click('#showSmallModal');

        //! Espera por funcion
        await page.waitForFunction(()=> document.querySelector('#example-modal-sizes-title-sm').innerText ==='Small Modal')

        //!Ejemplo para observar el viewport
        // const observaResize = page.waitForFunction('window.innerWidth < 100');
        // await page.setViewport({width: 50, height: 50});

        // await observaResize

        await page.click('#closeSmallModal')

        await page.waitForFunction(()=> !document.querySelector('#example-modal-sizes-title-sm'))

        await browser.close();
    });
});
