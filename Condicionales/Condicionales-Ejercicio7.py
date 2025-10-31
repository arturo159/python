renta=input("Dime tu renta: ")
if int(renta) <= 10000:
    print ("Tipo de impositivo equivalente al 5%")
elif int(renta) > 10000 and int(renta) < 20000:
    print ("Tipo de impositivo equivalente al 15%")
elif int(renta) >= 20000 and int(renta) < 35000:
    print ("Tipo de impositivo equivalente al 20%")
elif int(renta) >= 35000 and int(renta) <= 60000:
    print ("Tipo de impositivo equivalente al 30%")
elif int(renta) > 60000:
    print ("Tipo de impositivo equivalente al 45%")