"""
Ejercicio 2.2.21
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se
desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando
el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se
debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar
teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de
descuento.
"""


def sumMontos():
    total = 0
    monto = pedirMonto()
    while(monto != 0):
        if(monto < 0):
            print("Monto no válido, ingrese un nuevo monto.")
        else:
            total += monto
        monto = pedirMonto()
    if(total > 1000):
        total -= (total * 0.1)
    return "El monto total a pagar es de {total}$".format(total = total)


def pedirMonto():
    monto = float(input("Dime el monto a introducir: "))
    return monto


def main():
    print(sumMontos())
    
    
if __name__ == '__main__':
    main()