"""
The program for explaining message boxes.
"""

import tkinter as tk


root = tk.Tk()
whatever = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(root, text=whatever)
msg.config(bg="lightgreen", font=("times", 24, "italic"))
msg.pack()
root.mainloop()
