class Nota:
    def __init__(self, Catedra, notaExamen):
        self.Catedra = Catedra
        self.notaExamen = notaExamen 

    def __repr__(self):
        return (f"Catedra = {self.Catedra}, Nota = {self.notaExamen} ")