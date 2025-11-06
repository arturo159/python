puntuacion = float(input("Dime la puntuación del empleado: "))
cantDinero = 2400
if puntuacion == 0:
    print ("El nivel de rendimiento de este empleado es Inaceptable")
    print ("Y este empleado recibirá", cantDinero, "euros")
elif puntuacion == 0.4:
    print ("El nivel de rendimiento de este empleado es Aceptable")
    aumento = cantDinero * 0.4
    cantDinero = cantDinero + aumento
    print ("Y este empleado recibirá", cantDinero, "euros")
elif puntuacion == 0.6:
    print ("El nivel de rendimiento de este empleado es Meritorio")
    aumento = cantDinero * 0.6
    cantDinero = cantDinero + aumento
    print ("Y este empleado recibirá", cantDinero, "euros")
else:
    print ("Esta puntuación no se encuentra en la base de datos")