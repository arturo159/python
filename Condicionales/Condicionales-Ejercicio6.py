name=input("Dime tu nombre: ")
sex=input("Dime tu sexo: ")
if sex == "hombre" and name < "N" or sex == "mujer" and name < "M":
    print ("Correspondes al grupo A")
else:
    print("Correspondes al grupo B")
