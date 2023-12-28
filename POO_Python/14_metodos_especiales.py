class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"Persona(nombre = {self.nombre}, edad = {self.edad})"
    
    def __repr__(self) -> str:
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)
luca = Persona("Luca", 23)

print(luca)

repre = repr(luca)
resultado = eval(repre)
print(resultado)

pedro = Persona("Pedro", 30)

resultado =  luca + pedro
print(resultado)