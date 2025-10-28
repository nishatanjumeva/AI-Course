import tkinter as tk
from tkinter import messagebox
import copy

class TicTacToeAI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe: Player vs AI")
        self.window.resizable(False, False)
        self.current_turn = "X"  # Player always X
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_dashboard()
        self.window.mainloop()

    def create_dashboard(self):
        self.status_label = tk.Label(self.window, text="Player X's Turn", font=("Arial", 18), bg="#1E1E1E", fg="white", width=25, pady=10)
        self.status_label.pack()

        frame = tk.Frame(self.window, bg="#121212")
        frame.pack(padx=10, pady=10)

        for r in range(3):
            for c in range(3):
                btn = tk.Button(frame, text="", font=("Arial", 40), width=5, height=2, bg="#FFEB3B", fg="black",
                                activebackground="#FFC107",
                                command=lambda row=r, col=c: self.player_move(row, col))
                btn.grid(row=r, column=c, padx=5, pady=5)
                self.buttons[r][c] = btn

        self.reset_btn = tk.Button(self.window, text="Reset Game", font=("Arial", 14), bg="#03A9F4", fg="white", command=self.reset_game)
        self.reset_btn.pack(pady=10)

    def player_move(self, row, col):
        if self.board[row][col] == "" and self.current_turn == "X":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", fg="blue", bg="#B3E5FC")
            if self.check_winner(self.board, "X"):
                self.status_label.config(text="Player Wins!", bg="#4CAF50")
                self.disable_all_buttons()
                return
            elif self.is_draw(self.board):
                self.status_label.config(text="Draw!", bg="#9E9E9E")
                return
            else:
                self.current_turn = "O"
                self.status_label.config(text="AI's Turn", bg="#F44336")
                self.window.after(500, self.ai_move)  # small delay for AI

    def ai_move(self):
        move = self.best_move(self.board)
        if move:
            row, col = move
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O", fg="red", bg="#FFCDD2")
            if self.check_winner(self.board, "O"):
                self.status_label.config(text="AI Wins!", bg="#F44336")
                self.disable_all_buttons()
                return
            elif self.is_draw(self.board):
                self.status_label.config(text="Draw!", bg="#9E9E9E")
                return
            else:
                self.current_turn = "X"
                self.status_label.config(text="Player X's Turn", bg="#1E1E1E")

    def best_move(self, board):
        best_score = -float('inf')
        move = None
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = "O"
                    score = self.minimax(board, 0, False)
                    board[r][c] = ""
                    if score > best_score:
                        best_score = score
                        move = (r, c)
        return move

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(board, "O"):
            return 1
        elif self.check_winner(board, "X"):
            return -1
        elif self.is_draw(board):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == "":
                        board[r][c] = "O"
                        score = self.minimax(board, depth+1, False)
                        board[r][c] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == "":
                        board[r][c] = "X"
                        score = self.minimax(board, depth+1, True)
                        board[r][c] = ""
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, board, player):
        # Rows, columns and diagonals
        for r in range(3):
            if board[r][0] == board[r][1] == board[r][2] == player:
                return True
        for c in range(3):
            if board[0][c] == board[1][c] == board[2][c] == player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

    def is_draw(self, board):
        for row in board:
            if "" in row:
                return False
        return True

    def disable_all_buttons(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(state="disabled")

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_turn = "X"
        self.status_label.config(text="Player X's Turn", bg="#1E1E1E")
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", state="normal", bg="#FFEB3B", fg="black")

if __name__ == "__main__":
    TicTacToeAI()
