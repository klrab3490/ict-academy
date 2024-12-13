from tkinter import *

window = Tk()
window.title("Button")
window.geometry("500x500+150+150")

r1 = StringVar()
r2 = StringVar()
r3 = StringVar()
def click():
    print(int(r1.get()))
    print(int(r2.get()))
    print(int(r3.get()))

lb1 = Label(window, text="Select Gender: ").pack()
Checkbutton(window,text="Male", variable=r1, onvalue="0", offvalue="Not Checked").pack()
Checkbutton(window,text="Female", variable=r2, onvalue="1", offvalue="Not Checked").pack()
Checkbutton(window,text="Others", variable=r3, onvalue="2", offvalue="Not Checked").pack()
btn1 = Button(window, text="Select Gender", command=click).pack()


window.mainloop()

