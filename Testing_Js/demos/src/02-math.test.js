const {sum, subtract, multiply, divide} = require('./02-math')

describe('Test for Math', () =>{

    describe('test for sum', () =>{
        test('adds 1 + 3 should be 4', () =>{
            const rta = sum(1, 3);
            expect(rta).toBe(4);
        });
    });
    
    describe('Test for Multiply', () =>{
        test('should be 4', () =>{
            const rta = multiply(1,4);
            expect(rta).toBe(4);
        });
    });
    
    describe('Test for Divide', () =>{
        test('should divide', () =>{
            const rta = divide(6,3);
            const rta2 = divide(5,2);
            expect(rta).toBe(2);
            expect(rta2).toBe(2.5);
        });
    });
    
    describe('Test for Divide in to Zero', () =>{
        test('should divide for zero', () =>{
            const rta = divide(6,0);
            const rta2 = divide(5,0);
            expect(rta).toBeNull();
            expect(rta2).toBeNull();
        });
    })
    
    describe('Test for Subtract', () =>{
        test("should subtract", () =>{
            const rta = subtract(10, 5)
            expect(rta).toBe(5)
        });
    });
});