asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for i in asignaturas:
    nota = input("Dime que nota has sacado en " + i + ": ")
    if int(nota) >= 5:
        notas.append(i)
for i in notas:
    asignaturas.remove(i)
print("Tienes que recuperar ", asignaturas)