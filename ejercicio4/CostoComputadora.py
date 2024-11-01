from Computadora import Computadora
from ComponenteCPU import ComponenteCPU

class CostoComputadora:
    @staticmethod
    def main():
        Repetir = True
        while Repetir == True:
            # Ingreso de datos de la computadora
            marca_pc = input("Ingrese la marca de la computadora: ")
            modelo_pc = input("Ingrese el modelo de la computadora: ")
            computadora = Computadora(marca_pc, modelo_pc)

            # Ingreso de componentes
            n_componentes = int(input("Ingrese el número de componentes de la computadora: "))
            for _ in range(n_componentes):
                componente = input("Ingrese el nombre del componente: ")
                marca = input("Ingrese la marca del componente: ")
                cantidad = int(input("Ingrese la cantidad de este componente: "))
                precio = float(input("Ingrese el precio unitario del componente: "))
                computadora.agregar_componente(ComponenteCPU(componente, marca, cantidad, precio))

            # Mostrar datos de la computadora y calcular precios
            print(f"Información de la computadora {computadora.marca} {computadora.modelo}:")
            for comp in computadora.componentes:
                print(f"Componente: {comp.componente}, Marca: {comp.marca}, Cantidad: {comp.cantidad}, Precio Unitario: ${comp.precio:.2f}, Costo Total: ${comp.costo_total():.2f}")

            costo_total = computadora.costo_total()
            precio_sugerido = computadora.precio_sugerido()
            print(f"Costo total de la computadora: ${costo_total:.2f}")
            print(f"Precio de venta sugerido: ${precio_sugerido:.2f}")

            # Preguntamos si desea cotizar otra computadora
            print("Desea cotizar una nueva computadora?")
            print("(1) SI")
            print("(2) NO")
            continuar = int(input())
            if continuar == 1:
                repetir = True
            else:
                repetir = False
                print("Finalizando programa.")
                break
                

# Ejecutar el método main si este archivo es el principal
if __name__ == "__main__":
    CostoComputadora.main()
