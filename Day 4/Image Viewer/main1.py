from tkinter import *
from PIL import Image, ImageTk 

window = Tk()

window.title("Image Viewer")
window.geometry("1350x660+0+0")
window.resizable(False,False)

count = 0

def next():
    global count
    count = (count + 1) % len(images)
    update_image()

def prev():
    global count
    count = (count - 1) % len(images)
    update_image()

def update_image():
    global count
    img = ImageTk.PhotoImage(images[count])
    lb1.config(image=img)
    lb1.image = img

images = [
    Image.open(r"/home/poweruser/Workshop/Rahul/Tkinder-App/ImageViewer/1.jpg").resize((1350,580)),
    Image.open(r"/home/poweruser/Workshop/Rahul/Tkinder-App/ImageViewer/2.jpeg").resize((1350,580)),
    Image.open(r"/home/poweruser/Workshop/Rahul/Tkinder-App/ImageViewer/3.jpg").resize((1350,580)),
    Image.open(r"/home/poweruser/Workshop/Rahul/Tkinder-App/ImageViewer/4.jpg").resize((1350,580)),
]

imgtk = ImageTk.PhotoImage(images[count])

lb1 = Label(window, image=imgtk, bg="#FFFFFF")
previous = Button(window, text="Previous ", font=("Arial", 24, "bold"), bg="#FBC02D", width=20, height=2, command=prev)
exit = Button(window, text="Exit ", font=("Arial", 24, "bold"), bg="#FBC02D", width=20, height=2, command=window.destroy)
next = Button(window, text="Next ", font=("Arial", 24, "bold"), bg="#FBC02D", width=20, height=2, command=next)

lb1.grid(row=0,column=0,columnspan=3)
previous.grid(row=1,column=0)
exit.grid(row=1,column=1)
next.grid(row=1,column=2)

window.mainloop()