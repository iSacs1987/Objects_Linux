import tkinter as tk

class Entries():
    def __init__(self):
    	self.root = tk.Tk()
    	self.input1 = tk.StringVar()
    	self.input2 = tk.StringVar()
    	self.edit1 = tk.Entry(self.root, textvariable = self.input1)
    	self.edit2 = tk.Entry(self.root, textvariable = self.input2)
    	self.edit1.pack()
    	self.edit2.pack()
    	self.root.mainloop()

    def add_up(self):
    	zahl1 = self.input1.get()
    	zahl2 = self.input2.get()
    	ergebnis = float(zahl1) + float(zahl2)
    	print(ergebnis)

Entries()
