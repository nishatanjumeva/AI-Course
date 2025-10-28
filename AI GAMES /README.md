# 🎮 AI Game Collection (Python)

🤖 This project includes three classic AI-based games — **Chess**, **Tic-Tac-Toe**, and **Rock Paper Scissors** — each powered by the Minimax Algorithm (with Alpha-Beta Pruning where applicable) to make intelligent decisions.

---

## 🧠 Overview

This project focuses on how Artificial Intelligence search algorithms can be applied in real-time games. Core AI features used in these games include:

* Minimax Algorithm
* Alpha-Beta Pruning
* Heuristic Evaluation
* Depth-Limited Search
* Simple GUI (tkinter / pygame)

All games share a similar UI flow and organized code structure.

---

## 🎯 Games Included

### 1) Chess (Simplified Version)

**Description:**
A turn-based simplified chess engine that predicts the next best move by evaluating multiple future board states.

**Algorithms Used:**

* Minimax
* Alpha-Beta Pruning
* Depth-Limited Search
* Piece-Value & Positional Heuristic

**How It Works:**

1. AI generates all legal moves.
2. Board scoring function evaluates each move.
3. Minimax selects the best move.
4. Alpha-Beta pruning skips unnecessary branches to improve speed.

> Note: Optional features like en-passant, castling, pawn promotion can be added depending on your implementation.

---

### 2) Tic-Tac-Toe

**Description:**
Classic 3×3 board game where the AI is unbeatable using full Minimax search.

**Algorithms Used:**

* Minimax (Full Game Tree)
* Alpha-Beta Pruning (Performance Optimization)

**How It Works:**

* Board is represented as a 3×3 matrix.
* AI simulates every possible move recursively.
* Selects the optimal move to ensure win/draw.

---

### 3) Rock Paper Scissors

**Description:**
Rock-Paper-Scissors with improved AI that can detect patterns instead of random guessing.

**AI Techniques (choose your approach):**

* Random baseline
* Pattern-based heuristic
* History-based prediction (optional upgrade)

---

## ✨ Main Features

* Common UI style for all games
* AI vs Human mode
* Tunable search depth
* Playable GUI experience

---

## 🧰 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/AI-Game-Collection.git
cd AI-Game-Collection

# Create virtual environment (optional but recommended)
python -m venv venv
# Windows
venv\\Scripts\\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Typical dependencies (example):

```
pygame
numpy
python-chess  # optional if used
```

> Tkinter usually comes pre-installed with Python.

---

## ▶️ Run the Games

Top-level launcher script:

```bash
python run_game.py
```

Or launch each game individually:

```bash
python run_chess.py
python run_tictactoe.py
python run_rps.py
```

---

## 🗂️ Suggested Folder Structure

```
AI-Game-Collection/
├─ README.md
├─ requirements.txt
├─ run_game.py
├─ games/
│  ├─ chess/
│  │  ├─ board.py
│  │  ├─ ai.py
│  │  └─ gui.py
│  ├─ tictactoe/
│  │  ├─ game.py
│  │  ├─ ai.py
│  │  └─ gui.py
│  └─ rps/
│     ├─ game.py
│     ├─ ai.py
│     └─ gui.py
└─ assets/
   └─ images/
```

---

## 🛠️ Customization Tips

* **Chess:** Using `python-chess` can simplify legal move generation.
* **Tic-Tac-Toe:** Full search is lightweight — 100% optimal AI.
* **RPS:** Try Markov models or frequency analysis to improve prediction.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`feature/your-feature`)
3. Add your improvements and test
4. Submit a pull request

---

## 📄 License

MIT License — see the `LICENSE` file for details.

---

## 📬 Contact

Feel free to open issues or submit pul
