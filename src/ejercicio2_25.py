"""
Ejercicio 2.2.15
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la
sumatoria de todos los números positivos ingresados.
"""


from ejercicio2_24 import recibNum


def sumatorNumPos(num: int):
    sum = 0
    while(num != 0):
        if(num > 0):
            sum += num
        num = recibNum()
    return "La suma final es {sum}".format(sum = sum)


def main():
    number = int(input("Dime un número: "))
    print(sumatorNumPos(number))
    
    
if __name__ == '__main__':
    main()