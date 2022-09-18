class Zoologico:
    _zonas = []

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    @classmethod
    def cantidadTotalAnimales(cls):
        total = 0
        for zona in cls._zonas:
            total += zona.cantidadAnimales()

        return total

    