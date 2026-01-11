lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.reverse()
for i in lista:
    if i == lista[-1]:
        print(i, end="")
    else:
        print(i, end=", ")