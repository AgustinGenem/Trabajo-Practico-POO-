from Plato import Plato
from Ingrediente import Ingrediente

class MenuRestaurant:
    def __init__(self):
        self.platos_menu = []

    def cargar_platos(self):
        while True:
            nombre = input("Escribe el nombre del plato (o SALIR para terminar): ")
            if nombre.lower() == "salir":
                break

            precio = float(input("¿Cuánto vale el plato? "))
            es_bebida = input("¿Es una bebida? (s/n): ").lower() == "s"

            plato = Plato(nombre, precio, es_bebida)

            if not es_bebida:
                while True:
                    nombre_ingrediente = input("Escribe el ingrediente (o 'fin' para terminar): ")
                    if nombre_ingrediente == "fin":
                        if len(plato.ingredientes) < 1:
                            print("¡Debes agregar al menos un ingrediente para un plato que no es bebida!")
                            continue
                        break
                    cantidad = float(input("¿Cuánto hay de ese ingrediente? "))
                    unidad = input("¿Cuál es la unidad de medida? ")
                    ingrediente = Ingrediente(nombre_ingrediente, cantidad, unidad)
                    plato.agregar_ingrediente(ingrediente)

            self.platos_menu.append(plato)

    def mostrar_menu(self):
        print("-----------MENÚ----------------")
        for plato in self.platos_menu:
            print(plato.mostrar())
        print("----------------------------------")

    @staticmethod
    def main():
        menu = MenuRestaurant()
        menu.cargar_platos()
        menu.mostrar_menu()

if __name__ == "__main__":
    MenuRestaurant.main()
