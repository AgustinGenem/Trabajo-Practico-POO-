class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombre = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def AgregarNotas(self, Nota):
        self.notas.append(Nota)
    
    def CalcularPromedio(self):
        if not self.notas:
            return 0
        
        total = sum(nota.notaExamen for nota in self.notas)
        return total / len(self.notas)
    
    def __repr__(self):
        return (f"\n Nombre: {self.nombre}, \n Legajo: {self.legajo}, \n Nota: {self.notas}, \n Promedio = {self.CalcularPromedio()}")

