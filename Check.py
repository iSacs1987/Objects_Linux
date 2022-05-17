"""
This is the first example for working with check boxes.
"""

import tkinter as tk


class Check:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("150x100")
        self.checkValue = tk.BooleanVar()
        self.checkValue.set(True)
        self.check1 = tk.Checkbutton(
            self.root, text="Check Box", var=self.checkValue, command=self.Print_Check
        )
        self.check1.pack(side="left")
        self.root.mainloop()

    def Print_Check(self):
        Checking = self.checkValue.get()
        print("Currently the value of your Checkbutton is", Checking)


Check()
