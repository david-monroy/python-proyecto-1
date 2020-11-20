import time
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
    i = 1
    option = 0
    selected_ingredients=[]

    #Muestra los ingredientes en pantalla
    for key, value in ingredients.items():
        print("\t",key, "-",value[0], "-", value[1])

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

def getDrinks(drinks,quantity_pizza):
    showHeader(quantity_pizza)
    print("¿Desea agregar BEBIDAS a su orden?")
    print("\ts - Sí")
    print("\tn - No")

    drink_option = input("\nSeleccione una opción: ")
    print("Bebidas:")
    selected_drinks = []
    option = 0

    #Muestra las bebidas en pantalla
    for key, value in drinks.items():
        print("\t",key, "-",value[0],"- $",value[1])

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
        return selected_drinks
    else:
        print("¡Debe seleccionar una opción válida!")
        return getDrink(drinks)
def delivery():
    print("¿Cómo desea recibir su pedido?")
    print("\td - Delivery")
    print("\tp - Pick-Up")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "d":
        deliveryInfo={}
        deliveryInfo["phone"] = input("Ingrese su número de teléfono:")
        deliveryInfo["direction"] = input ("Ingrese su dirección:")
        return deliveryInfo
    elif opcion == "p":
        print("Lo esperamos!")
        time.sleep(1)

    else:
        print("¡Debe seleccionar una opción válida!")
        return delivery()
