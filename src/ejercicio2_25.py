from ejercicio2_24 import recibNum


def sumatorNumPos(num: int):
    sum = 0
    while(num != 0):
        if(num > 0):
            sum += num
        num = recibNum()
    return "La suma final es {sum}".format(sum = sum)


def main():
    number = int(input("Dime un número: "))
    print(sumatorNumPos(number))
    
    
if __name__ == '__main__':
    main()