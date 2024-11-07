def PedirGolosina(golosinas, Empleados,GolosinasPedidas):
    con = input("Ingrese su clave: ")
    if con in Empleados:
        clavegolosina = int(input("ingrese el codigo de la golosina: "))
        for golosina in golosinas:
            if golosina[0] == clavegolosina:
                if golosina[2]==0:
                    print("Lo sentimos, no hay stock")
                    return
                else:
                    golosina[2]-=1
                    for pedido in GolosinasPedidas:
                        if pedido[0] == clavegolosina:
                            pedido[2] += 1
                            break
                    else:
                        GolosinasPedidas.append([clavegolosina, golosina[1],1])
                    print(f"usted pidio {golosina[1]}")
                    return
    else:
        print("Usted no es empleado")  

    return

def MostrasGolosinas(golosinas):
    print("Golosinas disponibles:")
    for golosina in golosinas:
        print(f"Código: {golosina[0]}, Nombre: {golosina[1]}, Stock: {golosina[2]}")
    return

def RellenarGolosinas(golosina,ClavesTecnico):
    clave1 = input("Ingrese la primera clave: ")
    clave2 = input("Ingrese la segunda clave: ")
    clave3 = input("Ingrese la tercera clave: ")
    if (clave1, clave2, clave3) != ClavesTecnico:
        print("No tiene permiso para ejecutar la funcion de recarga")
        return

    codigo = int(input("Ingrese el código de la golosina: "))
    cantidad = int(input("Ingrese la cantidad a recargar: "))
    if cantidad <= 0:
        print("La cantidad debe ser mayor a cero")
        return

    for golosina in golosinas:
        if golosina[0] == codigo:
            golosina[2] += cantidad
            print(f"Se ha recargado {cantidad} unidades de {golosina[1]}")
            return
    print("Código de golosina inválido")

def ApagarMaquina(GolosinasPedidas):
    print("Golosinas Pedidas:")
    for golosina in GolosinasPedidas:
        print(f"Código: {golosina[0]}, Nombre: {golosina[1]}, Pedidos: {golosina[2]}")
    return

golosinas = [
             [1,"KitKat",20,],
             [2,"Chicles",50,],
             [3,"Caramelos de menta",50,],
             [4,"Huevo Kinder",10,],
             [5,"Chetoos",10,],
             [6,"Twix",10,],
             [7,"M&M'S",10,],
             [8,"Papas Lays",2,],
             [9,"Milkybar",10,],
             [10,"Alfajor Tofi",15,],
             [11,"Lata Coca",20,],
             [12,"Chitos",10,],]

Empleados = {"1100": "José Alonso",
            "1200": "Federico Pacheco",
            "1300": "Nelson Pereyra",
            "1400": "Osvaldo Tejada",
            "1500": "Gastón García"}

ClavesTecnico = ("admin","CCCDDD","2020")

GolosinasPedidas = []
while True:
    print("Menu: ")
    print("1-Pedir Golosinas/2-Mostrar Golosinas/3-RellenarGolosinas/4-ApagarMaquina")
    opc = int(input("eliga una opcion "))
    if opc == 1:
        PedirGolosina(golosinas, Empleados,GolosinasPedidas)
    if opc == 2:
        MostrasGolosinas(golosinas)
    if opc == 3:
        RellenarGolosinas(golosinas, ClavesTecnico)
    if opc == 4:
        ApagarMaquina(GolosinasPedidas)
        break
     
