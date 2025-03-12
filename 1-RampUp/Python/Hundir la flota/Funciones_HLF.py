from clases_HLF import *
import random

def obtener_coordenadas():
    while True:
        try:
            fila = int(input("Introduce fila (0-9): "))
            columna = int(input("Introduce columna (0-9): "))
            if 0 <= fila < variables_HLF.TAMANIO_TABLERO and 0 <= columna < variables_HLF.TAMANIO_TABLERO:
                return fila, columna
            else:
                print("Coordenadas fuera del rango, intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Introduce números enteros.")

def turno_jugador(tablero_maquina):
    print("Tu turno!")
    tablero_maquina.mostrar_tablero(oculto=True)
    fila, columna = obtener_coordenadas()
    if tablero_maquina.recibir_disparo(fila, columna):
        print("¡Impacto!")
        return True
    else:
        print("Agua...")
        return False

def turno_maquina(tablero_jugador):
    print("Turno de la máquina...")
    while True:
        fila = random.randint(0, variables_HLF.TAMANIO_TABLERO - 1)
        columna = random.randint(0, variables_HLF.TAMANIO_TABLERO - 1)
        if tablero_jugador.tablero[fila, columna] not in [variables_HLF.IMPACTO, variables_HLF.FALLO]:
            break
    if tablero_jugador.recibir_disparo(fila, columna):
        print(f"La máquina impactó en ({fila}, {columna})")
        return True
    else:
        print(f"La máquina falló en ({fila}, {columna})")
        return False
