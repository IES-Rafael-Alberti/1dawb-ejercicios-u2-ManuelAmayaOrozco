"""
Ejercicio 2.2.12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el número de veces que aparece la letra en la frase.
"""


def cuentaLetra(phrase: str, letter: str):
    cont = 0
    tot = 0
    while(cont < len(phrase)):
        if(phrase[cont] == letter):
            tot += 1
        cont += 1
    fin = "La letra se repite {tot} veces.".format(tot = tot)
    return fin


def main():
    frase = input("Dime una palabra o frase: ")
    letra = input("Dime una letra a contar en la palabra/frase: ")
    print(cuentaLetra(frase, letra))
    

if __name__ == '__main__':
    main()