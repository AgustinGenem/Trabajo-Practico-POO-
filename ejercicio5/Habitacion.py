class Habitacion:
    def __init__(self, nombre: str, metrosCuadrados: float):
        self.nombre = nombre
        self.metrosCuadrados = metrosCuadrados

    def __str__(self):
        return f"Habitación: {self.nombre}, Metros Cuadrados: {self.metrosCuadrados}"
