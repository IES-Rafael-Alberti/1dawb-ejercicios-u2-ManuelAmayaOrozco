""" 
Ejercicio 2.1.5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad
y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""


def tributar(ed: int, din: int):
    if (ed < 16 or din < 1000):
        return "Usted no tiene que tributar."
    else:
        return "Usted tiene que tributar."
  
    
def main():
    edad = int(input("Dime tu edad: "))
    ing = int(input("Dime tus ingresos mensuales en euros: "))
    print(tributar(edad, ing))
   
    
if __name__ == '__main__':
     main()