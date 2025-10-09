pesoMuñecas=75
pesoPayasos=112
numMuñecas=input("Dime el número de muñecas que se han vendido: ")
numPayasos=input("Dime el número de payasos que se han vendido: ")
pesoVenta=(int(pesoMuñecas)*int(numMuñecas))+(int(pesoPayasos)*int(numPayasos))
print("El peso de tu pedido es de: ", pesoVenta, "g")