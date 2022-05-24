"""
This is the second example for working with check boxes.
"""

import tkinter as tk


def Print_Check():
    Checking = checkValue.get()
    if Checking:
        print("You're Check Box is activated")
    else:
        print("You're Check Box is not activated")


root = tk.Tk()
root.geometry("300x100")
checkValue = tk.BooleanVar()
checkValue.set(True)
check1 = tk.Checkbutton(root, text="Check Box", var=checkValue)
check1.pack(side="left")
button1 = tk.Button(
    root, text="Check your input", width=80, fg="blue", bg="grey", command=Print_Check,
)
button1.pack(side="right")
root.mainloop()
