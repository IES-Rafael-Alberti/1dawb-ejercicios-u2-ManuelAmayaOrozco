"""
Ejercicio 2.2.25
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso
de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará
como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
"""


def longestWord():
    phrase = enterPhrase()
    phrase = phrase.strip()
    wordcount = 0
    lenglongestword = 0
    while (len(phrase) != 0):
        wordcount += 1
        cont = phrase.find(" ")
        if (cont != -1):
            word = phrase[0:cont]
            while (cont < len(phrase) and phrase[cont] == " "):
                cont += 1
            phrase = phrase[cont:]
        else:
            word = phrase
            phrase = ""
        if (len(word) > lenglongestword):
            lenglongestword = len(word)
            longestword = word
    if (wordcount > 0):
        print("La palabra más larga es '{longestword}'.".format(longestword = longestword))
    return "La cantidad de palabras es de {wordcount}.".format(wordcount = wordcount)


def enterPhrase():
    phrase = input("Introduce una frase: ")
    return phrase


def main():
    print(longestWord())
    
    
if __name__ == '__main__':
    main()