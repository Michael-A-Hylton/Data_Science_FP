import tkinter as tk
from tkinter import messagebox
import numpy as np
from gameloop import UltTicTacToe  # Ensure this is your corrected gameloop.py

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Tic-Tac-Toe")
        self.game = UltTicTacToe()
        self.buttons = {}  # Dictionary to hold button widgets
        self.create_widgets()
        self.current_player = self.game.player

    def create_widgets(self):
        # Create a frame for the entire board
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        # Create 9 frames for the mini-boards
        for main_row in range(3):
            for main_col in range(3):
                frame = tk.Frame(
                    self.board_frame,
                    borderwidth=2,
                    relief="solid",
                    padx=2,
                    pady=2
                )
                frame.grid(row=main_row, column=main_col, padx=3, pady=3)
                self.create_subboard(frame, main_row, main_col)

    def create_subboard(self, parent_frame, main_row, main_col):
        for sub_row in range(3):
            for sub_col in range(3):
                button = tk.Button(
                    parent_frame,
                    text='',
                    font=('Helvetica', 12),
                    width=4,
                    height=2,
                    command=lambda mr=main_row, mc=main_col, sr=sub_row, sc=sub_col: self.on_button_click(mr, mc, sr, sc)
                )
                button.grid(row=sub_row, column=sub_col)
                # Store the button with its coordinates
                self.buttons[(main_row, main_col, sub_row, sub_col)] = button

    def on_button_click(self, main_row, main_col, sub_row, sub_col):
        try:
            # Enforce mini-grid restriction
            if self.game.currentBoard and (main_row, main_col) != self.game.currentBoard:
                raise ValueError(f"You must play in mini-grid {self.game.currentBoard}")

            # Check if spot is already taken
            if self.game.board[main_row, main_col][sub_row, sub_col] != 0:
                raise ValueError("Spot already taken.")

            # Make the move
            self.game.makeMove(main_row, main_col, sub_row, sub_col)
            self.update_button(main_row, main_col, sub_row, sub_col)

            # Check if the mini-board was won
            mini_winner = self.game.checkBoard(self.game.board[main_row, main_col])
            if mini_winner:
                self.mark_subboard_winner(main_row, main_col, mini_winner)

            # Check for a winner
            winner = self.game.checkWinner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.root.destroy()  # Close the window
                return

            # Update the next mini-grid
            nextBoard = (sub_row, sub_col)
            if self.game.checkBoard(self.game.board[nextBoard]) != 0 or not np.any(self.game.board[nextBoard] == 0):
                self.game.currentBoard = None
            else:
                self.game.currentBoard = nextBoard

            self.current_player = self.game.player

        except ValueError as e:
            messagebox.showerror("Invalid Move", str(e))

    def update_button(self, main_row, main_col, sub_row, sub_col):
        button = self.buttons[(main_row, main_col, sub_row, sub_col)]
        button['text'] = 'X' if self.current_player == 1 else 'O'
        button['state'] = 'disabled'

    def mark_subboard_winner(self, main_row, main_col, winner):
        parent_frame = self.buttons[(main_row, main_col, 0, 0)].master
        # Remove all buttons in the subboard
        for widget in parent_frame.winfo_children():
            widget.destroy()
        # Display the winner in the center of the mini-board
        label = tk.Label(
            parent_frame,
            text='X' if winner == 1 else 'O',
            font=('Helvetica', 24),
            fg='red' if winner == 1 else 'blue'
        )
        label.pack(expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameGUI(root)
    root.mainloop()
