"""
Ejercicio 2.2.6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****
"""


def asterTriangulo(num: int):
    for i in range(1, num):
        print("*" * i)
    fin = ("*" * num)
    return fin


def main():
    number = int(input("Dime un número: "))
    print(asterTriangulo(number))
    
    
if __name__ == '__main__':
    main()