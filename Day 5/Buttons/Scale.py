from tkinter import *

window = Tk()
window.title("Selector")
window.geometry("500x500+150+150")

age = StringVar()

def click():
    print(age.get())

Label(window, text="Select Age: ").pack()
age = Scale(window, from_=18, to=80, orient=HORIZONTAL)
age.pack()
Button(window, text="Select Gender", command=click).pack()

window.mainloop()