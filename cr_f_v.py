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
from cr_f_ii import main # This module fetches the encryption function for encrypitng data stored within a file
from cr_f_iii import main_d
from pwdpop import mypop
from tkinter.ttk import Progressbar
from time import sleep
import threading

# the main class for the window


class Notes(tk.Frame): 

	__master = Tk() # The main() run inside the TKinter box

	# default window width and height
	
	__ntWidth = 300
	__ntHeight = 300
	__ntScrolledTx = tkscrolled.ScrolledText(__master, undo=True, padx=2, pady=2, wrap='word') 
	__ntMenuBar = Menu(__master) 
	__ntFileMenu = Menu(__ntMenuBar, tearoff=0) 
	__ntEditMenu = Menu(__ntMenuBar, tearoff=0) 
	__ntAbout = Menu(__ntMenuBar, tearoff=0)
	__ntStatus = Label(__master, text="Cryptor", bd=1, fg="Blue", bg="Yellow", relief=SUNKEN)
	__ntButn = Button(__ntStatus, text="Encry", bd=2, fg="Yellow", bg="Blue")
	__ntButnN = Button(__ntStatus, text="Decry", bd=2, fg="Yellow", bg="Blue")	 
	
	__file = None

	def __init__(self, **kwargs):

		tk.Frame.__init__(self, self.__master, **kwargs)  

		# The icon 
		try: 
			self.__master.wm_iconbitmap("hilma_1.ico") 
		except: 
			pass

		# The window size (the default is 300x300) 

		try: 
			self.__ntWidth = kwargs['width'] 
		except KeyError: 
			pass

		try: 
			self.__ntHeight = kwargs['height'] 
		except KeyError: 
			pass

		# The window text 
		self.__master.title("Untitled - Notes")

		# Center the window 
		screenWidth = self.__master.winfo_screenwidth() 
		screenHeight = self.__master.winfo_screenheight() 
	
		# Left-align 
		left = (screenWidth / 2) - (self.__ntWidth / 2) 
		
		# Right-align 
		top = (screenHeight / 2) - (self.__ntHeight /2) 
		
		# For top and bottom 
		self.__master.geometry('%dx%d+%d+%d' % (self.__ntWidth, 
									self.__ntHeight, 
									left, top)) 

		# ScrolledTx auto resizable 
		self.__master.grid_rowconfigure(0, weight=1) 
		self.__master.grid_columnconfigure(0, weight=1)

		#self.pwdpop = mypop(self.__ntButnN)	

		# Pop up menu Tree

		self.__tree = ttk.Treeview(self.__ntScrolledTx, height=35)
		
        ##########################################
        #  		Right click menu				 #
        ##########################################
		self.__c_rightClick = tk.Menu(self.__master, tearoff=0, relief="sunken")
		self.__c_rightClick.add_command(label='Undo', command=self.__undo)
		self.__c_rightClick.add_separator()
		self.__c_rightClick.add_command(label="Cut", command=self.__cut)
		self.__c_rightClick.add_separator()
		self.__c_rightClick.add_command(label="Copy", command=self.__copy)
		self.__c_rightClick.add_separator()
		self.__c_rightClick.add_command(label="Paste", command=self.__paste)
		self.__c_rightClick.add_separator()
		self.__c_rightClick.add_command(label='Change Font', command=None)
		self.__c_rightClick.add_separator()
		self.__c_rightClick.add_command(label='Find', command=None)
		self.__c_rightClick.add_separator()
		self.__c_rightClick.add_command(label='Run', command=self.__run)
		
        #########################################
        #		Text formating and arranging	#
        #########################################

		self.__ntScrolledTx.bind('<Button-3>', self.__popup)
		self.__ntButnN.bind('<Button-1>', self.__decry)
		#self.__c_rightClick.bind('<Button-1>', self.__decry)

		# Add controls (widget) 
		self.__ntScrolledTx.grid(sticky = N + E + S + W)
		self.__ntStatus.grid(sticky=E + W)
		self.__ntButn.grid(row=0, column=1, ipadx=4, ipady=1, sticky=E)
		self.__ntButnN.grid(row=0, column=2, ipadx=4, ipady=1, sticky=W) 
		
		#########################################
		# 	MENU FILE AND ITEMS					#
		# #######################################
 
		self.__ntFileMenu.add_command(label="New", 
							command=self.__newFile, accelerator="Ctrl+N")	 
		
		# To open a already existing file 
		self.__ntFileMenu.add_command(label="Open", 
							command=self.__openFile, accelerator="Ctrl+O") 
		self.__ntFileMenu.add_separator()
		# To save current file 
		self.__ntFileMenu.add_command(label="Save", 
								command=self.__saveFile, accelerator="Ctrl+S")	 

		self.__ntFileMenu.add_command(label="Save As", 
								command=self.__saveFileAs, accelerator="Ctrl+Shift+S")
		# To create a line in the dialog		 
		self.__ntFileMenu.add_separator()										 
		self.__ntFileMenu.add_command(label="Exit", 
								command=self.__quitApplication, accelerator="Ctrl+Q") 
		self.__ntMenuBar.add_cascade(label="File", 
							menu=self.__ntFileMenu)	 
		
		self.__ntEditMenu.add_command(label="Undo", command=self.__undo, accelerator="Ctrl+Z")

		self.__ntEditMenu.add_command(label='Redo', command=self.__redo, accelerator='Ctrl+Y')

		# To give a feature of cut 
		self.__ntEditMenu.add_command(label="Cut", 
							command=self.__cut, accelerator="Ctrl+X")			 
	
		# to give a feature of copy	 
		self.__ntEditMenu.add_command(label="Copy", 
							command=self.__copy, accelerator="Ctrl+C")		 
		
		# To give a feature of paste 
		self.__ntEditMenu.add_command(label="Paste", 
							command=self.__paste, accelerator="Ctrl+V")		 
		
		# To give a feature of editing 
		self.__ntMenuBar.add_cascade(label="Edit", 
							menu=self.__ntEditMenu)	 
		
		# To create a feature of description of the notepad 
		self.__ntAbout.add_command(label="Help", 
							command=self.__showAbout) 

		self.__ntAbout.add_command(label="Welcome", 
							command=self.__showWelcome) 

		# To create a feature of description of the notepad 
		self.__ntAbout.add_command(label="Licences", 
								command=self.__showLicence) 
		self.__ntMenuBar.add_cascade(label="About", 
							menu=self.__ntAbout)

		self.__master.config(menu=self.__ntMenuBar)

		#################################################################
		# 		SCROLL BAR AND TEXT AREA PUT TOGETHER					#
		# ###############################################################		 
		self.__ntScrolledTx.focus()

		self.__ntButn.config(command=self.__encry)

    #####################################################
    #		THE FUNCTIONS OF DEFINED ITEMS ABOVE		#
    #####################################################

	def __popup(self, event):
		self.__c_rightClick.post(event.x_root, event.y_root)
	
	def __run(self):
		self.__decry()
		#self.pwdpop()

	def __quitApplication(self):
		if messagebox.askyesno("Close Window!", "Do you really want to quit! \nAny unsaved material will be lost"):
			self.__master.destroy()

	def __showAbout(self): 
		messagebox.showinfo("Notes","Completely illegal to open documents without prior authority")

	def __openFile(self): 
		
		self.__file = askopenfilename(defaultextension=".txt", 
									filetypes=[("All Files","*.*"), 
										("Text Documents","*.txt")]) 

		if self.__file == "":
			
			# no file to open 
			self.__file = None
		else:

			
			# Try to open the file 
			# set the window title 
			self.__master.title(os.path.basename(self.__file) + " - Notes") 
			self.__ntScrolledTx.delete(1.0,END) 

			file = open(self.__file,"r") 
			#file.readFromFileAndDecrypt()
			self.__ntScrolledTx.insert(1.0, file.read())

			file.close() 

		
	def __newFile(self): 
		self.__master.title("Untitled - Notes") 
		self.__file = None
		self.__ntScrolledTx.delete(1.0,END) 

	def __saveFile(self): 

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
				file.write(self.__ntScrolledTx.get(1.0,END)) 
				file.close() 
				
				# Change the window title 
				self.__master.title(os.path.basename(self.__file) + " - Notes") 
				
		else: 
			file = open(self.__file,"w") 
			file.write(self.__ntScrolledTx.get(1.0,END)) 
			file.close() 
        
	def __saveFileAs(self):
		self.__file = asksaveasfilename(initialfile='Untitled.txt', 
								defaultextension=".txt", 
								filetypes=[("All Files","*.*"), 
									("Text Documents","*.txt")])
                
		# Try to save the file 
		file = open(self.__file,"w") 			
		file.write(self.__ntScrolledTx.get(1.0,END))
		file.close() 
				
		# Change the window title 
		self.__master.title(os.path.basename(self.__file) + " - Notes") 

	def __undo(self):
		self.__ntScrolledTx.event_generate("<<Undo>>")

	def __redo(self):
		self.__ntScrolledTx.event_generate("<<Reod>>")

	def __cut(self): 
		self.__ntScrolledTx.event_generate("<<Cut>>") 

	def __copy(self): 
		self.__ntScrolledTx.event_generate("<<Copy>>") 

	def __paste(self): 
		self.__ntScrolledTx.event_generate("<<Paste>>") 

	def __decry(self):
		#self.pwdpop.post(event.x_root, event.y_root)
		txt = self.__ntScrolledTx.get(1.0, END)
		
		self.pwdpop = mypop(self.__ntScrolledTx)
		#self.pwdpop()
		#self.mypop.post(event.x_root, event.y_root)
		if self.__ntScrolledTx.wait_window(self.pwdpop.top):
			pass

		#else:
		#	Exception
		"""
		txt = range(100)

		pop = tk.Toplevel()
		tk.Label(pop, text='Please Wait a bit....').grid(row=0, column=0)
		progress = 0
		progress_var = tk.DoubleVar()
		progress_bar = ttk.Progressbar(pop, variable=progress_var, maximum=100)
		progress_bar.grid(row=1, column=0)#.pack(fill=tk.X, expand=1, side=tk.BOTTOM)
		pop.pack_slaves()

		progress_step = float(100.0/len(txt))
		for team in txt:
			pop.update()
			sleep(0.05)
			progress += progress_step
			progress_var.set(progress)
			if progress == 100:
				pop.destroy() """

		#if self.__ntScrolledTx.wait_window(self.pwdpop.top):
		#	pass

		if txt == "":
			main_d()
			file = 'cr_k_i.txt'
			fo = open(file)
			xt = fo.read()
			fo.read()
			self.__ntScrolledTx.delete(1.0, END)
			xt = range(100)

			pop = tk.Toplevel()
			tk.Label(pop, text='Please Wait a bit....').grid(row=0, column=0)
			progress = 0
			progress_var = tk.DoubleVar()
			progress_bar = ttk.Progressbar(pop, variable=progress_var, maximum=100)
			progress_bar.grid(row=1, column=0)#.pack(fill=tk.X, expand=1, side=tk.BOTTOM)
			pop.pack_slaves()

			progress_step = float(100.0/len(xt))
			for team in xt:
				pop.update()
				sleep(5)
				progress += progress_step
				progress_var.set(progress)
				if progress == 100:
					pop.destroy()
					
			self.__ntScrolledTx.insert(1.0, xt)
			fo.close()
		
		else:
			self.__ntScrolledTx.get(1.0, END)
			main_d()

			file = 'cr_k_i.txt'
			fo = open(file)
			xt = fo.read()
			fo.read()
			self.__ntScrolledTx.delete(1.0, END)
			self.__ntScrolledTx.insert(1.0, xt)
			fo.close()

	def __encry(self):
		tx = self.__ntScrolledTx.get(1.0, END)
		if tx == "":
			main()

		else:
			self.__ntScrolledTx.get(1.0, END)
			main()

		file = 'cr_k_i.txt'
		fil = open(file)
		ft = fil.read()
		fil.read()
		self.__ntScrolledTx.delete(1.0, END)
		self.__ntScrolledTx.insert(1.0, ft)
		fil.close()

	def run(self): 

		# Run main application 
		self.__master.mainloop() 

	def __showWelcome(self): 
		#if self.__file == None: 
		file = 'welcome.txt'
		fo = open(file)
		#fo.read()
		ts=fo.read()
		fo.read()
		self.__ntScrolledTx.delete(1.0, END)
		self.__ntScrolledTx.insert(1.0, ts)
		fo.close()	

	def __showLicence(self):
		messagebox.showinfo('Notes', "Mapenzi Mudimba, 2018.\n\nAllright reserved. No part may be exportedinto any media\nwithout consent from the author.")
	def __showAbout(self):
		messagebox.showinfo("Notes", "1. Press the encrypt button once.\n2. Press the Decrypt button once\n3. Enter a four digit PIN provided by your Administator.\n4. Make sure you encrypt the programme before closing the app, otherwise your files will be in plain text.")

# Run main application
  
if __name__ == "__main__":
	mainloop
	#app = ProgressBar()
	#app.pack()

notes = Notes(width=600,height=400) 
notes.run()