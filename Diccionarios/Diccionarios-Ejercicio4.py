date = input("Dime la fecha del día de hoy en formato dd/mm/aaaa: ")
date = date.split("/")

dicfecha = {
    'Día':date[0], 
    'Mes':date[1], 
    'Año':date[2], 
    }
dicmeses = {
    '01':'Enero',
    '02':'Febrero',
    '03':'Marzo',
    '04':'Abril',
    '05':'Mayo',
    '06':'Junio',
    '07':'Julio',
    '08':'Agosto',
    '09':'Septiembre',
    '10':'Octubre',
    '11':'Noviembre',
    '12':'Diciembre'
}

print(dicfecha['Día'], "de", dicmeses[dicfecha['Mes']], "de", dicfecha['Año'])