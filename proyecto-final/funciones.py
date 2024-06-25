#################################################
#
#
#             Funciones del juego
#                Tic - Tac - Toe
#
#
#################################################


# En este archivo se encuentran las funciones que son ejecutadas
# en el programa principal del juego tic-tac-toe.

from time import sleep
from random import randrange

# Para mostrar el estado actual del tablero.
def display_board(board):
    top_bottom = "+" + "-"*7
    sides = "|" + " "*7

    def num_side(elem):
          nums = []
          for j in range(0, 3):
              nums.append(" "*3 + board[elem][j] + " "*3 + "|")

          return nums[0] + nums[1] + nums[2]

    for i in range(0, 3):
        print(top_bottom*3 + "+")
        print(sides*3 + "|")
        print("|" + num_side(i))
        print(sides*3 + "|")

    print(top_bottom*3 + "+")


# Construye una lista con las celdas vacías del tablero. Las ubicaciones
# se almacenan como tuplas en la lista.
def make_list_of_free_fields(board):
    celdas_vacias = []

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] != "X" and board[i][j] != "O":
              celdas_vacias.append((i, j))

    return celdas_vacias


# Función creada por mi: Sirve para crear una lista con las celdas
# disponibles. Cada elemento es una cadena del numero de la celda.
def entradas_disponibles(board):
    celdas_disponibles = []
    celdas = make_list_of_free_fields(board)

    for i in range(len(celdas)):
        celdas_disponibles.append(board[celdas[i][0]][celdas[i][1]])

    return celdas_disponibles


# Es la función para las jugadas del usuario/a
def enter_move(board):
    print("\n**********************************************")
    print("*                ¡Es tu turno!               *")
    print("**********************************************\n")

    # Se muestran las celdas disponibles del tablero.
    print("El estado del tablero se muestra a continuación:\n")

    display_board(board)

    print("\nTienes disponible las siguientes celdas: ", end ="")
    
    celdas_disponibles = entradas_disponibles(board)

    print(', '.join(celdas_disponibles))

    # Turno del usuario.
    found = False

    while found != True:
        mov = input("\nIngresa el número de tu movimiento: ")
        try:
           int(mov) 
        except ValueError:
            print("\nError: Solo debes ingresar un número entero. Vuelve a intentarlo.")
            continue

        if int(mov) < 1 or int(mov) > 9:
            print("\nNúmero inválido. Vuelve a intentarlo")
            continue
        elif mov not in celdas_disponibles:
            print("\nEstá celda ya está ocupada. Vuelve a intentarlo")
            continue
        else:
            print("\nHas elegido la celda " + mov)
            confirm = input("\n¿Deseas confirmar tu jugada? (s/n): ")
            if confirm.lower() == "n":
                print("\nEstá bien. Vuelve a intentarlo")
                continue
            else:
                for i in range(0, 3):
                    for j in range(0, 3):
                        if board[i][j] == mov:
                            board[i][j] = "O"
                found = True


    print("\n¡Ha finalizado tu turno!")
    input("\nPresiona ENTER para continuar...")


# `draw_move()` es la funcion de las jugadas de la maquina/CPU.
# Funciona solo si se han importado las librerias `random` y `time`.
def draw_move(board):
    print("\n***********************************************")
    print("*              ¡Es turno de la CPU!           *")
    print("***********************************************\n")

    print("En estos momentos, está decidiendo su jugada...")

    sleep(3)
    
    found = False
    
    celdas_disponibles = entradas_disponibles(board)
    
    while found != True:
        cpu_mov = str(randrange(1, 10))
        if cpu_mov not in celdas_disponibles:
            print("\nLa CPU pensó usar la celda " + cpu_mov + ", pero ya está ocupada.")
            continue
        else:
            print("\nLa CPU ha elegido la celda " + cpu_mov)

            for i in range(0, 3):
                for j in range(0, 3):
                    if board[i][j] == cpu_mov:
                        board[i][j] = "X"
            found = True

    print("\n¡El turno de la CPU ha finalizado!")
    input("\nPresiona ENTER para continuar...")


# La siguiente funcion es para evaluar al ganador/a del juego o si termina
# en un empate.
def victory_for(board, sign):

    def msg_triunfo(sign):
        if sign == "X":
            print(
            """
            ************************
            *                      *
            *  ¡Ha ganado la CPU!  *
            *                      *
            ************************
            """
            )
            print("Hiciste un buen juego, pero la CPU fue superior")
            print("Con más práctica y perseverancia podrás vencer")
            print("**************¡A no decaer!*******************\n")
        else:
            print(
            """
            ************************
            *                      *
            *     ¡Has ganado!     *
            *                      *
            ************************
            """
            )
            print("¡Has vencido a la CPU en el Tic-Tac-Toe!\n")
            print("Este triunfo ha sido fruto de tu propio esfuerzo")
            print("Sigue así y en la vida cosecharás más victorias\n")
            print("***************¡Felicitaciones!******************\n")
 
    
    for i in range(0, 3):
        # Evaluacion por fila
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            msg_triunfo(sign)
            return True

        # Evaluacion por columna
        elif board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            msg_triunfo(sign)
            return True

    # Evaluacion diagonal
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        msg_triunfo(sign)
        return True
    
    # Evaluacion diagonal invertida
    elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        msg_triunfo(sign)
        return True

