from Barrio import Barrio
from Vivienda import Vivienda
from Habitacion import Habitacion

def main():

    barrio = Barrio("Barrio Los Olivos", "Constructora ABC")

  
    vivienda1 = Vivienda("Avenida Siempreviva", 123, "A", 1, 150.0)
    vivienda1.agregar_habitacion(Habitacion("Sala", 20.5))
    vivienda1.agregar_habitacion(Habitacion("Cocina", 15.0))
    vivienda1.agregar_habitacion(Habitacion("Dormitorio Principal", 30.0))

    vivienda2 = Vivienda("Calle Falsa", 456, "B", 2, 200.0)
    vivienda2.agregar_habitacion(Habitacion("Sala", 25.5))
    vivienda2.agregar_habitacion(Habitacion("Cocina", 18.0))
    vivienda2.agregar_habitacion(Habitacion("Dormitorio", 35.0))

   
    barrio.agregar_vivienda(vivienda1)
    barrio.agregar_vivienda(vivienda2)

  
    print(barrio)

  
    print(f"\nSuperficie total de terreno del barrio: {barrio.getSuperficieTotalTerreno()} m²")

   
    print(f"Superficie total de terreno en la manzana 'A': {barrio.getSuperficieTotalTerrenoXManzana('A')} m²")

    
    print(f"Superficie total cubierta del barrio: {barrio.getSuperficieTotalCubierta()} m²")

if __name__ == "__main__":
    main()
