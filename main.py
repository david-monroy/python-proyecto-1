from new_pizza import *
from show_header import *
from options_menu import delivery

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
    showHeader(quantity_pizza+1)
    add_pizza = True
          
    while add_pizza is True:
        quantity_pizza+=1
        order[quantity_pizza]=newPizza(sizes,ingredients,quantity_pizza)
        add_pizza = anotherPizza()
    showHeader(quantity_pizza)
    clientInfo = delivery()
    print ("***** RESUMEN DE COMPRA *****")
    print ("Su pedido tiene un total de", quantity_pizza, "pizzas")
    for i in range(len(order)):
        print(f'Una pizza {order[i+1]["Size"][0]} con', end = ' ')
        for j in range(len(order[i+1]["Ingredients"])):
            print (order[i+1]["Ingredients"][j][0], end= ' ')
        print ("por un monto de ")

    if clientInfo != None:
        print ("Delivery a", clientInfo["direction"], "Llamar al", clientInfo["phone"])

main()
 
