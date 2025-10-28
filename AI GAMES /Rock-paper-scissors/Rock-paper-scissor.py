import tkinter as tk
from tkinter import messagebox
import random

# -----------------------------
# Game Logic (Minimax)
# -----------------------------
moves = ["rock", "paper", "scissors"]

winner = {
    "rock": {"rock": 0, "paper": -1, "scissors": 1},
    "paper": {"rock": 1, "paper": 0, "scissors": -1},
    "scissors": {"rock": -1, "paper": 1, "scissors": 0},
}

def minimax():
    best_value = float('-inf')
    best_moves = []

    for comp_move in moves:
        worst_case = float('inf')
        for player_move in moves:
            score = winner[player_move][comp_move]
            worst_case = min(worst_case, score)

        if worst_case > best_value:
            best_value = worst_case
            best_moves = [comp_move]
        elif worst_case == best_value:
            best_moves.append(comp_move)

    return random.choice(best_moves)

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Rock–Paper–Scissors (AI Minimax)")
root.geometry("450x400")
root.config(bg="#F0F0F0")  # Standard light gray background

# -----------------------------
# Title Label
# -----------------------------
title = tk.Label(root, text="🎮 Rock–Paper–Scissors (AI Minimax)",
                 font=("Helvetica", 16, "bold"), bg="#F0F0F0", fg="#333333")  # Dark text
title.pack(pady=15)

# -----------------------------
# Result Area
# -----------------------------
result_label = tk.Label(root, text="Make your move!", font=("Helvetica", 14),
                        bg="#F0F0F0", fg="#006400")  # Dark green
result_label.pack(pady=15)

computer_label = tk.Label(root, text="", font=("Helvetica", 12),
                          bg="#F0F0F0", fg="#8B0000")  # Dark red
computer_label.pack(pady=5)

# -----------------------------
# Game Logic on Button Click
# -----------------------------
def play(player_move):
    computer_move = minimax()
    computer_label.config(text=f"Computer chose: {computer_move.capitalize()}")

    result = winner[player_move][computer_move]

    if result == 1:
        result_label.config(text="✅ You Win!", fg="#228B22")  # Green
    elif result == -1:
        result_label.config(text="❌ Computer Wins!", fg="#B22222")  # Red
    else:
        result_label.config(text="🤝 It's a Draw!", fg="#DAA520")  # Goldenrod

# -----------------------------
# Buttons
# -----------------------------
button_frame = tk.Frame(root, bg="#F0F0F0")
button_frame.pack(pady=20)

btn_style = {"width": 14, "height": 2, "font": ("Helvetica", 12, "bold")}

rock_btn = tk.Button(button_frame, text="🪨 Rock", bg="#D3D3D3", fg="black",  # Light gray
                     command=lambda: play("rock"), **btn_style)
paper_btn = tk.Button(button_frame, text="📄 Paper", bg="#DCDCDC", fg="black",  # Gainsboro
                      command=lambda: play("paper"), **btn_style)
scissors_btn = tk.Button(button_frame, text="✂ Scissors", bg="#C0C0C0", fg="black",  # Silver
                         command=lambda: play("scissors"), **btn_style)

rock_btn.grid(row=0, column=0, padx=12)
paper_btn.grid(row=0, column=1, padx=12)
scissors_btn.grid(row=0, column=2, padx=12)

# -----------------------------
# Exit Button
# -----------------------------
exit_btn = tk.Button(root, text="Quit Game", command=root.destroy,
                bg="#A9A9A9", fg="white", font=("Helvetica", 12, "bold"),  # Dark gray
                width=16, height=1)
exit_btn.pack(pady=15)

# -----------------------------
# Run the App
# -----------------------------
root.mainloop()
