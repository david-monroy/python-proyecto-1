import os

def clean():
    if os.name == "posix": # Limpiar pantalla en Linux
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls") # Limpiar pantalla en Windows

def showHeader(n):
    
    clean()
    print(23*'*')
    print('*    PIZZERÍA UCAB    *')
    print(23*'*')
    if n == "done":
        print ("** RESUMEN DE COMPRA **")
    elif n == "thanks":
        print ("* ¡Gracias por su compra, \nregrese prnoto! *")
    else:
        print("***** Pizza N°", n, "******")
    print(23*'*')

