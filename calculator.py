def calculate_pizza(pizza):
    total = 0
    for key,value in pizza.items():
        if key == "Size":
            total += value[1]
        else:
            for i in value:
                total += i[1]
    return total

def calculate_order(order):
    total = 0
    for i in range(len(order)-1):
        total += order[i+1]["Total"]
    for j in range(len(order["Drinks"])):
        total += order["Drinks"][j][1]
    return total