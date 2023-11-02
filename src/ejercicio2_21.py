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