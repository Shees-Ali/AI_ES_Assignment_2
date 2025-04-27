from src.ui.game_ui import play_game
from src.utils.performance import compare_algorithms

if __name__ == "__main__":
    print("What would you like to do?")
    print("1. Play Tic-Tac-Toe with Minimax AI")
    print("2. Play Tic-Tac-Toe with Alpha-Beta Pruning AI")
    print("3. Compare Minimax and Alpha-Beta Pruning performance")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        play_game(use_alpha_beta=False)
    elif choice == '2':
        play_game(use_alpha_beta=True)
    elif choice == '3':
        compare_algorithms()
    else:
        print("Invalid choice")