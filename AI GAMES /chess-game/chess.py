# chess_ai.py
import tkinter as tk
import random
from tkinter import messagebox

CELL = 64
LIGHT = "#EEEED2"
DARK = "#769656"

# Unicode Chess symbols
PIECE = {
    'r':'♜','n':'♞','b':'♝','q':'♛','k':'♚','p':'♟',
    'R':'♖','N':'♘','B':'♗','Q':'♕','K':'♔','P':'♙',' ': ' '
}

START = [
    list("rnbqkbnr"),
    list("pppppppp"),
    list("        "),
    list("        "),
    list("        "),
    list("        "),
    list("PPPPPPPP"),
    list("RNBQKBNR")
]

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess - User vs AI")
        self.canvas = tk.Canvas(root, width=8*CELL, height=8*CELL)
        self.canvas.pack()
        self.status = tk.Label(root, text="White (You) to move", font=("Arial",12))
        self.status.pack()
        self.board = [r[:] for r in START]
        self.selected = None
        self.turn = 'white'
        self.canvas.bind("<Button-1>", self.click)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for r in range(8):
            for c in range(8):
                color = LIGHT if (r+c)%2==0 else DARK
                self.canvas.create_rectangle(c*CELL, r*CELL, (c+1)*CELL, (r+1)*CELL, fill=color, outline="")
                p = self.board[r][c]
                if p != ' ':
                    self.canvas.create_text(c*CELL+CELL/2, r*CELL+CELL/2,
                                            text=PIECE[p], font=("Arial",36))
        if self.selected:
            r,c=self.selected
            self.canvas.create_rectangle(c*CELL, r*CELL, (c+1)*CELL, (r+1)*CELL,
                                         outline="yellow", width=3)

    def click(self, event):
        if self.turn!='white':
            return
        c=event.x//CELL
        r=event.y//CELL
        if not(0<=r<8 and 0<=c<8):return
        p=self.board[r][c]
        if self.selected is None:
            if p!=' ' and p.isupper():
                self.selected=(r,c)
                self.draw_board()
        else:
            sr,sc=self.selected
            if (sr,sc)==(r,c):
                self.selected=None
                self.draw_board()
                return
            if self.is_legal(sr,sc,r,c):
                self.move(sr,sc,r,c)
                self.selected=None
                self.turn='black'
                self.draw_board()
                self.root.after(600,self.ai_move)
            else:
                self.selected=None
                self.draw_board()

    def move(self,sr,sc,r,c):
        self.board[r][c]=self.board[sr][sc]
        self.board[sr][sc]=' '

    def is_legal(self,sr,sc,r,c):
        piece=self.board[sr][sc]
        target=self.board[r][c]
        if target!=' ' and target.isupper()==piece.isupper():
            return False
        return True  # simple move rules ignored for now

    def ai_move(self):
        moves=self.get_all_moves('black')
        if not moves:
            messagebox.showinfo("Game Over","You Win! AI has no moves.")
            self.root.quit()
            return
        move=random.choice(moves)
        sr,sc,r,c=move
        self.move(sr,sc,r,c)
        self.turn='white'
        self.draw_board()
        if not self.king_alive('K'):
            messagebox.showinfo("Game Over","AI Wins! Your king captured.")
            self.root.quit()

    def get_all_moves(self,side):
        moves=[]
        for r in range(8):
            for c in range(8):
                p=self.board[r][c]
                if p==' ':continue
                if (side=='white' and p.isupper()) or (side=='black' and p.islower()):
                    for dr in range(-1,2):
                        for dc in range(-1,2):
                            if dr==0 and dc==0:continue
                            nr, nc=r+dr, c+dc
                            if 0<=nr<8 and 0<=nc<8:
                                t=self.board[nr][nc]
                                if t==' ' or t.isupper()!=p.isupper():
                                    moves.append((r,c,nr,nc))
        return moves

    def king_alive(self,k):
        for r in self.board:
            if k in r:
                return True
        return False

if __name__=="__main__":
    root=tk.Tk()
    ChessGame(root)
    root.mainloop()
