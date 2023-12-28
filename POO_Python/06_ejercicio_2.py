class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    def nombre_y_edad(self):
        print(f"nombre: {self.nombre}, edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado) -> None:
        super().__init__(nombre, edad)
        self.grado = grado
    def imprimir_grado(self):
        print(f"grado: {self.grado}")

luca = Estudiante("Luca", 23, "tercero")
luca.nombre_y_edad()
luca.imprimir_grado()

class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")

class Ave(Animal):
    def volar(self):
        print("El animal esta volando")

class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()