palabra = input("Dime una palabra: ")
lista = list(palabra)
listaInversa = list(palabra)
listaInversa.reverse()
if lista == listaInversa:
    print("Esta palabra es un palíndromo")
else:
    print("Esta palabra no es un palíndromo")