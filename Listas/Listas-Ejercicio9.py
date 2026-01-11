palabra = input("Dime una palabra: ")
vocales = ["a", "e", "i", "o", "u"]
for i in vocales:
    cont = 0
    for j in palabra:
        if j == i:
            cont = cont + 1
    print("La palabra contiene", cont, "veces la vocal", i)