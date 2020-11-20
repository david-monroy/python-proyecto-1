from choose_ingredients import chooseIngredients
from choose_size import *

# Electiva: Programación con Python
# Proyecto #1 - Pizzería

# Realizado por:
# David Monroy CI: 26.473.543
# Carolina Patiño CI:

print('***********************')
print('*    PIZZERÍA UCAB    *')
print('***********************')

sizes = {
    "p": ["Personal", 280],
    "m": ["Mediana", 430],
    "g": ["Grande", 580],
}

ingredients = {
    "ja": ["Jamón", 40],
    "ch": ["Champiñones", 35],
    "pi": ["Pimentón", 30],
    "dq": ["Doble Queso", 40],
    "ac": ["Aceitunas", 57.5],
    "pp": ["Pepperoni", 38.5],
    "sa": ["Salchichon", 62.5],
}

order = {
    1: {"Tamaño":[], "Ingredientes":[], "Total": 0}
}

pizza = [] # Lista para la PIZZA, que contiene tamaño e ingredientes
selected_size = [] # Lista para guardar el tamaño en cada iteración
selected_ingredients = [] #Lista para guardar los ingredientes seleccionados para cada pizza

def main():
    if order == None:
        print("     ¡Bienvenido!")
    print("***** Pizza N°", len(order)+1, "******")
    print('***********************')

    selected_size = chooseSize(sizes) # Crea lista TEMPORAL con tamaño y precio correspondiente
    print(selected_size)
    order[1]["Tamaño"]=selected_size
    selected_ingredients= chooseIngredients(ingredients) #Crea lista TEMPORAL con ingredientes y precios
    order[1]["Ingredientes"] = selected_ingredients
    print("La pizza que ordenó:", order)
    
main()
    