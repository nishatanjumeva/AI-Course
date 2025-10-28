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

**How It Works:**

* The AI analyzes the player's move history.
* It predicts the most likely upcoming move.
* Then selects the counter move to win.

**Markov Chain Strategy (Step-by-Step):**
4. Maintain a transition table like: `transition[last_move][next_move]` that counts how often each move follows another.
5. When the player makes a move, the AI checks which move typically comes after it and chooses the counter move to beat that predicted move.

---

## ✨ Main Features

* Common UI style for all games
* AI vs Human mode
* Tunable search depth
* Playable GUI experience

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

Feel free to open issues or submit pull requests on GitHub.

---

> Need help with adding screenshots, GitHub badges, or feature icons? Just ask! 😊
