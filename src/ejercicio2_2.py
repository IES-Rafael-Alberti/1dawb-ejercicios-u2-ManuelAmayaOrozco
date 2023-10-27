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