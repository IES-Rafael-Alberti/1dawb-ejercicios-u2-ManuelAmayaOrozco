"""
Ejercicio 2.1.10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
ingredientes para cada tipo de pizza aparecen a continuación.
- Ingredientes vegetarianos: Pimiento y tofu.
- Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función
de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se
puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al
final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes
que lleva.
"""


def pizzatime(elec: str):
    if (elec == "V"):
        return "V"
    else:
        return "N"
    
    
def elecIngredveg():
    ingr = input("Elige un ingrediente (Pimiento, Tofu): ")
    print("Su pizza vegetariana lleva: Mozzarella, Tomate, {ingr}.".format(ingr = ingr))


def elecIngred():
    ingr = input("Elige un ingrediente (Peperoni, Jamón, Salmón, Pimiento, Tofu): ")
    print("Su pizza lleva: Mozzarella, Tomate, {ingr}.".format(ingr = ingr))


def main():
    eleccion = input("¿Quieres que tu pizza sea vegetariana? (V para Vegetariana, N para Normal): ")
    if (eleccion == "V"):
        print(elecIngredveg())
    else:
        print(elecIngred())
    print(pizzatime(eleccion))
   
    
if __name__ == '__main__':
     main()