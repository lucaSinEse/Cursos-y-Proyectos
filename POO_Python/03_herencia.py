class Persona:
    def __init__(self, nombre, edad, nacionalidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario) -> None:
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad) -> None:
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

roberto = Empleado("Roberto", 42, "argentino", "programador", 100000)

print(roberto.nombre)
roberto.hablar()