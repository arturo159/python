dic = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Dime cual es la divisa: ")
if divisa in dic:
    print (dic[divisa])
else:
    print("No se encuentra la divisa")