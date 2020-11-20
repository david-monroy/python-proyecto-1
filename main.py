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
        quantity_pizza+=1
        order[quantity_pizza] = newPizza(sizes,ingredients,quantity_pizza) # Pedir nueva pizza
        add_pizza = anotherPizza(quantity_pizza)
    selected_drinks = getDrinks(drinks,quantity_pizza)
    order["Drinks"] = selected_drinks
    
    clientInfo = delivery(quantity_pizza)   # Pregunta por delivery
    order_total = calculate_order(order)    # Calcula y almacena el total de la orden
    showHeader("done")
    
    print ("Su pedido tiene un total de", quantity_pizza, "pizzas y", len(order["Drinks"]), "bebidas:")
    for i in range(len(order)-1):
        if order[i+1]["Ingredients"] !=[]:
            print(f'Una pizza {order[i+1]["Size"][0]} con', end = ' ')
            for j in range(len(order[i+1]["Ingredients"])):
                if i == len(order[i+1]["Ingredients"])-1:
                    print (order[i+1]["Ingredients"][i][0])
                elif i == len(order[i+1]["Ingredients"])-2:
                    print (order[i+1]["Ingredients"][i][0], end= ' y ')
                else: 
                    print (order[i+1]["Ingredients"][i][0], end= ', ')
            print ("por un monto de $", order[i+1]["Total"])
        else:
            print(f'Una pizza {order[i+1]["Size"][0]} Margarita')
        
    for i in order["Drinks"]:
        print(f'Una {i[0]} por un monto de $', i[1])
    print(23*'-')
    clientInfo = delivery(quantity_pizza)
    order_total = calculate_order(order)    
    print(order_total)
    showHeader(quantity_pizza)
    print ("***** RESUMEN DE COMPRA *****")
    print ("Su pedido tiene un total de", quantity_pizza, "pizzas")

    for i in range(len(order)-1):
        if order[i+1]["Ingredients"] !=[]:
            print(f'Una pizza {order[i+1]["Size"][0]} con', end = ' ')
            for j in range(len(order[i+1]["Ingredients"])):
                if i == len(order[i+1]["Ingredients"])-1:
                    print (order[i+1]["Ingredients"][i][0])
                elif i == len(order[i+1]["Ingredients"])-2:
                    print (order[i+1]["Ingredients"][i][0], end= ' y ')
                else: 
                    print (order[i+1]["Ingredients"][i][0], end= ', ')
            print ("por un monto de ")
        else:
             print(f'Una pizza {order[i+1]["Size"][0]} Margarita')
    print("Monto total: $",order_total)
    print(23*'-')
    if clientInfo != None:
        print ("Delivery a", clientInfo["direction"], "Llamar al", clientInfo["phone"])

    thanks = input("Presione enter para finalizar: ")
    showHeader("thanks")

main()
 
