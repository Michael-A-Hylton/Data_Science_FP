import numpy as np


class UltTicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3, 3, 3), dtype=int)
        self.currentBoard = None
        self.player = 1

    def checkBoard(self, miniBoard):
        for i in range(3):
            # Check rows
            if all(miniBoard[i, :] == miniBoard[i, 0]) and miniBoard[i, 0] != 0:
                return miniBoard[i, 0]
            # Check columns
            if all(miniBoard[:, i] == miniBoard[0, i]) and miniBoard[0, i] != 0:
                return miniBoard[0, i]  # Corrected assignment

        # Check main diagonal
        if all(miniBoard.diagonal() == miniBoard[0, 0]) and miniBoard[0, 0] != 0:
            return miniBoard[0, 0]
        # Check anti-diagonal
        if all(np.fliplr(miniBoard).diagonal() == miniBoard[0, 2]) and miniBoard[0, 2] != 0:
            return miniBoard[0, 2]

        return 0

    def makeMove(self, row, col, subRow, subCol):
        """Place a move on the board."""
        if self.board[row, col][subRow, subCol] != 0:
            raise ValueError("Spot already taken.")

        if self.checkBoard(self.board[row, col]) != 0:
            raise ValueError("This square has already been won")
        self.board[row, col][subRow, subCol] = self.player
        self.currentBoard = (subRow, subCol)  # Set the next mini-grid
        self.player = 2 if self.player == 1 else 1

        return 0

    def checkWinner(self):
        """Check for a winner in the main grid."""
        bigWinners = np.zeros((3, 3), dtype=int)
        for i in range(3):
            for j in range(3):
                bigWinners[i, j] = self.checkBoard(self.board[i, j])
        return self.checkBoard(bigWinners)

    def validMoves(self):
        if self.currentBoard:
            if np.any(self.board[self.currentBoard] == 0):
                return [self.currentBoard]
        return [(i, j) for i in range(3) for j in range(3) if np.any(self.board[i, j] == 0)]
