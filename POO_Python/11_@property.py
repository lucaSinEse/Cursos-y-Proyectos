class Persona:
    def __init__(self, nombre, edad) -> None:
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        del self._nombre


luca = Persona("Luca", 23)
nombre = luca.nombre

print(nombre)

luca.nombre = "Pepe"

nombre = luca.nombre

print(nombre)

del luca.nombre