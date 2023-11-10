"""
Ejercicio 2.2.24
Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores
que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
"""

from ejercicio2_24 import recibNum
from ejercicio2_20 import numPrimo


def numPrimoCounter():
    totPrimo = 0
    num = recibNum()
    while (num != 0):
        if (num < 0):
            print("Número no válido, vuelve a intentarlo.")
        else:
            primo = numPrimo(num)
            if (primo == True):
                totPrimo += 1
        num = recibNum()
    return "La cantidad total de números primos ingresados es de {totPrimo}.".format(totPrimo = totPrimo)


def main():
    print(numPrimoCounter())
    

if __name__ == '__main__':
    main()