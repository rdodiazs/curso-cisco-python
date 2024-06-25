#################################################
#
#
#             Programa principal de
#                Tic - Tac - Toe
#
#
#################################################


from funciones import (
      display_board,
      enter_move,
      draw_move,
      victory_for,
      entradas_disponibles
)
#from random import randrange
from time import sleep

# Se crea el tablero (board) en un array de 3 x 3
tablero = []

for i in range(1, 10, 3):
    fila = []
    for j in range(i, i + 3):
        fila.append(j)
    tablero.append(fila)

# Convierto todos los elementos de tablero a 'str'.
for i in range(0, 3):
    for j in range(0, 3):
        tablero[i][j] = str(tablero[i][j])

# Juego principal.

msg_bienvenida = """
*************************************
*                                   *
*  Bienvenido al Juego Tic-Tac-Toe  *
*                                   *
*************************************
"""

msg_intro = """
##########################################################################
=                                                                        =
=  Tu rival será nada más y nada menos que... ¡la CPU de tu computador!  =
=                                                                        =
=  Como estamos en su terreno, la CPU partirá el juego y lo registrará   =
=  usando la "X".                                                        =
=                                                                        =
=  Tú, en cambio, anotarás tus jugadas utilizando el símbolo 'O'.        =
=                                                                        =
##########################################################################

¿Estás preparado para este desafío?
"""

print(msg_bienvenida)

print(msg_intro)

input("Si lo estás, presiona ENTER para comenzar...")

primer_mov = True

while True:
    if primer_mov:
       print("\nEl estado inicial del tablero es el siguiente...")

       display_board(tablero)

       print("\nLa CPU hará el primer movimiento del juego.")
       print("Espera un momento mientras piensa en su jugada...")
       sleep(3)

       print("\nHa elegido la casilla 5")
       tablero[1][1] = "X"

       print("\n¡La CPU ha terminado su turno!")

       primer_mov = False

       input("Presiona ENTER para continuar...")
          
    enter_move(tablero)

    if victory_for(tablero, "O"):
       break

    draw_move(tablero)

    if victory_for(tablero, "X"):
       break
    

    celdas_disponibles = entradas_disponibles(tablero)
    
    if len(celdas_disponibles) == 0:
       print("************************************************")
       print("Han empatado. No hay más movimientos disponibles")
       print("************************************************")
       break

