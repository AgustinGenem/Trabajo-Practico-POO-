from ComponenteCPU import ComponenteCPU

class Computadora:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.componentes = []

    def agregar_componente(self, componente: ComponenteCPU):
        self.componentes.append(componente)

    def costo_total(self):
        return sum(componente.costo_total() for componente in self.componentes)

    def precio_sugerido(self):
        costo = self.costo_total()
        if costo < 50000:
            return costo * 1.40
        else:
            return costo * 1.30
