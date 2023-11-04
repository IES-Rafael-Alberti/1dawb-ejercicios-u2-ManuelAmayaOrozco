"""
Ejercicio 2.2.11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las
letras de la palabra introducida empezando por la última.
"""


def letraPalab (word: str):
    cont = (len(word) - 1)
    while(cont >= 0):
        print(word[cont])
        cont -= 1
    return ""


def main():
    palab = input("Dime una palabra: ")
    print(letraPalab(palab))
    
    
if __name__ == '__main__':
    main()