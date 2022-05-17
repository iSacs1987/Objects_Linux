"""
This is the example program for text fields.
"""

import tkinter as tk

class Editor:
    def __init__(self):
        self.root = tk.Tk()
        self.text1 = tk.Text(self.root)

        self.text1.pack()
        self.button1 = tk.Button(
            self.root, text="get Contents", command=self.Text_Output
        )
        self.button1.pack(side="left")
        self.button2 = tk.Button(
            self.root, text="clear Text field", command=self.Text_Clear
        )
        self.button2.pack(side="right")
        self.button3 = tk.Button(
            self.root, text="Display Text length", command=self.Text_length
        )
        self.button3.pack(side="bottom")
        self.label1 = tk.Label(self.root, text="")
        self.label1.pack(side="bottom")
        self.root.mainloop()

    def Text_Output(self):
        self.text1.insert(1.0, "This is a Test\n")
        self.Content = self.text1.get(1.0, "end")
        self.label1.config(text="Your pressed the first button")
        print(self.Content)
        print(repr(self.Content))

    def Text_Clear(self):
        self.label1.config(text="Your pressed the second button")
        self.text1.delete(1.0, "end")

    def Text_length(self):
        self.label1.config(
            text="You're text has "
            + str(len(self.text1.get(1.0, "end-1c")))
            + " characters"
        )


Editor()
