def chooseSize(sizes, quantity_pizza):
    showHeader(quantity_pizza)
    print("Elija un tamaño:")
    # Iteración que recorre la lista de tamaños dispolibles y los muestra
    for key, value in sizes.items():
        print("\t",key, "-",value[0])
    option = input("\nOpción: ")

    # Valida que ingresó una opción válida
    if option not in sizes.keys():
        print("¡Debe seleccionar una opción válida!", option)
        return chooseSize(sizes)
    else:
        return sizes[option]

def getDrink(drinks):
    print("¿Desea agregar una bebida a su orden?")
    print("\ts - Sí")
    print("\tn - No")

    drink_option = input("\nSeleccione una opción: ")

    if drink_option == "s":
        while 1==1: 
            option = input("Ingrese bebida (enter para terminar): ")
            if option != "":
                if option in drinks.keys():
                        selected_drinks.append(drinks[option])
                else:
                    print("¡Debe seleccionar una opción válida!")
            else: 
                break
        return selected_drinks
    elif drink_option == "n":
        return None
    else:
        print("¡Debe seleccionar una opción válida!")
        return getDrink(drinks)