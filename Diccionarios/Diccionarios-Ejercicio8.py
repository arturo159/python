dicTraduccion = {}
listaPalabras = input("Introduce una lista de plabras con sus respectivas traducciones en formato palabra:traducción y que estén separadas por comas: ")
palabras1 = listaPalabras.split(",")
for i in palabras1:
    palabra, traduccion = i.split(":")
    dicTraduccion[palabra] = traduccion
frase = input("Introduce una frase en español:")
palabras2 = frase.split()
for i in palabras2:
    if i in dicTraduccion:
        print(dicTraduccion[i], end=' ')
    else:
        print(i, end=' ')