"""
The program for explaining list boxes without a button
"""

import tkinter as tk


class ListBox:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.resizable(False, False)
        self.root.title("Listbox")
        self.langs = [
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
        self.langs_var = tk.StringVar(value=self.langs)
        self.listbox = tk.Listbox(self.root, listvariable=self.langs_var, height=9,)
        self.listbox.bind("<<ListboxSelect>>", self.items_selected)
        self.listbox.pack()
        self.root.mainloop()

    def items_selected(self, event):
        selected_index = self.listbox.get(self.listbox.curselection())
        print("You selected:", selected_index)


ListBox()
