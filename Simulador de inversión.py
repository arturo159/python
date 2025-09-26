capital=input("Dime cuanto quieres invertir para decirte las ganancias: ")
tasaIntereses=input("Dime cuantos intereses hay actualmente para calcular las ganancias: ")
tiempo=input("Dime cuantos años quieres pasar invirtiendo: ")
porcentaje=capital*tasaIntereses/100
intereses=int(capital)*int(tiempo)*porcentaje
print("Tus ganancias serán  ", intereses)