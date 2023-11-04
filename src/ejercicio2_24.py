"""
Ejercicio 2.2.14
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la
sumatoria de todos los números ingresados.
"""


def sumatorNum(num: int):
    sum = 0
    while(num != 0):
        sum += num
        num = recibNum()
    return "La suma final es {sum}".format(sum = sum)


def recibNum():
    num = int(input("Dime un número: "))
    return num


def main():
    number = int(input("Dime un número: "))
    print(sumatorNum(number))
    
    
if __name__ == '__main__':
    main()