class Persona:
    def __init__(self, nombre, edad) -> None:
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

luca = Persona("Luca", 23)

nombre = luca.get_nombre()
print(nombre)

luca.set_nombre("Pepito")

nombre = luca.get_nombre()
print(nombre)