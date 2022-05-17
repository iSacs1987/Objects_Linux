"""
This is the example for using entry field.
"""

import tkinter as tk

class Adder:
    def __init__(self):
        self.root = tk.Tk()
        self.input1 = tk.StringVar()
        self.input2 = tk.StringVar()
        self.edit1 = tk.Entry(self.root,textvariable=self.input1,font=15,width=33,bg="light slate gray",fg="snow",)
        self.edit2 = tk.Entry(
            self.root,
            textvariable=self.input2,
            font=15,
            width=33,
            bg="light slate gray",
            fg="snow",
        )
        self.edit1.pack()
        self.edit2.pack()
        self.button1 = tk.Button(
            self.root,
            text="Click Me",
            command=self.add_up,
            width=30,
            font=15,
            fg="yellow",
            bg="black",
            activebackground="grey",
            activeforeground="snow",
        )
        self.button1.pack()
        self.w = tk.Label(
            self.root,
            text="",
            font=15,
            width=33,
            fg="blue",
            bg="grey",
        )
        self.w.pack()
        self.root.mainloop()

    def add_up(self):
        Nr1 = self.input1.get()
        Nr2 = self.input2.get()
        ergebnis = float(Nr1) + float(Nr2)
        self.w.config(text=str(ergebnis))


Adder()
