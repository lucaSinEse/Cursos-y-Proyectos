const { Browser } = require('puppeteer');
const puppeteer = require('puppeteer');

describe('Interactuando con elementos', () => {
    
    it('Debe interactuar con los elementos de distintas formas',async() => {

        const browser = await puppeteer.launch({
            headless : false,
            defaultViewport: null,
        });

        const page = await browser.newPage();

        await page.goto('https://demo.guru99.com/test/simple_context_menu.html');
        //! Click derecho
        //await page.click('#authentication > span',{button: 'right', delay:500});
        //await new Promise((resolve) => setTimeout(resolve, 3000));

        //! Esto es muy util a la hora de tener que aceptar alertas para poder seguir avanzando
        page.on('dialog', async(dialog)=>{

            await new Promise((resolve) => setTimeout(resolve, 3000));
            await dialog.accept();
        })
        //! Doble click
        await page.click('#authentication > button',{clickCount:2});
        await new Promise((resolve) => setTimeout(resolve, 3000));

        //!Ir a otra pagina a probar cosas
        await page.goto('https://devexpress.github.io/testcafe/example/');
        
        await page.type('#developer-name','HOLAAAAAA');
        await new Promise((resolve) => setTimeout(resolve, 3000));
        
        await page.click('#remote-testing');
        await new Promise((resolve) => setTimeout(resolve, 3000));
        
        await page.click('#tried-test-cafe');
        await new Promise((resolve) => setTimeout(resolve, 3000));
        
        await page.type('#comments','Comentario god');
        await new Promise((resolve) => setTimeout(resolve, 3000));
        
        await page.click('#submit-button');
        await new Promise((resolve) => setTimeout(resolve, 3000));
        
        await browser.close();
    }, 550000);
});