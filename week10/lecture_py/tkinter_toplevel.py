import tkinter as tk
import tkinter.messagebox as mb

class NewWindow(tk.Toplevel):
    def __init__(self,master,msg):
        super().__init__(master=master)
        self.title("Confirmation Window")
        label = tk.Label(self,text=msg,fg="#ffc107",
                         font="Helvetica 12 bold",bg="#607b8d")
        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry("300x200+%d+%d" %(x+300,y))
        self.configure(bg="#607b8d")
        self.resizable(False,False)
        label.place(relx=0.5,rely=0.5,anchor="center")

def clear():
    emailField.delete(0,tk.END)
    passwordField.delete(0,tk.END)

def login():
    if(emailText.get() == "j.smith@example.com" and passwordText.get() == "user123"):
        info = "Correct email and password"
        NewWindow(root,info)
        clear()
    else:
        info = "Incorrect email or password"
        mb.showerror(title="Login Error",message=info)
        clear()

root = tk.Tk()
root.geometry("300x200")
root.title("TKinter GUI")
root.configure(bg="#607b8d")
root.resizable(False,False)

# Entry
box = tk.LabelFrame(root,text="Sign In",bg="#607b8d",fg="white",
                    padx=20,pady=20,font="Helvetica 10 bold")
box.columnconfigure(0,weight=1) # for grid
box.columnconfigure(1,weight=3)
box.place(relx=0.5,rely=0.5,anchor="center")

email = tk.Label(box,text="Email",justify="left",fg="#ffc107",
                 font="Helvetica 12 bold",bg="#607b8d")
email.grid(column=0,row=0,padx=5,pady=5,sticky="W")

password = tk.Label(box,text="Password",fg="#ffc107",
                    font="Helvetica 12 bold",bg="#607b8d")
password.grid(column=0,row=1,padx=5,pady=5,sticky="W")

emailText = tk.StringVar()
emailField = tk.Entry(box,textvariable=emailText)
emailField.grid(column=1,row=0,padx=5,pady=5)
emailField.focus()

passwordText = tk.StringVar()
passwordField = tk.Entry(box,textvariable=passwordText,show="*")
passwordField.grid(column=1,row=1,padx=5,pady=5)

cancelBtn = tk.Button(box,text="Cancel",command=lambda:root.quit())
cancelBtn.grid(column=1,row=3,sticky="W",padx=5,pady=5)
loginBtn = tk.Button(box,text="Login",command=login)
loginBtn.grid(column=1,row=3,sticky="E",padx=5,pady=5)

root.mainloop()