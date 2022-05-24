"""
This is the example for using entry field.
"""

import tkinter as tk


def add_up():
    Nr1 = input1.get()
    Nr2 = input2.get()
    ergebnis = float(Nr1) + float(Nr2)
    w.config(text=str(ergebnis))


root = tk.Tk()
input1 = tk.StringVar()
input2 = tk.StringVar()
edit1 = tk.Entry(
    root, textvariable=input1, font=15, width=33, bg="light slate gray", fg="snow",
)
edit2 = tk.Entry(
    root, textvariable=input2, font=15, width=33, bg="light slate gray", fg="snow",
)
edit1.pack()
edit2.pack()
button1 = tk.Button(
    root,
    text="Click Me",
    command=add_up,
    width=30,
    font=15,
    fg="yellow",
    bg="black",
    activebackground="grey",
    activeforeground="snow",
)
button1.pack()
w = tk.Label(root, text="", font=15, width=33, fg="blue", bg="grey",)
w.pack()
root.mainloop()
