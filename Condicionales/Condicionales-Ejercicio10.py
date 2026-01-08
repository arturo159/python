tipo=input("Dime el tipo de pizza que quieres: ")
tipo = tipo.lower()
if tipo == "vegetariana":
    print ("Ingredientes vegetarianos: Pimiento y tofu")
    ingrediente=input ("Elija uno de los ingrdientes para su pizza: ")
    ingrediente=ingrediente.lower()
    if ingrediente=="pimiento" or ingrediente=="tofu":
        print("Su ingrediente ha sido elegido y su pizza se encuentra en preparación")
elif tipo == "no vegetariana":
    print ("Ingredientes no vegetarianos: Peperoni, Jamón y Salmón")
    ingrediente=input ("Elija uno de los ingrdientes para su pizza: ")
    ingrediente=ingrediente.lower()
    if ingrediente=="peperoni" or ingrediente=="jamón" or ingrediente=="salmón":
        print("Su ingrediente ha sido elegido y su pizza se encuentra en preparación")
else:
    print ("Las opciones son vegetariana o no vegeteriana")