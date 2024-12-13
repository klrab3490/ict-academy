from tkinter import *

window = Tk()
window.title("Selector")
window.geometry("500x500+150+150")

states = [ "Andhra Pradesh", "Gujarat", "Kerala", "Karnataka", "Tamil Nadu" ]

clicked = StringVar()
clicked.set("Select State")

def click():
    print(clicked.get())

Label(window, text="Select State: ").pack()
OptionMenu(window, clicked, *states).pack()
Button(window, text="Select Gender", command=click).pack()

window.mainloop()