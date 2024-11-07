detallesFactura = [
    ["Código artículo", "NombreArtículo", "Cantidad", "PrecioUnitario", "Subtotal"]
]

listaArticulos = [
    [101, "Leche", 250],
    [102, "Gaseosa", 300],
    [103, "Fideos", 150],
    [104, "Arroz", 280],
    [105, "Vino", 1200],
    [106, "Manteca", 200],
    [107, "Lavandina", 180],
    [108, "Detergente", 460],
    [109, "Jabón en polvo", 960],
    [110, "Galletas", 600]
]

diccionarioClientes = {
    "20110425417": "Rodolfo Fernández",
    "30527419656": "Los Pollos Hnos",
    "27289425478": "Andrea Pereira",
    "33536549878": "Multimarca Repuestos",
    "20291122568": "Luis Peric"
}

def verificarCuit(cuit):
    global clienteFactura
    if cuit in diccionarioClientes:
        clienteFactura = diccionarioClientes[cuit]
    else:
        clienteFactura = "Consumidor Final"

def buscarCodigo(codigoArticulo):
    for articulo in listaArticulos:
        if articulo[0] == codigoArticulo:
            return True
    return False

def cargarDetallesFactura(codigoArticulo, cantidadArticulo, listaArticulos, detallesFactura):
    fila = []
    subtotal = 0
    fila.append(codigoArticulo)
    for element in listaArticulos:
        if element[0] == codigoArticulo:
            fila.append(element[1])
            fila.append(cantidadArticulo)
            fila.append(element[2])
            subtotal = cantidadArticulo * element[2]
            fila.append(subtotal)
            break
    detallesFactura.append(fila)

def calcularTotal(detallesFactura):
    total = 0
    for element in detallesFactura[1:]:  # Ignorar la primera fila de encabezado
        total += element[4]
    return total

fechaFactura = ""
numeroFactura = 0
letraFactura = ""
totalFactura = 0
montoIva = 0
clienteFactura = ""

fechaFactura = input("Ingrese la fecha de factura: ")
numeroFactura = input("Ingrese el número de factura: ")

cuit = input("Ingrese su cuit: ")
verificarCuit(cuit)
codigoCorrecto = False
while not codigoCorrecto:
    codigoArticulo = int(input("Ingrese el código de artículo a facturar (0000 para terminar): "))
    if codigoArticulo == 0:
        codigoCorrecto = True
    else:
        if buscarCodigo(codigoArticulo):
            cantidadArticulo = int(input("Ingrese la cantidad de artículos a facturar: "))
            cargarDetallesFactura(codigoArticulo, cantidadArticulo, listaArticulos, detallesFactura)
        else:
            print("Código incorrecto")

total = calcularTotal(detallesFactura)

if str(cuit).startswith('20') or str(cuit).startswith('27') or clienteFactura == "Consumidor Final":
    montoIva = 0
    letraFactura = "B"
elif str(cuit).startswith('30') or str(cuit).startswith('33'):
    montoIva = 1.21
    letraFactura = "A"

if letraFactura == "A":
    totalFactura = total * montoIva
elif letraFactura == "B":
    totalFactura = total

print(f"Fecha Factura:                    {fechaFactura}")
print(f"Número:                           {numeroFactura}")
print(f"Letra:                            {letraFactura}")
print(f"Cliente:                          {clienteFactura}")
for element in detallesFactura[1:]:  # Ignorar la primera fila de encabezado
    print(element)
print(f"                                   IVA: {montoIva}")
print(f"                                   Total: {totalFactura}")





