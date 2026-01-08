alt= input("Dime un número positivo para crear el triángulo: ")
for i in range(1, int(alt)+1, 2):
    for j in range(i, 0, -2):
        print(j, end="")
    print("")