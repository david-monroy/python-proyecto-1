def calculate_pizza(pizza):
    total = 0
    for key,value in pizza.items():
        if key == "Tamaño":
            total += value[1]
        else:
            for i in value:
                total += i[1]
    return total

def calculate_order(order):
    total = 0
    lista = list(order.values())
    for i in lista:
        print(i)
    return total