from clases_HLF import *
from Funciones_HLF import *
from variables_HLF import *

def main():
    print("Bienvenido a Hundir la Flota!")
    tablero_jugador = Tablero("Jugador")
    tablero_maquina = Tablero("Máquina")

    turno = True  # True: jugador, False: máquina
    while tablero_jugador.vida> 0 and tablero_maquina.vida > 0:
        if turno:
            if not turno_jugador(tablero_maquina):
                turno = False
        else:
            if not turno_maquina(tablero_jugador):
                turno = True
    
    if tablero_jugador.vida == 0:
        print("La máquina ha ganado.")
    else:
        print("¡Has ganado!")

def jugar():
    print("Starting the game!")

jugar()  # This will run automatically when you execute main.py



