def newPizza():
    print("¿Desea agregar otra pizza a su orden?")
    print("\ts - Sí")
    print("\tn - No")

    opcion = input("Seleccione una opción: ")

    if opcion == "s":
        return True
    elif opcion == "n":
        return False
    else:
        print("¡Debe seleccionar una opción válida!")
        return newPizza()
