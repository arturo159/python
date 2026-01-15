dicAsignaturas = {
    'nombre': '',
    'edad': '',
    'sexo': '',
    'telefono': '',
    'correo': ''
    }

for i in dicAsignaturas:
    variable = input("Dime tu %s: " %i)
    dicAsignaturas[i] = variable
    print (dicAsignaturas)