from tkinter import  *

root = Tk()
root.geometry("1100x600")
root.title("Paint")
root.resizable(False,False)
root.config(bg="#448AFF")

mymenu = Menu(root)
root.config(menu=mymenu)

def create():
    pass

file = Menu(mymenu)
mymenu.add_cascade(label="File",menu=file)
file.add_command(label="New", command=create)
file.add_separator()
file.add_command(label="Exit", command=root.quit)

edit = Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=edit)
edit.add_command(label="New Edit", command=create)
edit.add_command(label="Exit Edit", command=root.quit)

toolbar = Frame(root,width=1100,height=100, bg="#616161")
toolbar.grid(row=0,column=0)

pallet = Frame(root, width=1100, height=500, bg="#FFFFFF")
pallet.grid(row=1,column=0)

canvas = Canvas(pallet, width=1100, height=500)
canvas.grid(row=0,column=0)

# Add Shapes
# canvas.create_line(100,100,200,100)
# canvas.create_oval(400,100,200,300)

startPoint = [0, 0]

# Methods
def paint(event):
    global startPoint
    x = event.x
    y = event.y
    if startPoint[0]!=0 and startPoint[1]!=0:
        canvas.create_line(startPoint[0],startPoint[1],x,y,fill="green")

    startPoint= [x, y]

# Binding Canvas To Mouse
canvas.bind("<B1-Motion>", paint)

root.mainloop()
