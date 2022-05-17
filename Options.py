"""
This is the example for an option menu.
"""
import tkinter as tk


class Options:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x200")
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var1.set("Option 1")
        self.var2.set("snow")
        self.menu = tk.OptionMenu(
            self.root,
            self.var1,
            "Option 1",
            "Option 2",
            "Option 3",
            command=self.display_selected,
        )
        self.menu.pack(side="left")
        self.menu2 = tk.OptionMenu(
            self.root, self.var2, "blue", "snow", "grey", command=self.change_bg,
        )
        self.menu2.pack(side="left")
        self.label1 = tk.Label(self.root, text=self.var1.get(), bg=self.var2.get())
        self.label1.pack(side="right")
        self.root.mainloop()

    def display_selected(self, choice):
        choice = self.var1.get()
        print(choice)
        self.label1.config(text=choice)

    def change_bg(self, choice):
        self.label1.config(bg=self.var2.get())


Options()
