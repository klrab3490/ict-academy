tiles = ["_"] * 9  # Initial empty board
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

# Print the board
def display():
    cnt = 0
    for i in range(3):
        for j in range(3):
            print(tiles[cnt], end="\t")
            cnt += 1
        print()
    print()

# Add player move to the board and track positions
def add(mov, loc):
    # Even moves are player 2's turn (O)
    if mov % 2 == 0:  
        tiles[loc] = player2
        print(f"{player2} added to position {loc}")
    # Odd moves are player 1's turn (X)
    else:  
        tiles[loc] = player1
        print(f"{player1} added to position {loc}")

# Check if a player has won
def checkWin():
    for condition in win_conditions:
        if tiles[condition[0]] == tiles[condition[1]] == tiles[condition[2]] and tiles[condition[0]] != "_":
            return tiles[condition[0]]  # Return 'X' or 'O' if found a winner
    return None  # No winner yet

# Main game loop
move = 1
while True:
    display()  # Show the current state of the board
    
    position = int(input("Enter Position (1-9): ")) - 1
    if position in range(9) and tiles[position] == "_":
        # Make the move if it's a valid position and not already taken
        add(move, position)
        winner = checkWin()
        
        if winner:
            display()
            print(f"Player {winner} wins!")
            break
        
        if move == 9:  # If all positions are filled, it's a draw
            display()
            print("It's a draw!")
            break
        
        move += 1  # Next player's turn
    else:
        print("Invalid move. Please try again.")
