# Importing tkinter module
from tkinter import *


# Creating the main window object
window = Tk()


# Set the title of the window
window.title("Demo App")  # This sets the title of the window to "Demo App"


# Set the size and position of the window
# The format is: width x height + x_coordinate + y_coordinate
window.geometry("600x400+100+150")  


# Set whether the window can be resizable
# Both True, True for resizing both horizontally and vertically
# Both True, False for resizing horizontally
# Both False, True for resizing vertically
# Both False, False for no resizing 
window.resizable(True,False)


# Set Background Color
window.configure(bg="#616161")


# Create a Label widget with the following properties:
'''
- Text: "Hello World"
- Font: Arial, size 24, bold
- Text color: white (fg="#fff")
- Background color: grey (bg="#616161")
- Width:
- Height:
'''
lb1 = Label(window, text="Hello World", font=("Arial", 24, "bold"),fg="#fff",bg="#616161",width=15, height=3)  
lb2 = Label(window, text="Hello World", font=("Arial", 24, "bold"),fg="#fff",bg="#616161")  

# Geometry Manager
''' Method 1: Using the pack geometry manager
lb1.pack()  
lb2.pack(padx=20, pady=20)  # Places lb2 with 20 pixels of padding around it
'''

''' Method 2: Using the grid geometry manager
lb1.grid(row=0, column=0)  # Places lb1 in the first row (0) and first column (0)
lb2.grid(row=1, column=1)  # Places lb2 in the second row (1) and third column (1)
'''

''' Method 3: Using the place geometry manager '''
lb1.place(x=0, y=0)  # Places lb1 at the position (0, 0) relative to its parent container (top-left corner)
lb2.place(x=100, y=50)  # Places lb2 at the position (100, 50) relative to its parent container (100 pixels right, 50 pixels down)


# Start the Tkinter event loop, which makes the window appear
window.mainloop()
