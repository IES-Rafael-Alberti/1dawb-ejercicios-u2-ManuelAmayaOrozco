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