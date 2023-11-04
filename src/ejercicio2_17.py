"""
Ejercicio 2.2.7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""


def tablasMultiplicar(number: int):
    for i in range(0, 10):
        res = number * i
        print("{number} x {i} = {res}".format(number = number, i = i, res = res))
    res = number * (i + 1)
    fin = "{number} x {dosi} = {res}".format(number = number, dosi = (i + 1), res = res)
    return fin


def main():
    num = int(input("Dime un número: "))
    print(tablasMultiplicar(num))
    
       
if __name__ == '__main__':
    main()