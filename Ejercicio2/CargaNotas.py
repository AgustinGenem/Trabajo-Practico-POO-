from alumno import Alumno
from nota import Nota

class CargaNotas:
    def __init__(self):
        self.alumnos = []

    def cargar_alumnos(self):
        while True:
            nombreCompleto = input("Ingrese el nombre completo del alumno (o 'FIN' para terminar): ")
            if nombreCompleto == "FIN":
                break
            legajo = int(input("Ingrese el legajo del alumno: "))
            alumno = Alumno(nombreCompleto, legajo)
            self.cargar_notas(alumno)
            self.alumnos.append(alumno)

    def cargar_notas(self, alumno):
        while True:
            catedra = input("Ingrese la catedra (o 'FIN' para terminar): ")
            if catedra == "FIN":
                if not alumno.notas:
                    print("Debe ingresar al menos una nota.")
                    continue
                break
            notaExamen = float(input("Ingrese la nota del examen: "))
            nota = Nota(catedra, notaExamen)
            alumno.AgregarNotas(nota)

    def mostrar_informacion(self):
        for alumno in self.alumnos:
            print(alumno)

    def main(self):
        self.cargar_alumnos()
        self.mostrar_informacion()

if __name__ == "__main__":
    carga_notas = CargaNotas()
    carga_notas.main()
