import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # Initialize variables
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        # Create grid of buttons
        for i in range(9):
            button = tk.Button(root, text="", font=("Arial", 40), height=2, width=5,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        # Create reset button
        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 20), command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def on_button_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_game(self):
        # Reset the game
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
