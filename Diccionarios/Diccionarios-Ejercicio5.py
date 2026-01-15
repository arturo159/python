dicAsignaturas = {
    'Mátematicas':6, 
    'Física':4, 
    'Química':5, 
    }
cont = 0

for i in dicAsignaturas:
    print(i, "tiene", dicAsignaturas[i], "créditos")
    cont = cont +  dicAsignaturas[i]
print ("El total de créditos son:", cont)