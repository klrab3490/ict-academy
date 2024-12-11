from tkinter import *

# Initialize the main application window
window = Tk()

# Set the window title and size
window.title("Demo App")
window.geometry("600x400+100+150")  # Window size and position
window.resizable(True, False)  # Allow resizing horizontally, but not vertically
window.configure(bg="#616161")  # Set the background color of the window

# Create two StringVar variables to hold dynamic values
var1 = StringVar()  # This will hold the main number displayed
var1.set(0)  # Set the initial value of var1 to 0
var2 = StringVar()  # This will hold the value from the entry box
var2.set("-")  # Set the initial value of var2 to "-"
 
# Create a Label widget to display the number (lb1)
lb1 = Label(window, textvariable=var1, font=("Arial", 24, "bold"), fg="#fff", bg="#616161")
lb1.grid(row=0, column=0)  # Position lb1 at row 0, column 0 of the grid layout

# Create another Label widget to display the content of var2 (lb2)
lb2 = Label(window, textvariable=var2, font=("Arial", 24, "bold"), fg="#fff", bg="#616161")
lb2.grid(row=1, column=1)  # Position lb2 at row 1, column 1 of the grid layout

# Function to increment the number in var1 when the button is clicked
def click():
    var1.set(int(var1.get()) + 1)  # Increment var1 by 1
    lb2.config(text=var2.get())  # Update lb2 to show the current value of var2

# Function to clear the number and reset var2 when the "Delete" button is clicked
def clearNumber():
    var1.set(0)  # Reset var1 to 0
    var2.set("-")  # Reset var2 to "-"
    lb2.config(text="")  # Clear the text in lb2 (no display text)

# Button
btn1 = Button(window, text="Increment", font=("Arial", 24, "bold"), fg="#fff", bg="#616100", command=click) # Create the "Increment" button, which calls the click() function when pressed
btn2 = Button(window, text="Delete", font=("Arial", 24, "bold"), fg="#fff", bg="#616100", command=clearNumber) # Create the "Delete" button, which calls the clearNumber() function when pressed

# Create an Entry widget to allow the user to input a value, tied to var2
entry = Entry(window, textvariable=var2)
entry.grid(row=1, column=0)  # Position the entry widget at row 1, column 0 of the grid layout

# Position the buttons in the window
btn1.grid(row=0, column=1)  # Position the "Increment" button at row 0, column 1
btn2.grid(row=1, column=2)  # Position the "Delete" button at row 1, column 2

# Start the Tkinter event loop, which keeps the window open
window.mainloop()
