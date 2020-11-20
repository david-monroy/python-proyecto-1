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

drinks = {
    "a": ["Agua", 10],
    "l": ["Limonada", 15],
    "c": ["Coca-Cola", 20],
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
    quantity_pizza = 0  # Cantida de pizzas
    add_pizza = True    # Booleano para detener el ciclo de peticiones
          
    while add_pizza is True:
        quantity_pizza += 1
        order[quantity_pizza] = newPizza(sizes,ingredients,drinks,quantity_pizza) # Pedir nueva pizza
        add_pizza = anotherPizza(quantity_pizza)
    selected_drinks = getDrinks(drinks,quantity_pizza)
    order["Bebidas"] = selected_drinks
    order_total = calculate_order(order)    
    print(order)

main()
 
