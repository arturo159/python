estatura=input("Dime cuanto mides para calcular tu imc: ")
peso=input("Dime cuanto pesas para calcular tu imc: ")
imc=float(peso)/float(estatura)**2
print("Tu indice de masa corporal es  ", round(imc,2))