def numPrimo(num: int):
    if (num == 0):
        return False
    else:
        for i in range(2, num):
            if ((num % i) == 0):
                return False
        return True


def main():
    number = int(input("Dime un número: "))
    if numPrimo(number):
        print("El número es primo.")
    else:
        print("El número no es primo.")
     
        
if __name__ == '__main__':
     main()