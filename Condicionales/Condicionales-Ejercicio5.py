edad=input("Dime tu edad: ")
ingresos=input("Dime tus ingresos: ")
if int(edad) > 16 and int(ingresos) > 1000:
    print("Puedes tributar")
else:
    print("No puedes tributar")