from options_menu import *
from show_header import *
from calculator import *

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

def newPizza(sizes,ingredients,drinks,quantity_pizza):
    pizza = {}
    showHeader(quantity_pizza)
    selected_size = chooseSize(sizes) # Crea lista TEMPORAL con tamaño y precio correspondiente
    print(selected_size)
    showHeader(quantity_pizza)
    pizza["Tamaño"] = selected_size
    selected_ingredients = chooseIngredients(ingredients) #Crea lista TEMPORAL con ingredientes y precios
    pizza["Ingredientes"] = selected_ingredients
    showHeader(quantity_pizza)
    pizza["Total"] = calculate_pizza(pizza)
    return pizza
    