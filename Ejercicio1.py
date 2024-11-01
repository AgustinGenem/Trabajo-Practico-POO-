class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
    def __repr__(self):
        return (f"Celda (Fila: {self.fila} Columna: {self.columna} Valor: {self.valor})")

class Matriz:
    def __init__(self):
        self.celdasMatriz = []
    
    def agregarCelda(self, celda):
        for i in self.celdasMatriz:
            if i.fila == celda.fila and i.columna == celda.columna:
                print("La celda ya se encuentra en la matriz")
                return
        self.celdasMatriz.append(celda)

    def obtenerValor(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y columna indicada no fue asignada en ninguna celda"
    
    def mostrarCelda(self):
        for celda in self.celdasMatriz:
            print(celda)

def main(): 
    matriz = Matriz()

    while True:
        fila_input = (input("Ingrese la fila (ingrese 'FIN' para terminar): "))
        if fila_input == "FIN":
            break
        fila = int(fila_input)
        columna = int(input("Ingrese la columna: "))
        valor = input ("Ingrese el valor:  ")

        
            
        celda = Celda(fila, columna, valor)
        matriz.agregarCelda(celda)

    print("\n Valores cargados: ")
    matriz.mostrarCelda()

    fila = int(input("\nIngrese la fila para buscar el valor: "))
    columna = int(input("Ingrese la columna para buscar el valor: "))
    valor = matriz.obtenerValor(fila, columna)
    print(f"Valor en la celda ({fila}, {columna}): {valor}")

if __name__ == "__main__":
    main()

        
