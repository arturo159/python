list = []
cont = 0
while cont < 6:
    list.append(int(input("Dime un número ganador de la primitiva: ")))
    cont = cont + 1
list.sort()
print(list)