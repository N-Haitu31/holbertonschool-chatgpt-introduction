#!/usr/bin/python3
import random
import os
import sys


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        max_cells = width * height
        if not (0 < mines < max_cells):
            raise ValueError(f"Le nombre de mines doit être entre 1 et {max_cells - 1}.")
        self.mines = set(random.sample(range(max_cells), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.total_safe = max_cells - mines
        self.revealed_count = 0

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:>2} ", end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        ch = '*'
                    else:
                        c = self.count_mines_nearby(x, y)
                        ch = str(c) if c > 0 else ' '
                else:
                    ch = '.'
                print(ch, end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue  # ne pas compter la case courante
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def reveal(self, x, y):
        if not self.in_bounds(x, y):
            return True  # ignorer hors bornes sans casser la partie
        if self.revealed[y][x]:
            return True  # déjà révélé, rien à faire
        idx = y * self.width + x
        if idx in self.mines:
            return False  # mine → perdu

        # révéler
        self.revealed[y][x] = True
        self.revealed_count += 1

        # flood fill sur les zéros
        if self.count_mines_nearby(x, y) == 0:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if self.in_bounds(nx, ny) and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def is_victory(self):
        return self.revealed_count == self.total_safe

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                input("Press Enter to continue...")
                continue
            except (EOFError, KeyboardInterrupt):
                print("\nBye!")
                return

            if not self.in_bounds(x, y):
                print("Out of bounds. Try again.")
                input("Press Enter to continue...")
                continue

            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break

            if self.is_victory():
                self.print_board(reveal=True)
                print("Congrats! You cleared the field 🎉")
                break


if __name__ == "__main__":
    game = Minesweeper()
    game.play()
