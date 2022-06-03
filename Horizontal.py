"""
The program for explaining horizontal scales. This program is nearly identical
to Vertical.py and thus I will only add a comment about the Scale here.
"""

import tkinter as tk


def show1():
    sel = "Horizontal Scale Value = " + str(v1.get())
    label2.config(text=sel,)


root = tk.Tk()
root.geometry("400x300")
v1 = tk.DoubleVar()
# This scale has a smaller range than the previous one (1 to 10). Furthermore I
# change the orientation to horizontal and add the attribtue resolution that
# defines the step-size for my scale. So here I have a stepsize of 0.2 that
# means I can choose values like 1.0, 1.2, 1.4 ... 9.8, 10.0.
# Some additional attributes you may find useful are width (default 100 pixel)
# and height (default 15 pixel) to adjust the size of your scale. Additionally
# there is an attribute called sliderlength (default 30 pixel) which allows you
# to adjust the size of your slider.
scale1 = tk.Scale(
    root, variable=v1, from_=1, to=10, orient="horizontal", resolution=0.2,
)
label1 = tk.Label(root, text="Horizontal Scaler")
button1 = tk.Button(root, text="Display Horizontal", command=show1, bg="yellow")
label2 = tk.Label(root)
scale1.pack(anchor="center")
label1.pack()
button1.pack(anchor="center")
label2.pack()
root.mainloop()
