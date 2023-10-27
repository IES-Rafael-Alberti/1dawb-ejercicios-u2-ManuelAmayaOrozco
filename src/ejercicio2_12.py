def cuentEdad(ed: int):
    i = 1
    while(i < ed):
        print(i)
        i += 1
    return ed

def main():
    edad = int(input("Dime tu edad: "))
    print(cuentEdad(edad))
    if __name__ == '__main__':
        main()