def funcionFactorial(num):
    y = 1
    x = 0
    while x < num:
        y = y*(x+1)
        x = x + 1
    return y

print(funcionFactorial(4))