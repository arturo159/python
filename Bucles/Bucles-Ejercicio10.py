num = input("Introduce un número entero mayor que 2: ")
x = 2
if int(num) > 2:
    while int(num) % x != 0:
        x += 1
    if x == int(num):
        print(num, "es primo")
    else:
        print(num, "no es primo")
else:
    print("Este número no es mayor que 2")