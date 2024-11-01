from Habitacion import Habitacion

class Vivienda:
    def __init__(self, calle: str, numero: int, manzana: str, nroCasa: int, superficieTerreno: float):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []

    def agregar_habitacion(self, habitacion: Habitacion):
        self.habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self):
        metros_cubiertos = sum(habitacion.metrosCuadrados for habitacion in self.habitaciones)
        if metros_cubiertos > self.superficieTerreno:
            raise ValueError("La superficie cubierta no puede ser mayor a la superficie del terreno")
        return metros_cubiertos

    def __str__(self):
        habs = "\n  ".join(str(habitacion) for habitacion in self.habitaciones)
        return f"Vivienda en {self.calle} {self.numero}, Manzana: {self.manzana}, Casa Nro: {self.nroCasa}, " \
               f"Superficie de Terreno: {self.superficieTerreno} m²\n  {habs}"
