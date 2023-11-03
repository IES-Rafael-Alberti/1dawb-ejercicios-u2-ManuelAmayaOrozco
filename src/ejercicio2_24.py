def sumatorNum(num: int):
    sum = 0
    while(num != 0):
        sum += num
        num = recibNum()
    return "La suma final es {sum}".format(sum = sum)


def recibNum():
    num = int(input("Dime un número: "))
    return num


def main():
    number = int(input("Dime un número: "))
    print(sumatorNum(number))
    
    
if __name__ == '__main__':
    main()