frase = input("Dime una frase: ")
letra = input("Dime una letra: ")
cont = 0
for i in frase:
    if i == letra:
        cont =cont + 1
print("La letra aparece", cont, "veces")