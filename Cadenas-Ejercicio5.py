frase=input("Dime una frase para invertir: ")
#Frase invertida usando una técnica de Slicing
fraseInvertida=frase[::-1]
print(fraseInvertida)
#Frase invertida usando un String Method
print("".join(reversed(frase)))