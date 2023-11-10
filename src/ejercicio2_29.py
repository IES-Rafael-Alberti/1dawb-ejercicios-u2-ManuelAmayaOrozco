"""
Ejercicio 2.2.19
Mostrar un menú con tres opciones:

MENÚ
----
1 - Introduzca una nota
2 - Imprimir listado
3 - Finalizar programa
Seleccione una opción => 

A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3).
Si elige una opción incorrecta, informarle del error.
El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir.
Si elige la opción 1 debe pedir que introduzca una nota.
Si elige la opción 2 se imprimirá la lista de las notas introducidas.
Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
"""


def menuNotes():
    print("MENÚ")
    print("----")
    print("1 - Introduce una nota")
    print("2 - Imprimir listado")
    print("3 - Finaliza programa")
    opt = input("Seleccione una opción => ")
    ser = ""
    while(opt != (1, 2, 3)):
        if(opt == "1"):
            note = enterNote()
            if(ser == ""):
                ser = note
            else:
                ser = "{ser} - {note}".format(ser= ser, note = note)
        elif(opt == "2"):
            print(ser)
        elif(opt == "3"):
            return "Programa finalizado."
        else:
            print("**ERROR** Número incorrecto.")
        opt = input("Seleccione una opción => ")
        

def enterNote():
    note = str(input("Introduzca una nota: "))
    return note


def main():
    print(menuNotes())
    
    
if __name__ == '__main__':
    main()