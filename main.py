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

def main():
    quantity_pizza=0
    showHeader(quantity_pizza)
    add_pizza = True
          
    while add_pizza is True:
        quantity_pizza+=1
        order[quantity_pizza]=newPizza(sizes,ingredients,quantity_pizza)
        add_pizza = anotherPizza()
    print(order)

main()
 
