dicFacturas = {}
options = 0
cobrado = 0
pendiente = 0
while options != 3:
    if options == 1:
        numFactura = input("Introduce el número de la factura: ")
        coste = int(input("Introduce su costo: "))
        dicFacturas[numFactura] = coste
        pendiente = pendiente + coste
    elif options == 2:
        numFactura = input("Introduce el número de la factura: ")
        coste = dicFacturas.pop(numFactura, 0)
        cobrado = cobrado + coste
        pendiente = pendiente - coste
    print("Dinero cobrado:", cobrado, "€")
    print('Pendiente de cobrar: ', pendiente)
    options = input("Introduce si quieres añadir una nueva factura (1), pagarla (2) o terminar (3): ")