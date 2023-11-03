""" 
Ejercicio 2.1.2
Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el
usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
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
    password = getPassword()
    if tPassword(password):
        print("Has acertado.")
    else:
        print("Has fallado.")
    
    
if __name__ == '__main__':
     main()