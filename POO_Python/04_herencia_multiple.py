class Persona:
    def __init__(self, nombre, edad, nacionalidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando")

class Artista():
    def __init__(self, habilidad) -> None:
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"mi habilidad es {self.habilidad}"

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa) -> None:
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        return f'hola, soy {self.nombre}, {super().mostrar_habilidad()}, mi salario es de $ {self.salario} y laburo en {self.empresa}'


roberto = EmpleadoArtista("Roberto", 42, "argentino", "cantar", 100000, "Arcor")

print(roberto.nombre)
print(roberto.presentarse())

herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)

instancia = isinstance(roberto, Artista)
print(instancia)