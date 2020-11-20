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

order = [] # Lista para la ORDEN, que contiene pizzas
pizza = [] # Lista para la PIZZA, que contiene tamaño e ingredientes
selected_size = [] # Lista para guardar el tamaño en cada iteración
selected_ingredients = [] #Lista para guardar los ingredientes seleccionados para cada pizza

i = 1 # Nro de iteración
def main():
    showHeader(i)
    selected_size = chooseSize(sizes) # Crea lista TEMPORAL con tamaño y precio correspondiente
    pizza.append(selected_size)
    showHeader(i)
    selected_ingredients= chooseIngredients(ingredients) #Crea lista TEMPORAL con ingredientes y precios
    pizza.append(selected_ingredients)
    showHeader(i)
    print("La pizza que ordenó:\n",pizza,"\n")
    order.append(pizza)
       
add_pizza = True
while add_pizza is True:
    main()
    add_pizza = newPizza()
    i += 1

print("Resumen de la orden")