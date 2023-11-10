"""
Ejercicio 2.1.1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""


def edad(ed: int):
    if (ed >= 18):
        return "Eres mayor de edad."
    else:
       return "No eres mayor de edad."


def main():
    años = int(input("Dime tu edad: "))
    print(edad(años))
    

if __name__ == '__main__':
     main()