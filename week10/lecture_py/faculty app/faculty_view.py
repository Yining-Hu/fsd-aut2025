import tkinter as tk 
from controller import StudentController

root = tk.Tk()
root.geometry("300x300")
root.title("Faculty GUI")
root.configure(bg='#607b8d')
root.resizable(False,False)

controller = StudentController(root)
listVar = tk.Variable(value=controller.students())
studentList = tk.Listbox(root,listvariable=listVar)
studentList.pack(fill=tk.BOTH,expand=True,padx=20,pady=40)

selectBtn = tk.Button(root,text='Generate Report', bg='#252525', fg='#ffc107',
                      font='Helvetica 12 bold',
                      command=lambda: controller.select_student(studentList))

selectBtn.pack(padx=5,pady=5,side='bottom')

root.mainloop()
