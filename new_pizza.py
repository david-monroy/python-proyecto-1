from options_menu import chooseSize,chooseIngredients
from show_header import *

def anotherPizza(quantity_pizza):
    showHeader(quantity_pizza)
    print("¿Desea agregar otra pizza a su orden?")
    print("\ts - Sí")
    print("\tn - No")

    option = input("\nSeleccione una opción: ")

    if option == "s":
        return True
    elif option == "n":
        return False
    else:
        print("¡Debe seleccionar una opción válida!")
        return anotherPizza()

def newPizza(sizes,ingredients,quantity_pizza):
    order={}
    selected_size = chooseSize(sizes, quantity_pizza) # Crea lista TEMPORAL con tamaño y precio correspondiente
    print(selected_size)
    showHeader(quantity_pizza)
    order["Tamaño"]=selected_size
    selected_ingredients= chooseIngredients(ingredients) #Crea lista TEMPORAL con ingredientes y precios
    order["Ingredientes"] = selected_ingredients
    order["Total"]=0
    showHeader(quantity_pizza)
    print("La pizza que ordenó:\n", order,"\n")
    return order
    