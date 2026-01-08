cantDinero=input("Dime la cantidad de dinero que quieres invertir: ")
intAnual=input("Dime cuál es el interés anual: ")
numAños=input("Dime cuantos años pretendes invertir tu dinero: ")
for i in range(int(numAños)):
    cantDinero = int(cantDinero) * (1 + int(intAnual)/100)
    print("El capital tras ", str(i+1), "es de ", cantDinero)