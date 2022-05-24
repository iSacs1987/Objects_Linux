"""
The program for explaining list boxes without a button
"""

import tkinter as tk


def items_selected(event):
    selected_index = listbox.get(listbox.curselection())
    print("You selected:", selected_index)


root = tk.Tk()
root.geometry("200x200")
root.resizable(False, False)
root.title("Listbox")
langs = [
    "Java",
    "C#",
    "C",
    "C++",
    "Python",
    "Go",
    "JavaScript",
    "PHP",
    "Swift",
]
langs_var = tk.StringVar(value=langs)
listbox = tk.Listbox(root, listvariable=langs_var, height=9,)
listbox.bind("<<ListboxSelect>>", items_selected)
listbox.pack()
root.mainloop()
