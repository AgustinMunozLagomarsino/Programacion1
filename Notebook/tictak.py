def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Comprobar filas
    for row in board:
        if all(s == player for s in row):
            return True
    
    # Comprobar columnas
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Comprobar diagonales
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_player_move(player):
    while True:
        move = input(f"Jugador {player}, ingresa tu movimiento (fila y columna, separados por espacio): ")
        try:
            row, col = map(int, move.split())
            if row in range(1, 4) and col in range(1, 4):
                return row - 1, col - 1
            else:
                print("Movimiento fuera de rango. Intenta nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingresa dos números separados por un espacio.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row, col = get_player_move(current_player)

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"¡Jugador {current_player} gana!")
                break
            elif is_draw(board):
                print_board(board)
                print("¡Es un empate!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Esa casilla ya está ocupada. Intenta nuevamente.")

if __name__ == "__main__":
    main()
