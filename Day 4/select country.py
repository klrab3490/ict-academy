from tkinter import *

window = Tk()
window.title("Selector")
window.geometry("500x500+150+150")

states = [ "Andhra Pradesh", "Gujarat", "Kerala", "Karnataka", "Tamil Nadu" ]

r = StringVar()

def click():
    print(states[int(r.get())])

lb1 = Label(window, text="Select State: ").pack()
for i in range(len(states)):
    Radiobutton(window,text=states[i], variable=r, value=str(i)).pack()

btn1 = Button(window, text="Select Gender", command=click).pack()

window.mainloop()