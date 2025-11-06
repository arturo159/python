edad=int(input ("Dime tu edad: "))
if edad > 0 and edad < 4:
    print ("La entrada es gratis")
elif edad > 4 and edad < 18:
    print("La entrada cuesta 5 euros")
elif edad > 18:
    print("La entrada cuesta 10 euros")
else:
    print("No hay edades negativas")