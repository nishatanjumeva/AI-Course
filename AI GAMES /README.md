
## 🎯 Game 1 – Tic Tac Toe
## 🎯 Game 1 – Chess

**Description:**  
A classic 3×3 grid game where the player competes against an AI that never loses. The AI uses **Minimax with Alpha-Beta Pruning** to predict the best move.
A simplified Chess AI that can predict the next move using search algorithms. It evaluates possible future positions of the board to make intelligent decisions.

**Algorithm Used:**  
- **Minimax Algorithm:** Evaluates all possible moves and chooses the optimal one.  
- **Alpha-Beta Pruning:** Optimizes Minimax by skipping unnecessary branches.
- **Minimax Algorithm**
- **Alpha-Beta Pruning**
- **Depth-Limited Search**
- **Piece Value Evaluation Function**

**How It Works:**
1. The game board is represented as a 3×3 matrix.
2. AI simulates each move recursively.
3. Using Minimax, it chooses the move that maximizes its chance of winning.
4. Alpha-Beta pruning reduces the number of evaluated nodes.
1. AI generates all possible legal moves.
2. Evaluates board using a scoring function.
3. Uses Minimax to select the optimal move.
4. Alpha-Beta Pruning reduces unnecessary search.

---

@@ -52,22 +54,20 @@ A 7×6 grid-based game where players drop colored discs into a column. The AI an

---

## 🎯 Game 3 – Chess
## 🎯 Game 3 – Tic Tac Toe

**Description:**  
A simplified Chess AI that can predict the next move using search algorithms. It evaluates possible future positions of the board to make intelligent decisions.
A classic 3×3 grid game where the player competes against an AI that never loses. The AI uses **Minimax with Alpha-Beta Pruning** to predict the best move.

**Algorithm Used:**  
- **Minimax Algorithm**
- **Alpha-Beta Pruning**
- **Depth-Limited Search**
- **Piece Value Evaluation Function**
- **Minimax Algorithm:** Evaluates all possible moves and chooses the optimal one.  
- **Alpha-Beta Pruning:** Optimizes Minimax by skipping unnecessary branches.

**How It Works:**
1. AI generates all possible legal moves.
2. Evaluates board using a scoring function.
3. Uses Minimax to select the optimal move.
4. Alpha-Beta Pruning reduces unnecessary search.
1. The game board is represented as a 3×3 matrix.
2. AI simulates each move recursively.
3. Using Minimax, it chooses the move that maximizes its chance of winning.
4. Alpha-Beta pruning reduces the number of evaluated nodes.

