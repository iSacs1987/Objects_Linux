"""
This is the second exampl for radio buttons.
"""
import tkinter as tk

class Radio:
    def __init__(self):
        self.root = tk.Tk()
        self.var = tk.StringVar()
        self.var.set("Python")
        self.label1 = tk.Label(self.root, text="Pick one of the following")
        self.label1.pack()
        self.radio1 = tk.Radiobutton(
            self.root,
            text="Python",
            variable=self.var,
            value="Python",
            command=self.ShowChoice,
            indicator=0,
            width=20,
        )
        self.radio1.pack(anchor="w")
        self.radio2 = tk.Radiobutton(
            self.root,
            text="Perl",
            variable=self.var,
            value="Perl",
            command=self.ShowChoice,
            indicator=0,
            width=20,
        )
        self.radio2.pack(anchor="w")
        self.radio3 = tk.Radiobutton(
            self.root,
            text="Java",
            variable=self.var,
            value="Java",
            command=self.ShowChoice,
            indicator=0,
            width=20,
        )
        self.radio3.pack(anchor="w")
        self.radio4 = tk.Radiobutton(
            self.root,
            text="C++",
            variable=self.var,
            value="C++",
            command=self.ShowChoice,
            indicator=0,
            width=20,
        )
        self.radio4.pack(anchor="w")
        self.root.mainloop()

    def ShowChoice(self):
        print(self.var.get())


Radio()
