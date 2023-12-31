"""
Ejercicio 2.2.17
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo
componen.
"""


def sumDigs (num: int):
    sum = 0
    while(num != 0):
        dig = num % 10
        sum += dig
        num //= 10
    return "La suma de los dígitos es {sum}".format(sum = sum)


def main():
    number = int(input("Dime un número: "))
    print(sumDigs(number))
    
    
if __name__ == '__main__':
    main()