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
#####################################################################################

############################ tableros jugadores #####################################

def tablero_vacio():
    # Crear el tablero vacío
    filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    columnas = list(range(10))
    
    # Crear la estructura del tablero
    tablero = [['-' for _ in columnas] for _ in filas]
    return tablero

def imprimir_tablero(tablero):
    # Crear el tablero con filas y columnas
    filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    columnas = list(range(10))
    
    print("   " + " ".join(str(col) for col in columnas))
    
    for i, fila in enumerate(filas):
        print(fila + "  " + " ".join(tablero[i]))

#################################################################################################
# COLOCAR BARCOS
# Función para generar el tablero del jugador según la dificultad
def colocarBarcos(tablero, cantidad, tipo):
    # Definir tamaños para cada tipo de barco
    tamanios = {
        "L": 4,  # Longitud del barco 'L'
        "B": 3,  # Longitud del barco 'B'
        "Z": 2,  # Longitud del barco 'Z'
        "P": 1   # Longitud del barco 'P'
    }
    
    tamaño = tamanios[tipo]  # Obtener el tamaño del barco según el tipo

    for _ in range(cantidad):
        colocado = False
        while not colocado:
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            direccion = random.choice(["H", "V"])  # Horizontal o Vertical

            # Comprobar si cabe en la dirección deseada y no hay colisión con otros barcos
            if direccion == "H" and columna + tamaño <= 10:
                if all(tablero[fila][columna + i] == "-" for i in range(tamaño)):
                    for i in range(tamaño):
                        tablero[fila][columna + i] = tipo
                    colocado = True
            elif direccion == "V" and fila + tamaño <= 10:
                if all(tablero[fila + i][columna] == "-" for i in range(tamaño)):
                    for i in range(tamaño):
                        tablero[fila + i][columna] = tipo
                    colocado = True

# Ejemplo de uso:
tablero_jugador = tablero_vacio()

# Colocar barcos en el tablero del jugador
colocarBarcos(tablero_jugador, 1, "L")  # Coloca 1 barco de tamaño 4
colocarBarcos(tablero_jugador, 2, "B")  # Coloca 2 barcos de tamaño 3
colocarBarcos(tablero_jugador, 3, "Z")  # Coloca 3 barcos de tamaño 2
colocarBarcos(tablero_jugador, 4, "P")  # Coloca 4 barcos de tamaño 1

# Imprimir tablero actualizado
print("\nTablero con barcos:")
imprimir_tablero(tablero_jugador)



################################################################################################# 
#DISPAROS JUGADORES
