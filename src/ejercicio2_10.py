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