"""
The program for explaining List Boxes with a Button.
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
        self.listbox = tk.Listbox(
            self.root,
            listvariable=self.langs_var,
            height=9,
            selectmode="multiple",
            selectbackground="blue",
            selectforeground="snow",
        )
        self.button1 = tk.Button(
            self.root, text="Click Me", command=self.items_selected
        )
        self.listbox.pack(fill="both")
        self.button1.pack()
        self.root.mainloop()

    def items_selected(self):
        languages = []
        selected_indices = self.listbox.curselection()
        for i in selected_indices:
            index = self.listbox.get(i)
            languages.append(index)
        for lang in languages:
            print("You selected:", lang)


ListBox()
