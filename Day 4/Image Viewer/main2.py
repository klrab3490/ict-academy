from tkinter import *
from PIL import Image, ImageTk 
import glob

window = Tk()

window.title("Image Viewer")
window.geometry("1350x660+0+0")
window.resizable(False,False)

count = 0
path = r"/home/poweruser/Workshop/Rahul/Tkinder-App/ImageViewer/images/*"
images = glob.glob(path)

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
    img = Image.open(images[count]).resize((1350, 580))
    imgtk = ImageTk.PhotoImage(img)
    lb1.config(image=imgtk)
    lb1.image = imgtk

img = Image.open(images[count]).resize((1350, 580))
imgtk = ImageTk.PhotoImage(img)

lb1 = Label(window, image=imgtk, bg="#FFFFFF")
previous = Button(window, text="Previous ", font=("Arial", 24, "bold"), bg="#FBC02D", width=20, height=2, command=prev)
exit = Button(window, text="Exit ", font=("Arial", 24, "bold"), bg="#FBC02D", width=20, height=2, command=window.destroy)
next = Button(window, text="Next ", font=("Arial", 24, "bold"), bg="#FBC02D", width=20, height=2, command=next)

lb1.grid(row=0,column=0,columnspan=3)
previous.grid(row=1,column=0)
exit.grid(row=1,column=1)
next.grid(row=1,column=2)

window.mainloop()