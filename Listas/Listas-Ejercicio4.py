lista = []
cont = 0
while cont < 6:
    lista.append(int(input("Dime un número ganador de la primitiva: ")))
    cont = cont + 1
lista.sort()
print(lista)