class Estudiante:
    def __init__(self, nombre, edad, grado) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    #metodos
    def estudiar(self):
        print(f"el estudiante {self.nombre} esta estudiando")

nombre = str(input("Ingresar nombre: ")).lower().capitalize()
edad = int(input("Ingresar edad: "))
grado = str(input("Ingresar grado: ")).lower().capitalize()

estudiante_1 = Estudiante(nombre, edad, grado)

palabra = str(input("Que decea hacer?")).lower().capitalize()

if palabra == "Estudiar":
    estudiante_1.estudiar()