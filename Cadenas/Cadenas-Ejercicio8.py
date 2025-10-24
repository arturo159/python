precio=input("Dime el precio de tu producto con los centimos incluidos: ")
precio=precio.replace(".", ",")
euros=precio.split(",")[0]
centimos=precio.split(",")[1]
print("Tu producto vale", euros, " euros y", centimos, "céntimos")