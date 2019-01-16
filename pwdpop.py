from tkinter import Tk, Button, Label, Text, Entry, Frame, Toplevel, END
from cr_f_iii import main_d

class mypop(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.top = Toplevel(master, bg='tan', padx=4, pady=3)
        self.top.protocol("WM_DELETE_WINDOW", self.disable_event)

        self.top.resizable(width=False, height=False)
        self.top.minsize(width=200, height=70)
        self.top.maxsize(width=200, height=70)
        self.labl = Label(self.top, text='Password :', width=7, fg='brown', bg='tan', padx=1, pady=1, relief='flat')
        self.labl.grid(row=0, column=0)
        self.entry=Entry(self.top, show='*', width=5)
        self.entry.grid(row=0,column=1)
        self.lbl = Label(self.top, text='(4 digit)', fg='brown', bg='tan', relief='flat')
        self.lbl.grid(row=0, column=2)
        self.button = Button(self.top, text='ENTER', bg='orange', command=self._login_btn_clickked)
        self.button.grid(row=0, column=3)
        self.ges = Text(self.top, width=20, height=2, fg='brown', state='disable', relief='flat')
        self.ges.grid(row=1, columnspan=4)

        self.pack()

    def _login_btn_clickked(self):
        password = self.entry.get()

        if password != "2143":
            self.ges.config(state='normal')
            te = "Wrong PIN Entered!\n(Hint 4 digit Pin!)"
            self.ges.delete(1.0, END)
            self.ges.insert(1.0, te)
            self.ges.config(state='disable')
            
        else:
            self.disable_event()
            main_d()


    def disable_event(self):
        self.top.destroy()
