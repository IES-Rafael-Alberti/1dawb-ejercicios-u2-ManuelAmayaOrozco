def asterTriangulo(num: int):
    for i in range(1, num):
        print("*" * i)
    fin = ("*" * num)
    return fin

def main():
    number = int(input("Dime un número: "))
    print(asterTriangulo(number))
    
    
if __name__ == '__main__':
    main()