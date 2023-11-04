"""
Ejercicio 2.2.8
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""


def piramNum (num: int):
    cont = 1
    while (num > 1):
        cont += 2
        num -=1
    for i in range(1, cont + 1, 2):
        print("")
        for j in range(i, 0, -2):
            print("{j} ".format(j = j), end = "")
    return ""
        
    
def main():
    numer = int(input("Dime un número: "))
    print(piramNum(numer))
    

if __name__ == '__main__':
    main()