

import tkinter as tk
class hello2():
	def __init__(self):
		self.root = tk.Tk()
		self.button1 = tk.Button (self.root, text ="Hello World!")
		self.button1.pack()
		self.button1 = tk.Button (self.root, text ="Hello 2")
		self.button1.pack()
		self.root.mainloop()

hello2()
