class Personaje:
    def __init__(self, nombre, fuerza, velocidad) -> None:
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self) -> str:
        return f"{self.nombre} (fuerza: {self.fuerza}, velocidad: {self.velocidad})"
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad)/2)**2

        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

goku = Personaje("Goku", 100, 100)
print(goku)
vegetta = Personaje("Vegetta", 101, 101)

nuevo_personaje = goku + vegetta

print(nuevo_personaje)