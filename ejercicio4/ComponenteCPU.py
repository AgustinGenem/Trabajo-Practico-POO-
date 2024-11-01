class ComponenteCPU:
    def __init__(self, componente: str, marca: str, cantidad: int, precio: float):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio

    def costo_total(self):
        return self.cantidad * self.precio
