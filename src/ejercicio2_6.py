""" 
Ejercicio 2.1.6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El
grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un
nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su
nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""


def asiggrupo(nom: str, sex: int):
    nom = nom[0]
    if((nom == "A" or nom == "B" or nom == "C" or nom == "D" or nom == "E" or nom == "F" or nom == "G" or nom == "H" or nom == "I" or nom == "J" or nom == "K" or nom == "L" or nom == "M") and sex == 1):
        return "Eres parte del grupo B."
    elif((nom == "A" or nom == "B" or nom == "C" or nom == "D" or nom == "E" or nom == "F" or nom == "G" or nom == "H" or nom == "I" or nom == "J" or nom == "K" or nom == "L" or nom == "M") and sex == 2):
        return "Eres parte del grupo A."
    elif((nom == "N" or nom == "O" or nom == "P" or nom == "Q" or nom == "R" or nom == "S" or nom == "T" or nom == "U" or nom == "V" or nom == "W" or nom == "X" or nom == "Y" or nom == "Z") and sex == 1):
        return "Eres parte del grupo A."
    elif((nom == "N" or nom == "O" or nom == "P" or nom == "Q" or nom == "R" or nom == "S" or nom == "T" or nom == "U" or nom == "V" or nom == "W" or nom == "X" or nom == "Y" or nom == "Z") and sex == 2):
        return "Eres parte del grupo B."
    
    
def main():
    nombre = input("Dime tu nombre: ")
    sexo = 0
    while(sexo != 1 and sexo != 2):
        sexo = int(input("¿Eres hombre o mujer? (Escribe solo 1 para Hombre o 2 para Mujer): "))
    print(asiggrupo(nombre, sexo))
    
    
if __name__ == '__main__':
    main()
