precioInicial=3.49
ventas=input("Dime la cantidad de barras de pan que no son del día vendidas: ")
porcentaje=(float(precioInicial)*60)/100
precioPasado=float(precioInicial)-float(porcentaje)
ganancias=float(precioPasado)*int(ventas)
print("Precio de barras de pan frescas: ", precioInicial)
print("Precio de barras de pan: ", round(precioPasado, 2))
print("Hoy las ganancias solo de las barras de pan son de: ", round(ganancias, 2))