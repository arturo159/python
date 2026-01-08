longitud= input("Dime la altura del triángulo: ")
for i in range(int(longitud)):
    for j in range(i+1):
        print("*", end="")
    print("")