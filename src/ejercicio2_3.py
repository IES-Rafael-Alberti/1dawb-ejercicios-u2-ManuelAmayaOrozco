def division(n1: int, n2: int):
    if (n2 == 0):
        return "Error, no se puede dividir por 0."
    else:
        res = n1 / n2
        return res
    
def main():
    num1 = int(input("Dime un número: "))
    num2 = int(input("Dime otro número: "))
    print(division(num1, num2))
    
    
if __name__ == '__main__':
    main()
