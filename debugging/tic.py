#!/usr/bin/python3
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """
    Displays the current state of the board with column/row indices and aligned grid.
    """
    clear_screen()
    print("\n    1   2   3")
    print("  +---+---+---+")
    for i, row in enumerate(board):
        row_str = " | ".join(f"{cell:^1}" for cell in row)
        print(f"{i + 1} | {row_str} |")
        print("  +---+---+---+")
    print("\n")

def check_winner(board):
    """
    Checks if there is a winner on the board.

    Return:
    str: "X" or "O" if there's a winner ; none otherwise
    """
    # Rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    """
    Return: true if the board is full (i.e., no empty cells)
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main loop to play a game of Tic Tac Toe.
    Handles user input, game state updates, and error management.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            col = int(input(f"Enter Column for player {player}: ")) - 1
            row = int(input(f"Enter Row for player {player}: ")) - 1
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid coordinates. Please enter 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        except EOFError:
            print("\nInput interrupted. Exiting game.")
            return

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()