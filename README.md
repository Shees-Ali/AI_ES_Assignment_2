# Tic-Tac-Toe with AI

A command-line implementation of Tic-Tac-Toe with two AI algorithms: standard Minimax and Minimax with Alpha-Beta pruning.

## Features

- Play Tic-Tac-Toe against an AI opponent
- Two AI difficulty options:
  - Minimax: Guaranteed optimal play but slower
  - Alpha-Beta Pruning: Same optimal play but more efficient
- Performance comparison tool to see the speed difference between algorithms
- Clean, modular codebase for easy extension

## Project Structure

```
tic-tac-toe/
│
├── src/                      # Source code directory
│   ├── core/                 # Core game logic
│   │   └── tictactoe.py      # Game board and rules
│   │
│   ├── ai/                   # AI algorithms
│   │   └── algorithms.py     # Minimax and Alpha-Beta pruning
│   │
│   ├── ui/                   # User interface components
│   │   └── game_ui.py        # Game interface
│   │
│   └── utils/                # Utility functions
│       └── performance.py    # Performance comparison tools
│
├── main.py                   # Main entry point
├── requirements.txt          # Project dependencies
└── tests/                    # Test files (future expansion)
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script:
```
python main.py
```

You will be presented with three options:
1. Play against the Minimax AI
2. Play against the Alpha-Beta Pruning AI
3. Compare the performance of both algorithms

### Playing the Game

- You are X, the AI is O
- Enter your moves as "row col" (both 0-2)
- Example: "1 2" places your X in the middle row, right column

## How It Works

### Minimax Algorithm

The Minimax algorithm is a decision-making algorithm used in two-player games. It works by:
1. Exploring all possible future game states
2. Evaluating final states (win/loss/tie)
3. Working backward to determine the optimal move

### Alpha-Beta Pruning

Alpha-Beta pruning is an optimization technique for the Minimax algorithm that:
1. Reduces the number of nodes evaluated
2. Produces identical results to standard Minimax
3. Can be significantly faster, especially for deeper game trees

## Future Improvements

- Graphical user interface
- Adjustable AI difficulty levels
- Network play support
- Additional board sizes

## License

MIT