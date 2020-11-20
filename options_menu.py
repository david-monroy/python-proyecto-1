def chooseSize(sizes):
    print("Elija un tamaño:")
    i = 1
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


def chooseIngredients(ingredients):
    print("Ingredientes:")
    option = 0
    selected_ingredients=[]

    #Muestra los ingredientes en pantalla
    for key, value in ingredients.items():
        print("\t",key, "-",value[0])

    #Permite ingresar la cantidad de ingredientes que desee el cliente
    while 1==1: 
        option = input("Ingrese el ingrediente (enter para terminar): ")
        if option != "":
            if option in ingredients.keys():
                if ingredients[option] in selected_ingredients:
                   print("Ya ha agregado", ingredients[option][0], "como ingrediente") 
                else:
                    selected_ingredients.append(ingredients[option])
            else:
                print("¡Debe seleccionar una opción válida!")
        else: 
            break

    return selected_ingredients