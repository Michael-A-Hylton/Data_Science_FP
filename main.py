import numpy as np
from GameLoop import UltTicTacToe


def main():
    game = UltTicTacToe()
    while True:
        print(f"Player{game.player}'s turn." )

        print("Board:")
        print(game.board)
        validBoards = game.validMoves()
        print("Valid board squares:", validBoards)
        subBoardWins=np.zeros((3,3), dtype=int)
        for i in range(3):
            for j in range(3):
                subBoardWins[i,j]=game.checkBoard(game.board[i,j])
        if not game.validMoves():
            print("No valid moves left!")
            break
        # User input for move
        try:
            # Prompt user for move within the allowed mini-grid
            print("Enter your move as: main_row main_col main_row main_col")
            if game.currentBoard:
                print(f"Note: You must play in mini-grid {game.currentBoard}")
            else:
                print("You can choose any mini-grid.")
            userIn = input("Your move: ").strip()
            move = tuple(map(int, userIn.split()))
            if len(move) != 4:
                raise ValueError("Invalid input format.")

            row, col, subRow, subCol = move

            # Enforce mini-grid restriction
            if game.currentBoard and (row, col) != game.currentBoard:
                raise ValueError(f"Invalid mini-grid! You must play in: {game.currentBoard}")

            game.makeMove(row, col, subRow, subCol)
            nextBoard = (subRow, subCol)
            if game.checkBoard(game.board[nextBoard]) != 0 or not np.any(game.board[nextBoard] == 0):
                game.currentBoard = None
            else:
                game.currentBoard = nextBoard
            winner = game.checkWinner()
            if winner:
                print(f"Player {winner} wins!")
                break

        except ValueError as e:
            print(f"Invalid move: {e}. Please try again.")
            continue
            # Check for a winner

if __name__=="__main__":
    main()