salida = "salir"
palabra = " "
while palabra != salida:
    palabra = input("Escribe palabras hasta que logres salir: ")
    if palabra == salida:
        break
    else:
        print(palabra)