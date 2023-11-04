"""
Ejercicio 2.2.16
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el
mayor número ingresado.
"""


from ejercicio2_24 import recibNum


def mayorNum(num: int):
    mayor = num
    while(num != 0):
        if(num > mayor):
            mayor = num
        num = recibNum()
    return "El mayor número introducido es {mayor}".format(mayor = mayor)


def main():
    number = int(input("Dime un número: "))
    print(mayorNum(number))
    
    
if __name__ == '__main__':
    main()