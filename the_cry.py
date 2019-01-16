#!/usr/bin/python3

# Mapenzi Mudimba
# Copyright 2018
#############################################
#   Basic programme for my personal journal #
#############################################
#===========================================

# importing modules
import os, sys, math
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Menu, Entry, Label, Frame, Tk, Button, END, Text
from tkinter import Scrollbar
from cr_f_ii import main_c
from pwdpop import mypop
from datetime import date
from idlelib.colorizer import ColorDelegator, color_config

class cryptor(object):
	def __init__(self, *args, **kwargs):
		self.root = root = Tk()

		self.menufont = ("Arial", 12, 'normal')
		self.MINIMUM_FONT_SIZE = 6
		self.MAXIMUM_FONT_SIZE = 100
		self.font_sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 30]
		self.txtfont = ['Lucida Console', 11, 'normal']

		# The icon 
		try: 
			root.wm_iconbitmap("hilma_1.ico") 
		except: 
			pass

		# The Title		
		try:
			root.wm_title('The Cryptor')
		except:
			pass
		
		# File Path
		try:
			self.__file = None
		except:
			pass

		# scrolledTx auto resizable 
		root.grid_rowconfigure(0, weight=1) 
		root.grid_columnconfigure(0, weight=1)
		root.grid_columnconfigure(1, minsize=100, weight=1)
		root.grid_columnconfigure(2, minsize=100, weight=1)

		# The menu
		self.menuBar = Menu(root)
		self.fileMenu = Menu(self.root, tearoff=0)
		self.fileMenu.add_command(label="New", 
							command=self.newFile, accelerator="Ctrl+N")	 
		
		# Open a already existing file 
		self.fileMenu.add_command(label="Open", 
							command=self.openFile, accelerator="Ctrl+O") 
		self.fileMenu.add_separator()
		# Save current file 
		self.fileMenu.add_command(label="Save", 
								command=self.saveFile, accelerator="Ctrl+S")	 

		self.fileMenu.add_command(label="Save As", 
								command=self.saveFileAs, accelerator="Ctrl+Shift+S")
				 
		self.fileMenu.add_separator()										 
		self.fileMenu.add_command(label="Exit", 
								command=self.quitApplication, accelerator="Ctrl+Q") 
		self.menuBar.add_cascade(label="File", 
							menu=self.fileMenu)	 
		
		self.editMenu = Menu(self.root, tearoff=0)
		self.editMenu.add_command(label="Undo", command=self.unDo, accelerator="Ctrl+Z")

		self.editMenu.add_command(label='Redo', command=self.reDo, accelerator='Ctrl+Y')

		# Feature of cut 
		self.editMenu.add_command(label="Cut", 
							command=self.cut, accelerator="Ctrl+X")			 
	
		# Feature of copy	 
		self.editMenu.add_command(label="Copy", 
							command=self.copy, accelerator="Ctrl+C")		 
		
		# Feature of paste 
		self.editMenu.add_command(label="Paste", 
							command=self.paste, accelerator="Ctrl+V")		 
		self.fileMenu.add_separator()
			
		# Feature of editing 
		self.menuBar.add_cascade(label="Edit", 
							menu=self.editMenu)	 
		
		self.fnMenu = Menu(self.root, tearoff=0)

		self.menuBar.add_cascade(menu=self.fontMenu(self.menuBar), label='Font')


		# Feature of Run
		self.runMenu = Menu(self.root, tearoff=0)
		self.runMenu.add_command(label="Run", command=self.run,
							accelerator="F5")
		
		self.menuBar.add_cascade(label='Run', menu=self.runMenu)

		# The notepad descriptions
		self.About = Menu(self.root, tearoff=0)	
		self.About.add_command(label="Help", 
							command=self.showAbout) 

		self.About.add_command(label="Welcome", 
							command=self.showWelcome) 

		# The notepad 
		self.About.add_command(label="Licences", 
								command=self.showLicence) 
		self.menuBar.add_cascade(label="About", 
							menu=self.About)

		self.root.config(menu=self.menuBar)
						
		###############
		# The Pane
		###############

		# The Date funct
		self.day = date.today()
		self.day.strftime('%D-%M-%Y')
		self.day1 = date.today()
		self.day1.strftime('%Y %m %d')

		#						#				#						#
		# Buttons and Labels	################# The text framework #
		#						#				#						#

		self.text_frame = text_frame = Frame(root,relief='ridge')
		self.scrolledTx = text = Text(text_frame, name='text', padx=5, pady=4, undo=True,
                                wrap='word', relief='ridge')
		
		color_config(text)
		
		self.vbar = vbar = Scrollbar(text_frame, orient='vertical', width=20, command=self.scrolledTx.yview)
		self.scrolledTx.configure(yscrollcommand=self.vbar.set)

		self.scrolledTx.tag_configure("line", font=self.txtfont, justify='right')

		self.li_num = TextLineNumbers(text_frame, width=30, bg='#ddf')
		self.li_num.attach(text)
		vbar.pack(side='right', fill='y')
		self.li_num.pack(side='left', fill='y')

		text_frame.pack(fill='both', expand=1)

		text['font'] = tuple(self.txtfont)
		shortcut = 'Control'
		text.bind_all('<%s-minus>' % shortcut, self.decrease_size)
		text.bind_all('<%s-underscore>' % shortcut, self.decrease_size)
		text.bind_all('<%s-equal>' % shortcut, self.increase_size)
		text.bind_all('<%s-plus>' % shortcut, self.increase_size)
		text.bind('<Control-MouseWheel>', self.update_mousewheel)
		text.bind('<Control-Button-4>', self.increase_size)
		text.bind('<Control-Button-5>', self.decrease_size)

		text.pack(fill='both', expand=1)

		self.statusBar = Label(root, bd=1, relief='ridge') 
		self.statusBar.pack(side='bottom', fill='x')
		self.corn = Label(self.statusBar, text='C\\/D', width=3, bg='#fff', padx=4, pady=4, relief='ridge')
		self.corn.pack(side='left')
		self.btn = Button(self.statusBar, text='Encrypt', bg='yellow', fg='blue', padx=10, pady=2, relief='raised', command=self.encry)
		self.btn.pack(side='left')
		self.butn = Button(self.statusBar, text='Decrypt', bg='yellow', fg='brown', padx=10, pady=2, relief='raised', command=self.decry)
		self.butn.pack(side='left')
		self.wedge = Label(self.statusBar, text='H',font=('Edwardian Script ITC', '12'), width=1, bg='#dcf', padx=4, pady=4, relief='flat', justify='left')
		self.wedge.pack(side='right')
		self.ti_bt = Label(self.statusBar, text=self.day, bg='#ddf', fg='brown', padx=4, pady=4, relief='ridge')
		self.ti_bt.pack(side='right')
		self.motba = Label(self.statusBar, text='[ x-0 : y-0 ]', width=15, padx=4, pady=4, relief='ridge')
		self.motba.pack(side='right')

		# The events	
		self.scrolledTx.bind('<Button-3>', self.pop_up)
		self.scrolledTx.bind("<<Change>>", self._on_change)
		self.scrolledTx.bind("<Configure>", self._on_change)
		self.scrolledTx.bind('<Motion>', self.motion)

		#################################################
		#	THE AREA FOR DEFINING ALL THE FUCNTIONS		#
		#################################################

	def _on_change(self, event):
		self.li_num.redraw()

	def pop_up(self, event):
		self.editMenu.post(event.x_root, event.y_root)

	def run(self):
		self.decry()

	def quitApplication(self):
		if messagebox.askyesno("Close Window!", "Do you really want to quit! \
		\nAny unsaved material will be lost"):
			self.root.destroy()

	def showAbout(self): 
		messagebox.showinfo("Cryptor","It is illegal to open documents without permission to do so.")

	def openFile(self):
		self.scrolledTx.config(state='normal')
		self.__file = askopenfilename(defaultextension=".txt", 
									filetypes=[("All Files","*.*"), 
										("Text Documents","*.txt")]) 

		if self.__file == "":
			
			# no file to open 
			self.__file = None
		else:
			
			# Open the file 
			# set the window title 
			self.root.title(os.path.basename(self.__file) + " - Cryptor") 
			self.scrolledTx.delete(1.0,END) 

			file = open(self.__file,"r") 
			self.scrolledTx.insert(1.0, file.read())

			file.close() 
		
	def newFile(self):
		self.scrolledTx.config(state='normal') 
		self.root.title("Untitled - Cryptor") 
		self.__file = None
		self.scrolledTx.delete(1.0,END)
		self.del_fi()
		self.op_fi() 

	def saveFile(self): 

		if self.__file == None: 
			# Save as new file 
			self.__file = asksaveasfilename(initialfile='Untitled.txt', 
											defaultextension=".txt", 
											filetypes=[("All Files","*.*"), 
												("Text Documents","*.txt")]) 

			if self.__file == "": 
				self.__file = None
			else: 
				
				# Try to save the file 
				file = open(self.__file,"w") 			
				file.write(self.scrolledTx.get(1.0,END)) 
				file.close() 
							
		else:

			file = open(self.__file,"w") 
			file.write(self.scrolledTx.get(1.0,END))
			file.close()

		# Change the window title 
		self.root.title(os.path.basename(self.__file) + " - Cryptor") 
        
	def saveFileAs(self):
		self.__file = asksaveasfilename(initialfile='Untitled.txt', 
								defaultextension=".txt", 
								filetypes=[("All Files","*.*"), 
									("Text Documents","*.txt")])
                
		# Try to save the file 
		file = open(self.__file,"w") 			
		file.write(self.scrolledTx.get(1.0,END))
		file.close() 
				
		# Change the window title 
		self.root.title(os.path.basename(self.__file) + " - Cryptor") 

	def unDo(self):
		self.scrolledTx.event_generate("<<Undo>>")

	def reDo(self):
		self.scrolledTx.event_generate("<<Reod>>")

	def cut(self): 
		self.scrolledTx.event_generate("<<Cut>>") 

	def copy(self): 
		self.scrolledTx.event_generate("<<Copy>>") 

	def paste(self): 
		self.scrolledTx.event_generate("<<Paste>>") 

	def decry(self):
		self.scrolledTx.config(state='normal')
		self.pwdpop = mypop(self.scrolledTx)
		self.scrolledTx.wait_window(self.pwdpop.top)
		xt = self.fi_let()
		self.scrolledTx.insert(1.0, xt)

	def sav_fi(self):
		flt = open(r'C:\\Users\\hazel\Desktop\\the_cry\\fil_et.txt', "w") 
		flt.write(self.scrolledTx.get(1.0, END)) 
		flt.close()

	def del_fi(self):
		delfi = open(r'C:\\Users\\hazel\Desktop\\the_cry\\fil_et.txt', 'w')
		delfi.write("")
		delfi.close()

	def op_fi(self):
		with open(r'C:\\Users\\hazel\Desktop\\the_cry\\cr_k_i.txt', 'w') as f:
			wr_data = f.write("")
			return wr_data
		
	def fi_let(self):
		with open(r'C:\\Users\\hazel\Desktop\\the_cry\\cr_k_i.txt') as fi:
			re_data = fi.read()
			return re_data

	def encry(self):
		self.scrolledTx.config(state='normal')
		if self.scrolledTx.get(1.0, END) != "":
			self.sav_fi()
			main_c()
			self.del_fi()
			self.op_fi()
			self.scrolledTx.delete(1.0, END)
		else:
			messagebox.showwarning('Blank Screen!', 'There is nothing to save!')
			self.newFile()

	def showWelcome(self):
		self.scrolledTx.config(state='normal')  
		file = r'C:\\Users\\hazel\\Desktop\\the_cry\\welcome.txt'
		fo = open(file)
		ts=fo.read()
		fo.read()
		self.scrolledTx.delete(1.0, END)
		self.scrolledTx.insert(1.0, ts)
		self.scrolledTx.config(state='disable')
		fo.close()

	def showLicence(self):
		messagebox.showinfo('Cryptor', "Mapenzi Mudimba, 2018.\n\nAllright reserved. \
		\nNo part may be exported into any media\nwithout consent from the author.")
	
	def fontMenu(self, master):
		menu = Menu(master, tearoff=0)
		menu.add_command(label="Decrease (C-'-')", command=self.decrease_size,
                        font=self.menufont)
		menu.add_command(label="Increase (C-'+')", command=self.increase_size,
                        font=self.menufont)
		menu.add_separator()

		for size in self.font_sizes:
			def resize(size=size):
				self.set_txtsize(size)
			menu.add_command(label=str(size), underline=0,
                             font=self.menufont, command=resize)
		return menu

	def set_txtsize(self, size):
		self.txtfont[1] = size
		self.scrolledTx['font'] = tuple(self.txtfont)

	def decrease_size(self, dummy=None):
		self.set_txtsize(max(self.txtfont[1] - 1, self.MINIMUM_FONT_SIZE))
		return 'break'

	def increase_size(self, dummy=None):
		self.set_txtsize(min(self.txtfont[1] + 1, self.MAXIMUM_FONT_SIZE))
		return 'break'

	def update_mousewheel(self, event):
		if event.delta < 0:
			return self.decrease_size()
		else:
			return self.increase_size()

	def motion(self, event):
  		self.motba.config(text="[X-%s : Y-%s]" % (event.x_root, event.y_root))

################################################
#
#	THE CLASS FOR LINE NUMBERS
#
################################################

class TextLineNumbers(tk.Canvas):
	def __init__(self, *args, **kwargs):
		tk.Canvas.__init__(self, *args, **kwargs)
		self.textwidget = None

	def attach(self, text_widget):
		self.textwidget = text_widget
		color_config(self.textwidget)

	def redraw(self, *args):
		'''redraw line numbers'''
		self.delete("all")

		i = self.textwidget.index("@0,0")
		while True :
			dline= self.textwidget.dlineinfo(i)
			if dline is None: break
			y = dline[1]
			linenum = str(i).split(".")[0]
			self.create_text(2,y,anchor="nw", text=linenum, fill='brown')
			i = self.textwidget.index("%s+1line" % i)

		# Refreshes the canvas widget 30fps
		self.after(30, self.redraw)

#############################################
#		MAIN APP RUN			#############
#############################################
def main():
	cr = cryptor()
	cr.root.mainloop()

if __name__ == '__main__':
	main()
