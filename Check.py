"""
This is the first example for working with check boxes.
"""

import tkinter as tk


def Print_Check():
    Checking = checkValue.get()
    print("Currently the value of your Checkbutton is", Checking)


root = tk.Tk()
root.geometry("150x100")
checkValue = tk.BooleanVar()
checkValue.set(True)
check1 = tk.Checkbutton(root, text="Check Box", var=checkValue, command=Print_Check)
check1.pack(side="left")
root.mainloop()
