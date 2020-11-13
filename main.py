from choose_size import chooseSize

# Electiva: Programación con Python
# Proyecto #1 - Pizzería

# Realizado por:
# David Monroy CI: 26.473.543
# Carolina Patiño CI:

print('***********************')
print('*    PIZZERÍA UCAB    *')
print('***********************')

sizes = [(1,"Pequeña"), (2,"Mediana"), (3, "Grande")] # Lista de tuplas donde cada elemento es un identificador y su tamaño
n_pizza = 1 # Número de pizza a pedir (Veces de ejecución del menú principal)

def main():
    if n_pizza == 1:
        print("     ¡Bienvenido!")
    print("***** Pizza N°", n_pizza, "******")
    print('***********************')
    selected_size = chooseSize(sizes) - 1 # Almacena el ID de tamaño escogido
    print("Pizza", sizes[selected_size][1])
main()
    