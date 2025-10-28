**🧠 Algorithm Implementation Collection**

This repository contains implementations of fundamental algorithms in Artificial Intelligence and Computer Science.
Each algorithm is clearly implemented with well-documented code and examples to help you understand how they work in practice.

---------------------------------------------------

📚 Table of Contents
1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)
3. Depth-Limited Search (DLS)
4. Iterative Deepening Search (IDS)
5. Best-First Search
6. Beam Search
7. Bidirectional Search
8. Bidirectional Path Search
9. Hill Climbing
10. Minimax Algorithm
11. Alpha-Beta Pruning

---------------------------------------------------

🔍 Breadth-First Search (BFS)

How it Works:
BFS explores all neighboring nodes at the current depth before moving deeper. It uses a queue data structure.

Steps:
1. Start from the source node
2. Visit all immediate neighbors
3. Move to the next level
4. Mark visited nodes

Applications:
- Shortest path in unweighted graphs
- Web crawlers
- Network broadcasting
- Social networks (friend-of-friend search)

Complexity:
Time: O(V + E)
Space: O(V)

Example:
Input Graph:
A -> B, C
B -> D, E, F
C -> G
F -> H
G -> I

Output: A B C D E F G H I

---------------------------------------------------

🌲 Depth-First Search (DFS)

How it Works:
DFS explores as deep as possible along one path before backtracking. It uses a stack or recursion.

Applications:
- Path finding
- Topological sorting
- Cycle detection
- Maze solving

Complexity:
Time: O(V + E)
Space: O(V)

Example:
Input Graph:
A -> B, G
B -> C, D, E
E -> F
G -> H
H -> I

Output: A G H I B E F D C

---------------------------------------------------

⚙️ Depth-Limited Search (DLS)

How it Works:
A variant of DFS that stops when a depth limit is reached.

Applications:
- Fixed-depth game trees
- Resource-limited searches
- Infinite-path avoidance

Complexity:
-Time: O(b^d)
-Space: O(d)

Example:
-Start: 0, Target: 9, Max Depth: 3
-Output: 0 1 2 5
-Target not found within depth

---------------------------------------------------

🔁 Iterative Deepening Search (IDS)

How it Works:
Combines BFS’s completeness with DLS’s low memory. Repeats DLS with increasing depth limits.

Applications:
- Game trees
- Pathfinding with unknown depth

Complexity:
- Time: O(b^d)
- Space: O(d)

Example:
Depth 0: 0

Depth 1: 0 1 2

Depth 2: 0 1 3 4 2 5 6

Depth 3: 0 1 3 7 4 2 5 8 6

Depth 4: 0 1 3 7 4 2 5 8 9

Target found at depth 4

---------------------------------------------------

💡 Best-First Search

How it Works:
Selects the path that appears best using a heuristic function (h(n)).
Uses a priority queue for node selection.

Applications:
- GPS navigation
- Robot pathfinding
- AI games

Complexity:
- Time: O(b^m)
- Space: O(b^m)

Example:
- Output: 0 1 3 8 9

---------------------------------------------------

🎯 Beam Search

How it Works:
Similar to Best-First Search but limits the number of nodes considered at each level (beam width).

Applications:
- Machine translation
- Speech recognition
- Image captioning

Complexity:
- Time: O(b × k)
- Space: O(b)

Example:
- Start: 0, Goal: 7, Beam width: 2
- Output: Goal found at node 7

---------------------------------------------------

🔄 Bidirectional Search

How it Works:
Runs two searches — forward from start and backward from goal — meeting in the middle.

Applications:
- Shortest path
- Route planning
- Social graph search

Complexity:
- Time: O(b^(d/2))
- Space: O(b^(d/2))

Example:
- Start: 0, Target: 9
- Output: Target found at depth 3

---------------------------------------------------

🧩 Bidirectional Path Search

How it Works:
Extends bidirectional search by reconstructing the full path once the two searches meet.

Applications:
- GPS systems
- Robot motion planning
- Game pathfinding

Complexity:
- Time: O(b^(d/2))
- Space: O(b^(d/2))

Example:
- Output: Path: 0 2 5 9
- Path length: 3

---------------------------------------------------

🏔 Hill Climbing

How it Works:
A local search algorithm that iteratively improves the solution by moving to better neighboring states.

Applications:
- Feature selection
- Neural network optimization
- Job scheduling

Complexity:
- Time: Variable (can get stuck in local optima)
- Space: O(1)

Example:
- Function: f(x) = -x² + 10x
- Best found: x = 5, f(x) = 25

---------------------------------------------------

🎮 Minimax Algorithm

How it Works:
Used in two-player games. Assumes both players play optimally and evaluates all possible outcomes.

Applications:
- Chess, Checkers, Tic-Tac-Toe
- Decision making
- Game theory

Complexity:
- Time: O(b^d)
- Space: O(bd)

Example:
- Leaf node scores: [5, 6, 7, 4, 5, 3, 6, 6]
- Best score: 5

---------------------------------------------------

⚡ Alpha-Beta Pruning

How it Works:
Optimization of Minimax that prunes branches which can’t affect the final decision.

Applications:
- Game engines (e.g., Chess AI)
- Decision trees
- Adversarial search

Complexity:
- Time: O(b^(d/2)) (best case)
- Space: O(bd)

Example:
- Output: Optimal value using Alpha-Beta Pruning: 6

---------------------------------------------------

🧾 Author

Nishat Anjum Eva

📧 AI Algorithm Implementation Project
