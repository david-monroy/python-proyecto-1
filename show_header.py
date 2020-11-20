import os

def clean():
    if os.name == "posix": # Limpiar pantalla en Linux
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls") # Limpiar pantalla en Windows

def showHeader(n):
    clean()
    print('***********************')
    print('*    PIZZERÍA UCAB    *')
    print('***********************')
    print("***** Pizza N°", n, "******")
    print('***********************')

