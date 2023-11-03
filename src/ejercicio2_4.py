""" 
Ejercicio 2.1.4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o
impar.
"""


def paridad(n: int):
    res = n % 2
    if(res == 0):
        return "El número es par."
    else:
        return "El número es impar."
 
    
def main():    
    num = int(input("Dime un número: "))
    print(paridad(num))
  
    
if __name__ == '__main__':
     main()