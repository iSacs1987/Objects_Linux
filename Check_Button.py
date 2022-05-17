"""
This is the second example for working with check boxes.
"""

import tkinter as tk


class Check:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x100")
        self.checkValue = tk.BooleanVar()
        self.checkValue.set(True)
        self.check1 = tk.Checkbutton(self.root, text="Check Box", var=self.checkValue)
        self.check1.pack(side="left")
        self.button1 = tk.Button(
            self.root,
            text="Check your input",
            width=80,
            fg="blue",
            bg="grey",
            command=self.Print_Check,
        )
        self.button1.pack(side="right")
        self.root.mainloop()

    def Print_Check(self):
        Checking = self.checkValue.get()
        if Checking:
            print("You're Check Box is activated")
        else:
            print("You're Check Box is not activated")


Check()
