from choose_ingredients import chooseIngredients
from choose_size import *
from new_pizza import *
from show_header import *

# Electiva: Programación con Python
# Proyecto #1 - Pizzería

# Realizado por:
# David Monroy CI: 26.473.543
# Carolina Patiño CI:

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

order = {}

pizza = [] # Lista para la PIZZA, que contiene tamaño e ingredientes
selected_size = [] # Lista para guardar el tamaño en cada iteración
selected_ingredients = [] #Lista para guardar los ingredientes seleccionados para cada pizza
add_pizza = True
quantity_pizza=0

def main(quantity_pizza):
    showHeader(quantity_pizza)
    selected_size = chooseSize(sizes) # Crea lista TEMPORAL con tamaño y precio correspondiente
    print(selected_size)
    showHeader(quantity_pizza)
    order[quantity_pizza]= {"Tamaño":[], "Ingredientes":[], "Total": 0}
    order[quantity_pizza]["Tamaño"]=selected_size
    selected_ingredients= chooseIngredients(ingredients) #Crea lista TEMPORAL con ingredientes y precios
    order[quantity_pizza]["Ingredientes"] = selected_ingredients
    showHeader(quantity_pizza)
    print("La pizza que ordenó:\n", order,"\n")
       
while add_pizza is True:
    quantity_pizza+=1
    main(quantity_pizza)
    add_pizza = newPizza()

 
