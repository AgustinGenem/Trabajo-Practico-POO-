from Ingrediente import Ingrediente

class Plato:
    def __init__(self, nombre, precio, es_bebida):
        self.nombre = nombre
        self.precio = precio
        self.es_bebida = es_bebida
        self.ingredientes = []

    def agregar_ingrediente(self, ing):
        self.ingredientes.append(ing)

    def mostrar(self):
        info = f"{self.nombre}\nPrecio: $ {self.precio}\n"
        if not self.es_bebida:
            info += "Ingredientes:\n"
            for ing in self.ingredientes:
                info += ing.mostrar() + "\n"
        return info + "----------------------------------"
