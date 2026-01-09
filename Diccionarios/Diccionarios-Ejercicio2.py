nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
direccion = input("Dime tu dirección: ")
tlf = input("Dime tu número de teléfono: ")

dic = {
    'Nombre':nombre, 
    'Edad':edad, 
    'Dirección':direccion, 
    'Teléfono':tlf
    }

print(dic['Nombre'], "tiene", dic['Edad'], "años, vive en", dic['Dirección'], "y su número de teléfono es", dic['Teléfono'])