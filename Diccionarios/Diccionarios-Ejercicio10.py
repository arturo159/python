dicCliente = {}
option = 0
while option != 7:
    #Menú
    print("Menú de opciones: ")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar clientes")
    print("5. Listar clientes preferentes")
    print("6. Salir")
    option = int(input("Elige la opción que vaya a usar: "))
    #Opciones
    if option == 1:
        nif = input("Introduce NIF del cliente: ")
        nombre = input("Introduce el nombre del cliente: ")
        direccion = input("Introduce la dirección del cliente: ")
        telefono = input("Introduce el teléfono del cliente: ")
        email = input("Introduce el correo electrónico del cliente: ")
        preferencia = input("Introduce si es un cliente preferente (S/N): ")
        dicDatos = {
            "nombre":nombre,
            "dirección":direccion,
            "teléfono":telefono,
            "email":email,
            "preferente":preferencia=="S"
        }
        dicCliente[nif] = dicDatos
        print (dicDatos)
        print (dicCliente)
    elif option == 2:
        nif = input("Introduce el NIF del cliente: ")
        if nif in dicCliente:
            del dicCliente[nif]
        else:
            print("No existe ningún cliente con el NIF", nif)
    elif option == 3:
        nif = input("Introduce el NIF del cliente: ")
        if nif in dicCliente:
            cliente = dicCliente[nif]
            print("NIF:", nif)
            print("Nombre:", cliente["nombre"])
            print("Dirección:", cliente["direccion"])
            print("Teléfono:", cliente["telefono"])
            print("Correo:", cliente["correo"])
            print("Preferente:", cliente["preferente"])
        else:
            print("El cliente no existe.")
    elif option == 4:
        if not dicCliente:
            print("No hay clientes registrados.")
        else:
            for nif, datos in dicCliente.items():
                print("NIF:", nif, "- Nombre:", datos["nombre"])
    elif option == 5:
        preferencia = False
        for nif, datos in dicCliente.items():
            if datos["preferente"]:
                print("NIF:", nif, "- Nombre:", datos["nombre"])
                preferencia = True
        if not preferencia:
            print("No hay clientes preferentes.")
    elif option == 6:
        print("Gracias por usar nuestra aplicación")
        option = 7
    else:
        print("Esa opción no se encuentra dentro del menú")
