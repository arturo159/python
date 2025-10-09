dinero=input("Dime la cantidad de dinero depositada en la cuenta: ")
interés=(int(dinero)*4)/100
año1=int(dinero)+int(interés)
año2=int(dinero)+(int(interés)*2)
año3=int(dinero)+(int(interés)*3)
print("El primer año tendrás ", año1, " el segundo ", año2, " y el tercero ", año3)