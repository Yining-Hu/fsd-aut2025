from controller import Controller
import tkinter as tk
import tkinter.messagebox as mb

class ConfirmationView(tk.Toplevel):
    def __init__(self, master, msg):
        super().__init__(master=master)
        self.title("Confirmation Window")
        self.geometry("300x200")
        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry("+%d+%d" % (x+300, y))
        self.configure(bg='#607b8d')
        self.resizable(False, False)
        label = tk.Label(self, text=msg, fg='#ffc107',
                         font='Helvetica 12 bold', bg='#607b8d')
        label.place(relx=0.5, rely=0.5, anchor='center')
        closeBtn = tk.Button(self, text="Close", 
                             bg='#252525', fg='#ffc107',
                             font='Helvetica 10 bold',
                             command=lambda: self.destroy())
        closeBtn.pack(padx=5, pady=5, side='bottom')


class LoginFrame(tk.LabelFrame):
    def clear(self):
        self.emailField.delete(0, tk.END)
        self.passwordField.delete(0, tk.END)
        
    def login(self,master,model):
        user = model.match(self.emailText.get(), self.passwordTxt.get())
        if user != None:
            info = f"Welcome {user.name}"
            ConfirmationView(master, info)
            Controller.save(user)
            self.clear()
        else:
            info = "Incorrect email or password"
            mb.showerror(title="Login Error", message=info)
            self.clear()               
   
    def __init__(self, master,model) -> None:
        super().__init__(master)
        self.box = tk.LabelFrame(master, text='Sign In', bg='#607b8d', fg='white',
                            padx=20, pady=20, font='Helvetica 10 bold')
        self.box.columnconfigure(0, weight=1)
        self.box.columnconfigure(1, weight=3)
        self.box.place(rely=0.5, relx=0.5, anchor='center')

        self.emailLbl = tk.Label(self.box, text="Email:", justify='left', fg='#ffc107',
                                 font='Helvetica 12 bold', bg='#607b8d')
        self.emailLbl.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

        self.passwordLbl = tk.Label(self.box, text="Password:", fg='#ffc107',
                               font='Helvetica 12 bold', bg='#607b8d')
        self.passwordLbl.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

        self.emailText = tk.StringVar()
        self.emailField = tk.Entry(self.box, textvariable=self.emailText)
        self.emailField.grid(column=1, row=0, padx=5, pady=5)
        self.emailField.focus()

        self.passwordTxt = tk.StringVar()
        self.passwordField = tk.Entry(
            self.box, textvariable=self.passwordTxt, show="*")
        self.passwordField.grid(column=1, row=1, padx=5, pady=5)
        
        self.loginBtn = tk.Button(self.box, text="Login",
                                  bg='#252525', fg='#ffc107',
                                  font='Helvetica 10 bold',
                                  command= lambda: self.login(master,model))
        self.loginBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.cancelBtn = tk.Button(self.box,
                                   bg='#252525', fg='#ffc107',
                                   font='Helvetica 10 bold',
                                   text="Cancel", command=lambda: master.quit())
        self.cancelBtn.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)



        
