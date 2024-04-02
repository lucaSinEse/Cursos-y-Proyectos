// matchers

test('test obj', () =>{
    const data = {name: 'Luca'}
    data.lastname = 'Cussino'
    expect(data).toEqual({name: 'Luca', lastname: 'Cussino'})
});

test('null', () =>{
    const data = null
    expect(data).toBeNull();
    expect(data).toBeDefined();
    expect(data).not.toBeUndefined();
});

test('booleans', () =>{
    //! To Equal
    expect(true).toEqual(true);
    expect(false).toEqual(false);

    //! To Be
    expect(0).toBeFalsy();
    expect('').toBeFalsy();
    expect(false).toBeFalsy();
    expect(true).toBeTruthy();
    
    //! To Match
    expect('Christoph').toMatch(/stop/);
});

test('list / arrays', () =>{
    const numbers = [1, 2, 3, 4]
    //! To Contain
    expect(numbers).toContain(3);
});