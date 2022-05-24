"""
The program for explaining List Boxes with a Button.
"""

import tkinter as tk


def items_selected():
    languages = []
    selected_indices = listbox.curselection()
    for i in selected_indices:
        index = listbox.get(i)
        languages.append(index)
    for lang in languages:
        print("You selected:", lang)


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
listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=9,
    selectmode="multiple",
    selectbackground="blue",
    selectforeground="snow",
)
button1 = tk.Button(root, text="Click Me", command=items_selected)
listbox.pack(fill="both")
button1.pack()
root.mainloop()
