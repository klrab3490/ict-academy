from tkinter import *

window = Tk()

window.title("Image Viewer")
window.geometry("1350x642+0+0")
window.resizable(False,False)

lb1 = Label(window, text="2",width=168, height=30, bg="#FFFFFF")
previous = Button(window, text="Previous ", font=("Arial", 24, "bold"), width=20, height=2)
exit = Button(window, text="Exit ", font=("Arial", 24, "bold"), width=20, height=2)
next = Button(window, text="Next ", font=("Arial", 24, "bold"), width=20, height=2)

lb1.grid(row=0,column=0,columnspan=3)
previous.grid(row=1,column=0)
exit.grid(row=1,column=1)
next.grid(row=1,column=2)

window.mainloop()