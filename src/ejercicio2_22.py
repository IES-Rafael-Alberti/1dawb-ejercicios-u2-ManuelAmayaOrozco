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