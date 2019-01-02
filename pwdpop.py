from tkinter import *
from tkinter import messagebox

class mypop(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.PIN = '2143'

        self.top = Toplevel(master, bg='tan', padx=4, pady=3)
        self.top.resizable(width=False, height=False)
        self.top.minsize(width=195, height=35)
        self.top.maxsize(width=195, height=35)
        self.label = Label(self.top, text='Password :', fg='brown', bg='tan', padx=1, pady=1, relief=FLAT)
        self.label.grid(row=0, column=0)
        self.entry=Entry(self.top, show='*', width=5)
        self.entry.grid(row=0, column=1)
        self.lbl = Label(self.top, text='(4 digit)', fg='brown', bg='tan', relief=FLAT)
        self.lbl.grid(row=0, column=2)
        self.button = Button(self.top, text='ENTER', bg='orange', command=self.LogIn)
        self.button.grid(row=0, column=3)

        #self.value = self.entry.get()
    def LogIn(self):
        if self.PIN == self.entry.get():
            self.top.destroy()
        else:
            messagebox.askretrycancel('Wrond Pin', 'Try again!')
