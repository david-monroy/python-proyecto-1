from choose_size import chooseSize

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

order = [] # Lista para la ORDEN, que contiene pizzas
pizza = [] # Lista para la PIZZA, que contiene tamaño e ingredientes
selected_size = [] # Lista para guardar el tamaño en cada iteración

def main():
    if order == None:
        print("     ¡Bienvenido!")
    print("***** Pizza N°", len(order)+1, "******")
    print('***********************')
    size_option = chooseSize(sizes)  # Almacena el key de tamaño escogido

    selected_size = sizes[size_option] # Crea lista TEMPORAL con tamaño y precio correspondiente
    print(selected_size)
    pizza.append(selected_size) # Coloca el tamaño en la lista de la PIZZA
    print(pizza)
    
main()
    