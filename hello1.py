import tkinter as tk
class hello1():
	def __init__(self):
		self.root = tk.Tk()
		self.w = tk.Label(self.root, text ="Hello World!")
		self.w.pack()
		self.root.mainloop()

hello1()
