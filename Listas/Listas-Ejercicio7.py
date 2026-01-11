abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
sacar = []
for posicion, letra in enumerate(abecedario):
    if posicion == 0:
        continue
    elif posicion % 3 == 0:
        sacar.append(letra)
for i in sacar:
    abecedario.remove(i)
print (abecedario)