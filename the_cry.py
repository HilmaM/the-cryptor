#!/usr/bin/python3

# Mapenzi Mudimba
# Copyright 2018
#############################################
#   Basic programme for my personal journal #
#############################################
#===========================================

# importing modules
import os, sys, math
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import *
import tkinter.scrolledtext as tkscrolled
from tkinter import Scrollbar
from cr_f_ii import main # This module fetches the encryption function for encrypitng data stored within a file
from cr_f_iii import main_d
from pwdpop import mypop
from tkinter.ttk import Progressbar
from time import sleep
import threading
from PIL import ImageTk, Image
from datetime import date
from idlelib.colorizer import ColorDelegator, color_config

class cryptor(object):
	def __init__(self, **kwargs):
		#win_width = 600
		#win_height = 420
		self.root = root

		self.menufont = ("Arial", 12, NORMAL)
		self.MINIMUM_FONT_SIZE = 6
		self.MAXIMUM_FONT_SIZE = 100
		self.font_sizes = [8, 9, 10, 11, 12, 14, 18, 20, 22, 24, 30]
		self.txtfont = ['Lucida Console', 10, 'normal']

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
		# Create a line in the dialog		 
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
		# Feature of Run 
		self.editMenu.add_command(label="Run", 
							command=self.run, accelerator="F5")	
		# Feature of editing 
		self.menuBar.add_cascade(label="Edit", 
							menu=self.editMenu)	 
		
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
						
		self.fnMenu = Menu(self.root, tearoff=0)
		#self.fnMenu.add_command(command=self.fontMenu)

		self.menuBar.add_cascade(menu=self.fontMenu(self.menuBar), label='Fonts')

		self.root.config(menu=self.menuBar)

		###############
		# The Pane
		###############

		# The Date funct
		self.day = date.today()
		self.day.strftime('%d-%m-%Y')
		self.day1 = date.today()
		self.day1.strftime('%Y %m %d')

		#						#				#						#
		# Buttons and Labels	################# The text framework #
		#						#				#						#

		self.text_frame = text_frame = Frame(root,relief=RIDGE)
		self.scrolledTx = text = Text(text_frame, name='text', padx=5, pady=4,
                                wrap='word', relief=RIDGE)
		color_config(text)

		self.vbar = vbar = Scrollbar(text_frame, name='vbar')
		vbar['command'] = text.yview
		vbar.pack(side=RIGHT, fill=Y)
		text['yscrollcommand'] = vbar.set

		text_frame.pack(fill=BOTH, expand=1)

		text['font'] = tuple(self.txtfont)
		shortcut = 'Control'
		text.bind_all('<%s-minus>' % shortcut, self.decrease_size)
		text.bind_all('<%s-underscore>' % shortcut, self.decrease_size)
		text.bind_all('<%s-equal>' % shortcut, self.increase_size)
		text.bind_all('<%s-plus>' % shortcut, self.increase_size)
		text.bind('<Control-MouseWheel>', self.update_mousewheel)
		text.bind('<Control-Button-4>', self.increase_size)
		text.bind('<Control-Button-5>', self.decrease_size)

		text.pack(fill=BOTH, expand=1)


		self.statusBar = Label(root, bd=1, relief=SUNKEN) 
		self.statusBar.pack(side=BOTTOM, fill='x')
		self.btn = Button(self.statusBar, text='Encrypt', bg='green', fg='blue', padx=10, pady=2, relief=RAISED, command=self.encry)
		self.btn.pack(side=LEFT)
		self.butn = Button(self.statusBar, text='Decrypt', bg='yellow', fg='brown', padx=10, pady=2, relief=RAISED, command=self.decry)
		self.butn.pack(side='left')
		self.ti_bt = Label(self.statusBar, text=self.day1, bg='#ddd', padx=4, pady=4, relief=RIDGE)
		self.ti_bt.pack(side=RIGHT)

		# The Function for POP_UP Menu	
		self.scrolledTx.bind('<Button-3>', self.pop_up)

		#################################################
		#	THE AREA FOR DEFINING ALL THE FUCNTIONS		#
		#################################################

	def pop_up(self, event):
		self.editMenu.post(event.x_root, event.y_root)

	def run(self):
		self.decry()

	def quitApplication(self):
		if messagebox.askyesno("Close Window!", "Do you really want to quit! \nAny unsaved material will be lost"):
			self.root.destroy()

	def showAbout(self): 
		messagebox.showinfo("Cryptor","Completely illegal to open documents without prior authority")

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
				
				# Change the window title 
				self.root.title(os.path.basename(self.__file) + " - Cryptor") 
				
		else: 
			file = open(self.__file,"w") 
			file.write(self.scrolledTx.get(1.0,END)) 
			file.close() 
        
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
		t_xt = self.scrolledTx.get(1.0, END)
		
		self.pwdpop = mypop(self.scrolledTx)
		if self.scrolledTx.wait_window(self.pwdpop.top):
			pass

		if t_xt == "":
			main_d()
			xt = self.fi_let()
			self.scrolledTx.insert(1.0, xt)
		
		else:
			self.scrolledTx.get(1.0, END)
			main_d()
			xt = self.fi_let()
			self.scrolledTx.insert(1.0, xt)

	def sav_fi(self):
		flt = open(r'C:\\Users\\hazel\Desktop\\the_cry\\fil_et.txt', "w") 
		flt.write(self.scrolledTx.get(1.0, END)) 
		flt.close()

	def del_fi(self):
		#defi = self.fi_let()
		delfi = open(r'C:\\Users\\hazel\Desktop\\the_cry\\cr_k_i.txt', 'w')
		delfi.write("")
		delfi.close()

	def op_fi(self):
		with open(r'C:\\Users\\hazel\Desktop\\the_cry\\cr_k_i.txt') as f:
			read_data = f.read()
			return read_data
		
	def fi_let(self):
		with open(r'C:\\Users\\hazel\Desktop\\the_cry\\fil_et.txt') as fi:
			re_data = fi.read()
			return re_data

	def encry(self):
		self.scrolledTx.config(state='normal')
		self.sav_fi()
		main()
		self.del_fi()
		fie = self.op_fi()
		self.scrolledTx.delete(1.0, END)
		self.scrolledTx.insert(1.0, fie)
		self.scrolledTx.config(state='disable')

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
		messagebox.showinfo('Cryptor', "Mapenzi Mudimba, 2018.\n\nAllright reserved. No part may be exported into any media\nwithout consent from the author.")
	
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
		# For wheel up, event.delta = 120 on Windows, -1 on darwin.
		# X-11 sends Control-Button-4 event instead.
		if event.delta < 0:
			return self.decrease_size()
		else:
			return self.increase_size()

root = tk.Tk()
cr = cryptor()
root.mainloop()
