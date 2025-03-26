import tkinter as tk

class StudentView(tk.Toplevel):
    def __init__(self, master, info) -> None:
        super().__init__(master=master)
        self.title('Student Report')
        self.geometry('300x300')
        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry("+%d+%d" % (x+300,y))
        self.configure(bg='#607b8d')
        self.resizable(False,False)
        label = tk.Label(self,text=info,fg='#ffc107',
                         font='Helvetica 12 bold', bg='#607b8d')
        label.place(relx=0.5,rely=0.5,anchor='center')
        closeBtn = tk.Button(self,text='Close',bg='#252525',fg='#ffc107',
                             font='Helvetica 12 bold',
                             command=lambda: self.destroy())
        closeBtn.pack(padx=5,pady=20,side='bottom')