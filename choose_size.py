def chooseSize(sizes):
    print("Elija un tamaño:")
    i = 1
    # Iteración que recorre la lista de tamaños dispolibles y los muestra
    for key, value in sizes.items():
        print("\t",key, "-",value[0])
    option = input("Opción: ")

    # Valida que ingresó una opción válida
    if option not in sizes.keys():
        print("¡Debe seleccionar una opción válida!")
        chooseSize(sizes)
    else:
        return option

        