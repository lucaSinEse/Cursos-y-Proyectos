'''
Clase: resta que hay que seguir para obtener el objeto.
    Podemos defiirle las caracteristicas y todo lo que a a tener el objeto.
'''

class Celular:
    #metodo constructor
    #cuando creemos un objeto, lo prmero que se ejecuta es esto.
    #decir self.marca es equivalente a decir celular.marca
    def __init__(self, marca, modelo, camara) -> None:
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    #Los metodos son, basicamente, funciones de toda la vida.
    #la unica diferencia es que hay que pasarle el parametro self para que haga referencia al objeto
    #Nos sirven para definir las acciones que puede hacer nuestro objeto
    def llamar(self):
        print(f"estas haciendo una llamada desde un: {self.modelo}")
    
    def cortar(self):
        print(f"estas cortando una llamada desde un: {self.modelo}")

celular_1 = Celular("Samsung", "S23", "48MP")
celular_2 = Celular("Apple", "Iphone 15", "92MP")

celular_2.llamar()
celular_2.cortar()