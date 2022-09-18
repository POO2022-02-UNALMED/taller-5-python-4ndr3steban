

class Animal:
    _totalAnimales = 0
    _zona = []
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        _totalAnimales += 1

    #def movimiento(self):

    @staticmethod
    def totalPorTipo():
        txt = f"Mamiferos : {Mamifero.cantidadMamifero()}\nAves : {Ave.cantidadAves()}\nReptiles : {Reptil.cantidadReptiles()}\nPeces : {Pez.cantidadPeces}\nAnfibios : {Anfibio.cantidadAnfibios()}"
        return txt

    def __str__(self):
        if len(self._zonna) == 0:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona[0]}, en el {self._zona[0].getZoo()}"

