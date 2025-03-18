import random
from variables_HLF import *
import pprint

class Tablero:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.tablero = [[" " for i in range(TAMANIO_TABLERO)] for j in range(TAMANIO_TABLERO)]
        self.tablero_disparos = [[" " for _i in range(TAMANIO_TABLERO)] for j in range(TAMANIO_TABLERO)]
        self.barcos = []
        self.vida = sum(BARCOS.values())
        self.colocar_barcos()
    
    
    def colocar_barcos(self):
        for _, eslora in BARCOS.items():
            colocado = False
            while not colocado:
                fila = random.randint(0, TAMANIO_TABLERO - 1)
                columna = random.randint(0, TAMANIO_TABLERO - 1)
                direccion = random.choice(["N","S","E","O"])
                if self.verificar_espacio(fila, columna, eslora, direccion):
                    self.poner_barco(fila, columna, eslora, direccion)
                    colocado = True

    def verificar_espacio(self, fila, columna, eslora, direccion):
        if direccion == "H":
            if columna + eslora > TAMANIO_TABLERO:
                return False
            return all(self.tablero[fila][columna + i] == AGUA for i in range(eslora))
        else:
            if fila + eslora > TAMANIO_TABLERO:
                return False
            return all(self.tablero[fila + i][columna] == AGUA for i in range(eslora))

    def poner_barco(self, fila, columna, eslora, direccion):
        for i in range(eslora):
            if direccion == "H":
                self.tablero[fila][columna + i] = BARCO
            else:
                self.tablero[fila + i][columna] = BARCO

    def recibir_disparo(self, fila, columna):
        if self.tablero[fila][columna] == BARCO:
            self.tablero[fila][columna] = IMPACTO
            self.vida -= 1
            return True
        else:
            self.tablero[fila][columna] = FALLO
            return False

    def mostrar_tablero(self, oculto=False):
        if oculto:
            print("\n".join(" ".join(self.tablero_disparos[row]) for row in range(TAMANIO_TABLERO)))
        else:
            print("\n".join(" ".join(self.tablero[row]) for row in range(TAMANIO_TABLERO)))
            

"""
            

import random
from variables_HLF import * 

class Tablero:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.tablero = [[AGUA for _ in range(TAMANIO_TABLERO)] for _ in range(TAMANIO_TABLERO)]
        self.tablero_disparos = [[AGUA for _ in range(TAMANIO_TABLERO)] for _ in range(TAMANIO_TABLERO)]
        self.barcos = []
        self.vida = sum(BARCOS.values())
        self.colocar_barcos()

    def colocar_barcos(self):
        for _, eslora in BARCOS.items():
            colocado = False
            while not colocado:
                fila = random.randint(0, TAMANIO_TABLERO - 1)
                columna = random.randint(0, TAMANIO_TABLERO - 1)
                direccion = random.choice(["H", "V"])
                if self.verificar_espacio(fila, columna, eslora, direccion):
                    self.poner_barco(fila, columna, eslora, direccion)
                    colocado = True

    def recibir_disparo(self, fila, columna):
        if self.tablero[fila][columna] == BARCO:
            self.tablero[fila][columna] = IMPACTO
            self.vida -= 1
            return True
        else:
            self.tablero[fila][columna] = FALLO
            return False
        """
