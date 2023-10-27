def cuentAtras(num: int):
    i = num
    ser = "{i}, ".format(i = i)
    while(i > 1):
        i -= 1
        ser = ser + "{i}, ".format(i = i)
    ser = ser + "{fin}".format(fin = (i - 1))
    return ser

def main():
    numer = int(input("Dime un número entero positivo: "))
    print(cuentAtras(numer))
    
    
if __name__ == '__main__':
    main()