from tkinter import *

window = Tk()
window.title("Button")
window.geometry("500x500+150+150")

r = StringVar()
def click():
    print(int(r.get()))

lb1 = Label(window, text="Select Gender: ").pack()
Radiobutton(window,text="Male", variable=r, value="0").pack()
Radiobutton(window,text="Female", variable=r, value="1").pack()
Radiobutton(window,text="Others", variable=r, value="2").pack()
btn1 = Button(window, text="Select Gender", command=click).pack()


window.mainloop()

