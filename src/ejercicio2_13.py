"""
Ejercicio 2.2.3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos
los números impares desde 1 hasta ese número separados por comas.
"""


def cuentImpar(num: int):
    i = 1
    ser = "{i}, ".format(i = i)
    if((num % 2) == 0):
        while(i < (num - 3)):
            i += 2
            ser = ser + "{i}, ".format(i = i)
        ser = ser + "{fin}".format(fin = (num - 1))
        return ser
    else:
        while(i < (num - 2)):
            i += 2
            ser = ser + "{i}, ".format(i = i)
        ser = ser + "{fin}".format(fin = num)
        return ser


def main():
    numer = int(input("Dime un número entero positivo: "))
    print(cuentImpar(numer))
    
    
if __name__ == '__main__':
    main()