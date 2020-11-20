from options_menu import chooseSize,chooseIngredients
from show_header import *

def anotherPizza():
    print("¿Desea agregar otra pizza a su orden?")
    print("\ts - Sí")
    print("\tn - No")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "s":
        return True
    elif opcion == "n":
        return False
    else:
        print("¡Debe seleccionar una opción válida!")
        return anotherPizza()

def newPizza(sizes,ingredients,quantity_pizza):
    order={}
    selected_size = chooseSize(sizes) # Crea lista TEMPORAL con tamaño y precio correspondiente
    print(selected_size)
    showHeader(quantity_pizza)
    order["Size"]=selected_size
    selected_ingredients= chooseIngredients(ingredients) #Crea lista TEMPORAL con ingredientes y precios
    order["Ingredients"] = selected_ingredients
    order["Total"]=0
    showHeader(quantity_pizza)
    print(f'Usted seleccionó una pizza {order["Size"][0]} con', end = ' ')
    for i in range(len(order["Ingredients"])):
        print (order["Ingredients"][i][0], end= ' ')
    print("\n")
    return order
    