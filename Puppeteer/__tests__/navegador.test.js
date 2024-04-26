const puppeteer = require('puppeteer')

describe('Mi primer test en puppeteer', () =>{
    
    it('Debe de abrir y cerrar el navegador', async () =>{

        const browser = await puppeteer.launch({
            headless : false,
            //! Para que se abra brave en lugar de chromium
            //* executablePath: '/usr/bin/brave-browser'
            executablePath:'/usr/bin/brave-browser',
            slowMo: 200,
            devtools: false,
            //! Modificar el tamaño de la ventana
            // defaultViewport:{
            //     width:1920,
            //     height:1080
            // },
            // args:['--window-size=1920,1080'],
            defaultViewport: null
        });

        page = await browser.newPage()

        await page.goto('https://es.wikipedia.org/wiki/Wikipedia:Portada')

        //! Para que espere 5 segunditos
        // await new Promise((resolve) => setTimeout(resolve, 5000));

        await page.waitForSelector('img');
        
        //! Recargar la pagina
        await page.reload();

        //!Navegar a otro sitio
        await page.goto('https://www.docappoint.com.mx/')
        
        await page.waitForSelector('#root > div:nth-child(3) > div > div:nth-child(2) > section > div:nth-child(1) > header > div:nth-child(1) > img');

        //! Navegar hacia atras
        await page.goBack();

        await page.waitForSelector('img');

        await page.goForward();

        await page.waitForSelector('img');

        page2 = await browser.newPage()

        await page2.goto('https://www.youtube.com/watch?v=3mphS7dU7Os');
        await browser.close();
    });
}, 300000);