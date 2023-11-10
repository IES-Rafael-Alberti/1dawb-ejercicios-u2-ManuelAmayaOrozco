"""
Ejercicio 2.2.20
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase).
Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no
coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar.
Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
"""


def searchPhrase(phrase: str, letter: str):
    cont = 0
    while(cont != len(phrase)):
        if(letter != phrase[cont]):
            print("No hay coincidencia en la posición {cont}.".format(cont = cont))
            cont += 1
        else:
            return "Se encontró coincidencia en la posición {cont}.".format(cont = cont)
    return "No se encontraron coincidencias en la frase."


def main():
    phrase = input("Dime una frase: ")
    letter = input("Dime una letra para buscar en la frase: ")
    print(searchPhrase(phrase, letter))
    
    
if __name__ == '__main__':
    main()