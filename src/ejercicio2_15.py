"""
Ejercicio 2.2.5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número
de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
# Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
"""


def capital(amount: int, interest: int, year: int):
    while(year > 0):
        amount *= 1 + interest / 100
        year -= 1
    return amount


def main():
    cant = int(input("Dime la cantidad a invertir: "))
    inter = int(input("Dime el interés anual: "))
    ano = int(input("Dime el número de años: "))
    print(capital(cant, inter, ano))
    
    
if __name__ == '__main__':
    main()