"""
The program for explaining message boxes.
"""

import tkinter as tk


class Message:
    def __init__(self):
        self.root = tk.Tk()
        self.whatever = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
        self.msg = tk.Message(self.root, text=self.whatever)
        self.msg.config(bg="lightgreen", font=("times", 24, "italic"))
        self.msg.pack()
        self.root.mainloop()


Message()
