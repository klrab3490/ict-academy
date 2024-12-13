from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Get window size
window_width = 500
window_height = 500

# Calculate position for centering the window
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set window size and position
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.resizable(False, False)

def login():
    if username.get() == "admin" and password.get() == "admin":
        messagebox.showinfo("User Logged In", "Welcome User")
    elif username.get() != "admin":
        messagebox.showerror("User Error", "User Not Found")
    else:
        res = messagebox.askyesno("Wrong password", "Whether you need to enter all the details again?")
        print(res)
        if res:
            username.set("")
            password.set("")
        else:
            password.set("")

username = StringVar()
password = StringVar()

Label(root, text="Login Here", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=2)
Label(root, text="Username").grid(row=1, column=0)
Entry(root, textvariable=username).grid(row=1, column=1)
Label(root, text="Password").grid(row=2, column=0)
Entry(root, textvariable=password, show="*").grid(row=2, column=1)
Button(root, text="Login", width=30, command=login).grid(row=3, column=0, columnspan=2)

root.mainloop()
