""" 
Ejercicio 2.1.7
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
Renta                     Tipo impositivo
Menos de 10000€           5%
Entre 10000€ y 20000€     15%
Entre 20000€ y 35000€     20%
Entre 35000€ y 60000€     30%
Más de 60000€             45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""


def renta(din: int):
    if(din < 10000):
        return "Tu tipo impositivo es del 5%."
    elif(10000 <= din < 20000):
        return "Tu tipo impositivo es del 15%."
    elif(20000 <= din < 35000):
        return "Tu tipo impositivo es del 20%."
    elif(35000 <= din < 60000):
        return "Tu tipo impositivo es del 30%."
    else:
        return "Tu tipo impositivo es del 45%."
    
    
def main():
    dinren = int(input("¿Cuánto pagas por tu renta (en euros)?: "))
    print(renta(dinren))
    
    
if __name__ == '__main__':
    main()