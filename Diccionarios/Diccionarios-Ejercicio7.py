dicCesta = {}
opcion = 2

while opcion != 0:
    print("0. Salir")
    print("1. Añadir a la cesta")
    opcion = int(input("Elige lo que quieres hacer: "))
    if opcion == 0:
        print("Lista de la compra:")
        precio = 0
        for i in dicCesta:
            precio = precio + dicCesta[i]
            print(i, "              ", dicCesta[i])
        print ("Total                ", precio)
    elif opcion == 1:
        articulo = input("Dime que articulo deseas comprar: ")
        precio = float(input("Dime cuanto cuesta dicho artículo: "))
        dicCesta[articulo] = precio
    else:
        print("Esta opción no existe" )