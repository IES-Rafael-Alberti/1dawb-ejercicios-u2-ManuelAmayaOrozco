def repPalabra(word: str):
    i = 0
    while(i < 9):
        print(word)
        i += 1
    return word
   
def main():    
    pal = input("Dime una palabra: ")
    print(repPalabra(pal))
    if __name__ == '__main__':
        main()