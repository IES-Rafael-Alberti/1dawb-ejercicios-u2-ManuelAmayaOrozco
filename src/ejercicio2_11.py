"""
Ejercicio 2.2.1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""


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