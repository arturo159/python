dicFacturas = {}
options = 0
cobrado = 0
pendiente = 0
while options != 4:
    #Menú
    print("Dinero cobrado:", cobrado, "€")
    print("Pendiente de cobrar: ", pendiente)
    print("Menú de opciones: ")
    print("1. Añadir una nueva factura")
    print("2. Pagar factura")
    print("3. Salir")
    options = int(input("Elige la opción que vas a usar: "))
    #Opciones
    if options == 1:
        numFactura = input("Introduce el número de la factura: ")
        coste = int(input("Introduce su costo: "))
        dicFacturas[numFactura] = coste
        pendiente = pendiente + coste
        print(" ")
    elif options == 2:
        numFactura = input("Introduce el número de la factura: ")
        if numFactura in dicFacturas:
            coste = dicFacturas[numFactura]
            del dicFacturas[numFactura]
        else:
            print("No se ha encontrado la factura")
            coste = 0
        cobrado = cobrado + coste
        pendiente = pendiente - coste
        print(" ")
    elif options == 3:
        print("Gracias por usar nuestra aplicación")
        options = 4
    else:
        print("La opción no se encuentra en el menú")
        print(" ")