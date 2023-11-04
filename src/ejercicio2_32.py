"""
Ejercicio 2.2.22
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario
ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al
finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
"""

from ejercicio2_24 import recibNum


def totParImpar():
    num = recibNum()
    totPar = 0
    totImpar = 0
    while(num != 0):
        par = 0
        impar = 0
        while(num != 0):
            ultdig = num % 10
            if((ultdig % 2) == 0):
                par += 1
                totPar += 1
            else:
                impar += 1
                totImpar += 1
            num //= 10
        print("El número introducido tiene {par} dígitos pares y {impar} dígitos impares.".format(par = par, impar = impar))
        num = recibNum()
    print("Total de dígitos pares introducidos: {totPar}.".format(totPar = totPar))
    return "Total de dígitos impares introducidos: {totImpar}.".format(totImpar = totImpar)


def main():
    print(totParImpar())
    
    
if __name__ == '__main__':
    main()
            