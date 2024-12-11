from tkinter import *

window = Tk()

window.title("Tic-Tac-Toe")
window.geometry("250x210")
window.resizable(False, False)
window.configure(bg="#616161")

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
        btn.configure(bg="#00BCD4")
    else:
        tiles[loc] = player1
        text.set(player1)
        btn.configure(bg="#FFCC80")
    
    # Disable the button after the move
    btn.configure(state="disabled")
    
    mov += 1
    check_winner()
    if mov == 9:
        result_label.config(text="Tie")

# Function to check for a win
def check_winner():
    winner = None
    for condition in win_conditions:
        if tiles[condition[0]] == tiles[condition[1]] == tiles[condition[2]] and tiles[condition[0]] != "_":
            winner = tiles[condition[0]]
            break
    
    if winner:
        # Show a message when there's a winner
        result = f"Player {winner} wins!"
        result_label.config(text=result)
        disable_all_buttons()

# Function to disable all buttons after a win or draw
def disable_all_buttons():
    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        btn.configure(state="disabled")

# Label for result
lb = Label(window, text="Tic-Tac-Toe", font=("Arial", 16, "bold"), fg="#fff", bg="#616161").grid(row=0,column=0,columnspan=3)
result_label = Label(window, text="", font=("Arial", 16, "bold"), fg="#fff", bg="#616161")
result_label.grid(row=1, column=0, columnspan=3)

# Buttons
btn1 = Button(window, textvariable=text1, font=("Arial", 24, "bold"), fg="#fff", bg="#616100", command=lambda: add(0, text1, btn1), width=3)
btn1.grid(row=2, column=0)
btn2 = Button(window, textvariable=text2, font=("Arial", 24, "bold"), fg="#fff", bg="#616100", command=lambda: add(1, text2, btn2), width=3)
btn2.grid(row=2, column=1)
btn3 = Button(window, textvariable=text3, font=("Arial", 24, "bold"), fg="#fff", bg="#616100", command=lambda: add(2, text3, btn3), width=3)
btn3.grid(row=2, column=2)
btn4 = Button(window, textvariable=text4, font=("Arial", 24, "bold"), fg="#fff", bg="#616100", command=lambda: add(3, text4, btn4), width=3)
btn4.grid(row=3, column=0)
btn5 = Button(window, textvariable=text5, font=("Arial", 24, "bold"), fg="#fff", bg="#616100", command=lambda: add(4, text5, btn5), width=3)
btn5.grid(row=3, column=1)
btn6 = Button(window, textvariable=text6, font=("Arial", 24, "bold"), fg="#fff", bg="#616100", command=lambda: add(5, text6, btn6), width=3)
btn6.grid(row=3, column=2)
btn7 = Button(window, textvariable=text7, font=("Arial", 24, "bold"), fg="#fff", bg="#616100", command=lambda: add(6, text7, btn7), width=3)
btn7.grid(row=4, column=0)
btn8 = Button(window, textvariable=text8, font=("Arial", 24, "bold"), fg="#fff", bg="#616100", command=lambda: add(7, text8, btn8), width=3)
btn8.grid(row=4, column=1)
btn9 = Button(window, textvariable=text9, font=("Arial", 24, "bold"), fg="#fff", bg="#616100", command=lambda: add(8, text9, btn9), width=3)
btn9.grid(row=4, column=2)

# Main loop
window.mainloop()
