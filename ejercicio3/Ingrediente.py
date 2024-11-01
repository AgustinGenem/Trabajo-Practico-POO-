class Ingrediente:
    def __init__(self, nombre, cantidad, unidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad = unidad

    def mostrar(self):
        return f"{self.nombre} {self.cantidad} {self.unidad}"
