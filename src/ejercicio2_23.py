"""
Ejercicio 2.2.13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el
usuario escriba “salir” que terminará.
"""

def echoPhrase(phrase: str):
    sent = phrase
    while (phrase != "salir"):
        phrase = recibPhrase()
        sent += "\n{phrase}".format(phrase = phrase)
        print(sent)
    return ""


def recibPhrase():
    recib = input("Dime una palabra o frase: ")
    return recib


def main():
    phras = input("Dime una palabra o frase: ")
    print(echoPhrase(phras))
    
    
if __name__ == '__main__':
    main()