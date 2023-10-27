def capital(amount: int, interest: int, year: int):
    while(year > 0):
        amount *= 1 + interest / 100
        year -= 1
    return amount

def main():
    cant = int(input("Dime la cantidad a invertir: "))
    inter = int(input("Dime el interés anual: "))
    ano = int(input("Dime el número de años: "))
    print(capital(cant, inter, ano))
    if __name__ == '__main__':
        main()