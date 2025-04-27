import time
from src.core.tictactoe import TicTacToe
from src.ai.algorithms import TicTacToeAI

def compare_algorithms():
    # Compare performance of Minimax vs Alpha-Beta Pruning
    game = TicTacToe()
    ai = TicTacToeAI(game)
    
    # Set up a board with some initial moves
    # This will make the comparison more meaningful
    game.board[0, 0] = 1   # X in top-left
    game.board[1, 1] = -1  # O in center
    
    print("Performance Comparison: Minimax vs. Alpha-Beta Pruning")
    print("\nCurrent board state:")
    game.print_board()
    
    # Test Minimax
    start_time = time.time()
    minimax_move = ai.get_best_move(use_alpha_beta=False)
    minimax_time = time.time() - start_time
    print(f"Minimax best move: {minimax_move}")
    print(f"Minimax time: {minimax_time:.4f} seconds")
    
    # Test Alpha-Beta Pruning
    start_time = time.time()
    alpha_beta_move = ai.get_best_move(use_alpha_beta=True)
    alpha_beta_time = time.time() - start_time
    print(f"Alpha-Beta best move: {alpha_beta_move}")
    print(f"Alpha-Beta time: {alpha_beta_time:.4f} seconds")
    
    # Results
    print("\nResults:")
    print(f"Alpha-Beta is {minimax_time/alpha_beta_time:.2f}x faster than Minimax")
    print(f"Both algorithms chose the same move: {minimax_move == alpha_beta_move}")