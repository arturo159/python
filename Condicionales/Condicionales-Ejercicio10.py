tipo=input("Dime el tipo de pizza que quieres: ")
tipo = tipo.lower()
if tipo == "vegetariana":
    print ("Ingredientes vegetarianos: Pimiento y tofu")
elif tipo == "no vegetariana":
    print ("Ingredientes no vegetarianos: Peperoni, Jamón y Salmón")
else:
    print ("Las opciones son vegetariana o no vegeteriana")