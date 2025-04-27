import time

class TicTacToeAI:
    def __init__(self, game):
        self.game = game
    
    def minimax(self, depth, is_maximizing):
        # Minimax algorithm implementation
        # Return the best score
        
        winner = self.game.check_winner()
        if winner == self.game.human_player:
            return -10 + depth  # Human wins (minimizing score)
        if winner == self.game.ai_player:
            return 10 - depth   # AI wins (maximizing score)
        if len(self.game.available_moves()) == 0:
            return 0            # Tie game
        
        if is_maximizing:
            best_score = float('-inf')
            for move in self.game.available_moves():
                self.game.board[move] = self.game.ai_player
                score = self.minimax(depth + 1, False)
                self.game.board[move] = 0
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.game.available_moves():
                self.game.board[move] = self.game.human_player
                score = self.minimax(depth + 1, True)
                self.game.board[move] = 0
                best_score = min(score, best_score)
            return best_score
    
    def minimax_alpha_beta(self, depth, is_maximizing, alpha, beta):
        # Minimax with alpha-beta pruning
        
        winner = self.game.check_winner()
        if winner == self.game.human_player:
            return -10 + depth
        if winner == self.game.ai_player:
            return 10 - depth
        if len(self.game.available_moves()) == 0:
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for move in self.game.available_moves():
                self.game.board[move] = self.game.ai_player
                score = self.minimax_alpha_beta(depth + 1, False, alpha, beta)
                self.game.board[move] = 0
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Beta cutoff
            return best_score
        else:
            best_score = float('inf')
            for move in self.game.available_moves():
                self.game.board[move] = self.game.human_player
                score = self.minimax_alpha_beta(depth + 1, True, alpha, beta)
                self.game.board[move] = 0
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Alpha cutoff
            return best_score
    
    def get_best_move(self, use_alpha_beta=False):
        # Find the best move using minimax or alpha-beta pruning
        
        best_score = float('-inf')
        best_move = None
        
        start_time = time.time()
        for move in self.game.available_moves():
            self.game.board[move] = self.game.ai_player
            
            if use_alpha_beta:
                score = self.minimax_alpha_beta(0, False, float('-inf'), float('inf'))
            else:
                score = self.minimax(0, False)
                
            self.game.board[move] = 0
            
            if score > best_score:
                best_score = score
                best_move = move
        
        end_time = time.time()
        algorithm = "Alpha-Beta Pruning" if use_alpha_beta else "Minimax"
        print(f"AI ({algorithm}) took {end_time - start_time:.4f} seconds")
        
        return best_move