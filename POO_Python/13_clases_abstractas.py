from abc import abstractclassmethod, ABC

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llano {self.nombre} y tengo {self.edad} años")

#luca = Persona("luca", 23, "masculino", "programador")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Me dedico a {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Trabajo de: {self.actividad}")

luca = Estudiante("luca", 23, "masculino", "programador")

luca.hacer_actividad()

luca = Trabajador("luca", 23, "masculino", "programador")
luca.hacer_actividad()