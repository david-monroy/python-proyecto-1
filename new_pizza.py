from options_menu import *
from show_header import *
from calculator import *
import time

def anotherPizza(quantity_pizza):
    showHeader(quantity_pizza)
    print("¿Desea agregar otra PIZZA a su orden?")
    print("\ts - Sí")
    print("\tn - No")

    option = input("\nSeleccione una opción: ")

    if option == "s":
        return True
    elif option == "n":
        return False
    else:
        print("¡Debe seleccionar una opción válida!")
        return anotherPizza(quantity_pizza)

def newPizza(sizes,ingredients,quantity_pizza):
    pizza = {}
    showHeader(quantity_pizza)
    selected_size = chooseSize(sizes) # Crea lista TEMPORAL con tamaño y precio correspondiente
    print(selected_size)
    showHeader(quantity_pizza)

    pizza["Size"] = selected_size
    selected_ingredients= chooseIngredients(ingredients) #Crea lista TEMPORAL con ingredientes y precios
    pizza["Ingredients"] = selected_ingredients
    pizza["Total"] = calculate_pizza(pizza)
    if pizza["Ingredients"]!= []:
        print(f'Usted seleccionó una pizza {pizza["Size"][0]} con', end = ' ')
        for i in range(len(pizza["Ingredients"])):
            print(pizza["Ingredients"][i][0],f'(+${pizza["Ingredients"][i][1]})', end = ' ')
            if i == len(pizza["Ingredients"])-1:
                print(end = ' ')
            elif i == len(pizza["Ingredients"])-2:
                print(end= ' y ')
            else: 
                print(end= ', ')
    else:
        print(f'Usted seleccionó una pizza {pizza["Size"][0]} Margarita')
    print("\n")
    time.sleep(1)
    return pizza
    