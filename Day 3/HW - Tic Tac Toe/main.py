from tkinter import *

window = Tk()

window.title("Tic-Tac-Toe")
window.geometry("250x260")
window.resizable(False, False)
window.configure(bg="#FF5722")

# Variables
text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()
text5 = StringVar()
text6 = StringVar()
text7 = StringVar()
text8 = StringVar()
text9 = StringVar()

tiles = ["_"] * 9
win_conditions = [
    [0, 1, 2],  # Top row
    [3, 4, 5],  # Middle row
    [6, 7, 8],  # Bottom row
    [0, 3, 6],  # Left column
    [1, 4, 7],  # Middle column
    [2, 5, 8],  # Right column
    [0, 4, 8],  # Diagonal top-left to bottom-right
    [2, 4, 6]   # Diagonal top-right to bottom-left
]

# Player symbols
player1 = "X"
player2 = "O"
mov = 1

# Function to add move
def add(loc, text, btn):
    global mov
    if mov % 2 == 0:
        tiles[loc] = player2
        text.set(player2)
        btn.configure(bg="#E64A19", fg="#212121")
    else:
        tiles[loc] = player1
        text.set(player1)
        btn.configure(bg="#FFCCBC", fg="#212121")
    
    # Disable the button after the move
    btn.configure(state="disabled")
    
    mov += 1
    check_winner()
    if mov == 9:
        result_label.config(text="Tie")
        reset.configure(state="active")

# Function to check for a win
def check_winner():
    winner = None
    for condition in win_conditions:
        if tiles[condition[0]] == tiles[condition[1]] == tiles[condition[2]] and tiles[condition[0]] != "_":
            button[condition[0]].configure(bg="#4CAF50", fg="#212121")
            button[condition[1]].configure(bg="#4CAF50", fg="#212121")
            button[condition[2]].configure(bg="#4CAF50", fg="#212121")
            winner = tiles[condition[0]]
            break
    
    if winner:
        # Show a message when there's a winner
        result = f"Player {winner} wins!"
        result_label.config(text=result)
        disable_all_buttons()

# Function to disable all buttons after a win or draw
def disable_all_buttons():
    reset.configure(state="active")
    for btn in [button[0], button[1], button[2], button[3], button[4], button[5], button[6], button[7], button[8]]:
        btn.configure(state="disabled", fg="#212121")

def clear():
    reset.configure(state="disabled")
    mov=1
    for text in [text1, text2, text3, text4, text5, text6, text7, text8, text9]:
        text.set("")
    for btn in [button[0], button[1], button[2], button[3], button[4], button[5], button[6], button[7], button[8]]:
        btn.configure(state="active", fg="#212121", bg="#616100")
    for i in range(9):
        tiles[i] = "_"      
    result_label.config(text="")

# Label for result
lb = Label(window, text="Tic-Tac-Toe", font=("Arial", 16, "bold"), fg="#212121", bg="#FF5722").grid(row=0,column=0,columnspan=3)
result_label = Label(window, text="", font=("Arial", 16, "bold"), fg="#212121", bg="#FF5722")
result_label.grid(row=1, column=0, columnspan=3)

# Buttons
reset = Button(window, text="Reset", font=("Arial", 24, "bold"), fg="#212121", bg="#616100", width=12, state="disabled", command=clear)
reset.grid(row=2, column=0, columnspan=3)
button = [
    Button(window, textvariable=text1, font=("Arial", 24, "bold"),fg="#212121", bg="#616100", command=lambda: add(0, text1, button[0]), width=3),
    Button(window, textvariable=text2, font=("Arial", 24, "bold"),fg="#212121", bg="#616100", command=lambda: add(1, text2, button[1]), width=3),
    Button(window, textvariable=text3, font=("Arial", 24, "bold"),fg="#212121", bg="#616100", command=lambda: add(2, text3, button[2]), width=3),
    Button(window, textvariable=text4, font=("Arial", 24, "bold"),fg="#212121", bg="#616100", command=lambda: add(3, text4, button[3]), width=3),
    Button(window, textvariable=text5, font=("Arial", 24, "bold"),fg="#212121", bg="#616100", command=lambda: add(4, text5, button[4]), width=3),
    Button(window, textvariable=text6, font=("Arial", 24, "bold"),fg="#212121", bg="#616100", command=lambda: add(5, text6, button[5]), width=3),
    Button(window, textvariable=text7, font=("Arial", 24, "bold"),fg="#212121", bg="#616100", command=lambda: add(6, text7, button[6]), width=3),
    Button(window, textvariable=text8, font=("Arial", 24, "bold"),fg="#212121", bg="#616100", command=lambda: add(7, text8, button[7]), width=3),
    Button(window, textvariable=text9, font=("Arial", 24, "bold"),fg="#212121", bg="#616100", command=lambda: add(8, text9, button[8]), width=3)
]

button[0].grid(row=3, column=0)
button[1].grid(row=3, column=1)
button[2].grid(row=3, column=2)
button[3].grid(row=4, column=0)
button[4].grid(row=4, column=1)
button[5].grid(row=4, column=2)
button[6].grid(row=5, column=0)
button[7].grid(row=5, column=1)
button[8].grid(row=5, column=2)

# Main loop
window.mainloop()
