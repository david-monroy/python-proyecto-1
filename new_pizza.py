def newPizza():
    print("¿Desea agregar otra pizza a su orden?")
    print("\ts - Sí")
    print("\tn - No")

    option = input("\nSeleccione una opción: ")

    if option == "s":
        return True
    elif option == "n":
        return False
    else:
        print("¡Debe seleccionar una opción válida!")
        return newPizza()
