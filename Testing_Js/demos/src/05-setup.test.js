describe('group 1', () =>{

    beforeAll(() =>{
        console.log('beforeAll')
        //! Up DB
    })

    afterAll(() =>{
        console.log('afterAll')
        //! Down DB
    });

    beforeEach(() =>{
        console.log('beforeEach')
        //!Corre entre cada test
    }) 

    afterEach(() =>{
        console.log('afterEach')
        //!Corre entre cada test
    }) 

    test('case 1', () =>{
        console.log('case 1')
        expect(1 + 1).toBe(2)
    });

    test('case 2', () =>{
        console.log('case 2')
        expect(1 + 3).toBe(4)
    });

    describe('group 2', () =>{

        beforeAll(() =>{
            console.log('beforeAll Group 2')
            //! Up DB
        })

        afterAll(() =>{
            console.log('afterAll Group 2')
            //! Down DB
        });

        test('case 3', () =>{
        console.log('case 3')
            expect(1 + 3).toBe(4)
        });

        test('case 4', () =>{
        console.log('case 4')
            expect(1 + 3).toBe(4)
        });
    })
});

// beforeAll(): se ejecuta antes de todas las pruebas.
// beforeEach(): se ejecuta antes de cada prueba.
// afterEach(): se ejecuta después de cada prueba.
// afterAll(): se ejecuta después de todas las pruebas Nota: Todas estas funciones se ejecutan dentro del alcance del scope.
