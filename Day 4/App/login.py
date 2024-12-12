from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login")
root.geometry("500x500")
root.resizable(False,False)

def login():
    if username.get()=="admin" and password.get()=="admin":
        messagebox.showinfo("User Logged In","Welcome User")
    elif username.get()!="admin":
        messagebox.showerror("User Error","User NOt Found")
    else:
        res = messagebox.askyesno("Wrong password","Whether you need to enter all the details again?")
        print(res)
        if res:
            username.set("")
            password.set("")
        else:
            password.set("")

username = StringVar()
password = StringVar()

Label(root, text="Login Here", font=("Arial",36,"bold"), ).place(x=150,y=50)
Label(root, text="Username").place(x=50,y=150)
Entry(root, textvariable=username).place(x=250,y=150)
Label(root, text="password").place(x=50,y=250)
Entry(root, textvariable=password).place(x=50,y=250)

root.mainloop()