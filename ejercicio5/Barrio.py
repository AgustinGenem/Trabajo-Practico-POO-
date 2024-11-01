from Vivienda import Vivienda

class Barrio:
    def __init__(self, nombre: str, empresaConstructora: str):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []

    def agregar_vivienda(self, vivienda: Vivienda):
        self.viviendas.append(vivienda)

    def getSuperficieTotalTerreno(self):
        return sum(vivienda.superficieTerreno for vivienda in self.viviendas)

    def getSuperficieTotalTerrenoXManzana(self, manzana: str):
        return sum(vivienda.superficieTerreno for vivienda in self.viviendas if vivienda.manzana == manzana)

    def getSuperficieTotalCubierta(self):
        return sum(vivienda.getMetrosCuadradosCubiertos() for vivienda in self.viviendas)

    def __str__(self):
        vivs = "\n".join(str(vivienda) for vivienda in self.viviendas)
        return f"Barrio: {self.nombre}, Empresa Constructora: {self.empresaConstructora}\nViviendas:\n{vivs}"
