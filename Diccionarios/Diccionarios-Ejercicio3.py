dic = {
    'Plátano':1.35, 
    'Manzana':0.80, 
    'Pera':0.85, 
    'Naranja':0.70
    }

fruta = input("Fruta a elegir: ")
kilos = input("Número de kilos: ")

if fruta in dic:
    precio = dic[fruta] * int(kilos)
    print("El precio de", kilos, "kilos de", dic[fruta], "es", precio)
else:
    print("Esa fruta no se encuentra en nuestra frutería")