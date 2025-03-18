from Funciones_HLF import *
import pprint
import time
import os 
from variables_HLF import *
from clases_HLF import *

mensaje_bienvenida()
teblero_computer = crear_tablero(TAMANO)
teblero_computer_visualizar = crear_tablero(TAMANO)
#print("Tablero vacio")
#pprint.pprint(tablero_computer)

posicionar_barcos_fijos(tablero_computer)
print("Tablero computer con barcos fijos. Te doy 5 segundos para memorizarlos..")
time.sleep(5)
visualizar(tablero_computer)
os.system("cls")
print()
while True:
    print("Tus disparos")
    visualizar(tablero_mostrar)
    print(" ")
    i = input("Introduce la fila")                                        #  EN OTRA FUNCION
    j = input("Introduce la columna")
    acierto = disparo(tablero_computer, tablero_computer,i,j )
    if not acierto:
        break
    os.system("cls")