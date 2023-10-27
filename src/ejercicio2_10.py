def pizzatime(elec: str):
    if (elec == "V"):
        ing = elecIngredveg()
        print("Su pizza vegetariana lleva: Mozzarella, Tomate, {ing}.".format(ing = ing))
        return "V"
    else:
        ing = elecIngred()
        if (ing == "Pimiento" or ing == "Tofu"):
            print("Su pizza vegetariana lleva: Mozzarella, Tomate, {ing}.".format(ing = ing))
            return "V"
        else:
            print("Su pizza vegetariana lleva: Mozzarella, Tomate, {ing}.".format(ing = ing))
            return "N"
    
def elecIngredveg():
    ingr = input("Elige un ingrediente (Pimiento, Tofu): ")
    return ingr

def elecIngred():
    ingr = input("Elige un ingrediente (Peperoni, Jamón, Salmón, Pimiento, Tofu): ")
    return ingr

def main():
    eleccion = input("¿Quieres que tu pizza sea vegetariana? (V para Vegetariana, N para Normal): ")
    print(pizzatime(eleccion))
    
if __name__ == '__main__':
     main()