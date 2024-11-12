import random

#no tocar ya funciona
def MenuDificultad():
    while True:
        try:
            dificultad = int(input("Elige la dificultad (1: Fácil, 2: Medio, 3: Difícil): "))
            if dificultad in [1, 2, 3]:
                return dificultad
            else:
                print("Error: Elige un valor entre 1 y 3.")
        except ValueError:
            print("Error: Por favor, ingresa un número.")
############################################################################

############################ tablero #####################################3

def tablero_vacio():
    # Crear el tablero vacío
    filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    columnas = list(range(10))
    
    # Imprimir encabezado de columnas
    print("   " + " ".join(str(col) for col in columnas))
    
    # Crear e imprimir las filas del tablero
    tablero = [['-' for _ in columnas] for _ in filas]
    
    for i, fila in enumerate(filas):
        print(fila + "  " + " ".join(tablero[i]))

    return tablero

def tablero_disparo():
    # Crear el tablero 
    print("------------Disparos------------")
    filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    columnas = list(range(10))
    
    # Imprimir encabezado de columnas
    print("   " + " ".join(str(col) for col in columnas))
    
    # Crear e imprimir las filas del tablero
    tablero = [['-' for _ in columnas] for _ in filas]
    
    for i, fila in enumerate(filas):
        print(fila + "  " + " ".join(tablero[i]))

    return tablero

def tablero_pc():
    # Crear el tablero 
    print("------------Tablero Pc------------")
    filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    columnas = list(range(10))
    
    # Imprimir encabezado de columnas
    print("   " + " ".join(str(col) for col in columnas))
    
    # Crear e imprimir las filas del tablero
    tablero = [['-' for _ in columnas] for _ in filas]
    
    for i, fila in enumerate(filas):
        print(fila + "  " + " ".join(tablero[i]))

    return tablero

#################################################################################################