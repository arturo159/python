nacimiento=input("Dime el día de tu decha de nacimiento en formato dd/mm/aaaa: ")
dia=nacimiento.split("/")[0].zfill(2)
mes=nacimiento.split("/")[1].zfill(2)
ano=nacimiento.split("/")[2]
print("Tú naciste el día", dia, "del mes", mes, "del año", ano)