"""
Ejercicio 2.2.18
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de
los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar,
mostrar cuántos de los números ingresados por el usuario fueron números pares.
"""


from ejercicio2_24 import recibNum
from ejercicio2_27 import sumDigs


def repsumDigs(num: int):
    par = 0
    while(num != -1):
        print(sumDigs(num))
        if((num % 2) == 0):
            par += 1
        num = recibNum()
    return "El total de números pares es de {par}".format(par = par)


def main():
    number = int(input("Dime un número: "))
    print(repsumDigs(number))
    
    
if __name__ == '__main__':
    main()