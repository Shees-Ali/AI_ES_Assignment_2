import random
from src.core.tictactoe import TicTacToe
from src.ai.algorithms import TicTacToeAI

def play_game(use_alpha_beta=False):
    # Play a game of Tic-Tac-Toe against the AI
    
    game = TicTacToe()
    ai = TicTacToeAI(game)
    
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, the AI is O")
    print("Enter your moves as 'row col' (0-2 for both)")
    
    # Randomly decide who goes first
    current_player = random.choice([game.human_player, game.ai_player])
    
    game.print_board()
    
    while not game.is_game_over():
        if current_player == game.human_player:
            # Human player's turn
            valid_move = False
            while not valid_move:
                try:
                    row, col = map(int, input("Your move (row col): ").split())
                    if 0 <= row <= 2 and 0 <= col <= 2 and game.board[row, col] == 0:
                        game.board[row, col] = game.human_player
                        valid_move = True
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Enter row and column (0-2).")
        else:
            # AI player's turn
            print("AI is thinking...")
            
            move = ai.get_best_move(use_alpha_beta)
            
            game.board[move] = game.ai_player
        
        game.print_board()
        
        # Switch player
        current_player = -current_player
    
    # Game over
    winner = game.check_winner()
    if winner == game.human_player:
        print("You win!")
    elif winner == game.ai_player:
        print("AI wins!")
    else:
        print("It's a tie!")