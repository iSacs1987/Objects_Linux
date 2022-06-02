"""
This is the second exampl for radio buttons. The only difference here is that
I use the indicator attribute to create a so called button box. I won't explain
this program in detail, since it's functional identical to Radio.py
"""
import tkinter as tk


def ShowChoice():
    print(var.get())


root = tk.Tk()
var = tk.StringVar()
var.set("Python")
label1 = tk.Label(root, text="Pick one of the following")
label1.pack()
radio1 = tk.Radiobutton(
    root,
    text="Python",
    variable=var,
    value="Python",
    command=ShowChoice,
    indicator=0,
    width=20,
)
radio1.pack(anchor="w")
radio2 = tk.Radiobutton(
    root,
    text="Perl",
    variable=var,
    value="Perl",
    command=ShowChoice,
    indicator=0,
    width=20,
)
radio2.pack(anchor="w")
radio3 = tk.Radiobutton(
    root,
    text="Java",
    variable=var,
    value="Java",
    command=ShowChoice,
    indicator=0,
    width=20,
)
radio3.pack(anchor="w")
radio4 = tk.Radiobutton(
    root,
    text="C++",
    variable=var,
    value="C++",
    command=ShowChoice,
    indicator=0,
    width=20,
)
radio4.pack(anchor="w")
root.mainloop()
