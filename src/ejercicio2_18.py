def piramNum (num: int):
    cont = 1
    while (num > 1):
        cont += 2
        num -=1
    for i in range(1, cont + 1, 2):
        print("")
        for j in range(i, 0, -2):
            print("{j} ".format(j = j), end = "")
    return ""
        
    
def main():
    numer = int(input("Dime un número: "))
    print(piramNum(numer))
    

if __name__ == '__main__':
    main()