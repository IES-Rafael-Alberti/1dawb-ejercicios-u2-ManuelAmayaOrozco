from ejercicio2_24 import recibNum


def mayorNum(num: int):
    mayor = num
    while(num != 0):
        if(num > mayor):
            mayor = num
        num = recibNum()
    return "El mayor número introducido es {mayor}".format(mayor = mayor)


def main():
    number = int(input("Dime un número: "))
    print(mayorNum(number))
    
    
if __name__ == '__main__':
    main()