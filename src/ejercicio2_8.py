""" 
Ejercicio 2.1.8
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos
que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose
en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6
o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una
tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en
cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
Nivel          Puntución
Inaceptable    0.0
Aceptable      0.4
Meritorio      0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así
como la cantidad de dinero que recibirá el usuario.
"""


def rendimiento(niv: float):
    din = 2400 * niv
    if(niv <= 0.3 ):
        print("Nivel inaceptable, recibirá una paga de {din}€.".format(din = din))
        return din
    elif(0.4 <= niv <= 0.5):
        print("Nivel aceptable, recibirá una paga de {din}€.".format(din = din))
        return din
    else:
        print("Nivel meritorio, recibirá una paga de {din}€.".format(din = din))
        return din


def main():
    punt = float(input("Dime tu puntuación de rendimiento: "))
    print(rendimiento(punt))
    
    
if __name__ == '__main__':
    main()