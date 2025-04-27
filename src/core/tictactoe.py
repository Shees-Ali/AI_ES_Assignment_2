import numpy as np

class TicTacToe:
    def __init__(self):
        # Initialize empty 3x3 board
        self.board = np.zeros((3, 3), dtype=int)
        self.human_player = 1    # Human is X (1)
        self.ai_player = -1      # AI is O (-1)
        
    def print_board(self):
        # Display the board
        symbols = {0: ' ', 1: 'X', -1: 'O'}
        print('-------------')
        for row in self.board:
            print('|', end=' ')
            for cell in row:
                print(f"{symbols[cell]} |", end=' ')
            print('\n-------------')
    
    def available_moves(self):
        # Return list of available positions as (row, col) tuples
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    moves.append((i, j))
        return moves
    
    def make_move(self, position, player):
        # Make a move on the board
        if self.board[position] == 0:
            self.board[position] = player
            return True
        return False
    
    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        # Return 1 if X wins, -1 if O wins, 0 if no winner yet
        
        # Check rows and columns
        for i in range(3):
            # Check row i
            if abs(np.sum(self.board[i, :])) == 3:
                return np.sum(self.board[i, :]) // 3
            
            # Check column i
            if abs(np.sum(self.board[:, i])) == 3:
                return np.sum(self.board[:, i]) // 3
        
        # Check diagonals
        diag_sum = np.sum(np.diag(self.board))
        if abs(diag_sum) == 3:
            return diag_sum // 3
        
        anti_diag_sum = np.sum(np.diag(np.fliplr(self.board)))
        if abs(anti_diag_sum) == 3:
            return anti_diag_sum // 3
        
        return 0  # No winner yet
    
    def is_game_over(self):
        # Check if game is over (winner or tie)
        if self.check_winner() != 0:
            return True
        
        # Check for tie (all spaces filled)
        if len(self.available_moves()) == 0:
            return True
            
        return False