def chooseSize(sizes):
    print("Elija un tamaño:")

    # Iteración que recorre la lista de tamaños dispolibles y los muestra
    for size in sizes:
        print("\t",size[0], "-",size[1])
    opcion = int(input("Opción: "))

    # Valida que ingresó una opción válida
    if opcion > len(sizes):
        print("¡Debe seleccionar una opción válida!")
        chooseSize(sizes)
    else:
        return opcion