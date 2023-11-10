"""
Ejercicio 2.2.9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""


def tPassword(password: str):
    passOrig = "contraseña"
    if password.replace(" ", "").lower() == passOrig:
        return True
    else:
        return False


def getPassword():
    return input("Introduce una contraseña: ")


def main():
    fin = False
    while (fin == False):
        password = getPassword()
        if tPassword(password):
            print("Has acertado.")
            fin = True
            break
        else:
            print("Has fallado. Vuelve a intentarlo")

    
    
if __name__ == '__main__':
     main()