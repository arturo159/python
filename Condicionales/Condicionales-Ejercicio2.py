contraseñaSistema="contraseña"
contraseña=input("Dime cuál es la contraseña: ")
if contraseña.casefold() == contraseñaSistema:
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")