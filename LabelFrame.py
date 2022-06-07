"""
This is the example program for using LabelFrames. Here I show you how to create
such a Frame, how to use it to group together other widgets and how to change
the position of the text. For me one of the main advantages of these Widgets in
comparison to Frames is the directly present and visible border.
"""
# First we import tkinter
import tkinter as tk

# Now we can generate our GUI
root = tk.Tk()
root.geometry("300x200")
# First we set up the LabelFrame, by defining the parent (root), the displayed
# text and last but not least the position of the text. We have 12 positions
# available to us (n,s,w,e,nw,ne,en,es,se,sw,ws and we) according to the
# cardinal directions. When we hand over a two letter position the first letter
# specifies the border and the second the position on this border. So here "sw"
# tells tkinter to put the text to the bottom border and on the left side.
label_frame = tk.LabelFrame(root, text="LAB", labelanchor="sw")
# Now we can put our LabelFrame in our GUI. Here I use only pack, because its
# easier to use here.
label_frame.pack()
# Now I define an integer VarVar, so that I can create som simple radio buttons
# without any function.
var = tk.IntVar()
# Now I create my radiobuttons and pack them into my LabelFrame since I
# specified that label_frame is the parent of these Widgets
radio1 = tk.Radiobutton(label_frame, text="Option1", variable=var, value=1)
radio1.pack()
radio2 = tk.Radiobutton(label_frame, text="Option2", variable=var, value=2)
radio2.pack()
radio3 = tk.Radiobutton(label_frame, text="Option3", variable=var, value=3)
radio3.pack()
# Last but not least we initialize our GUI.
root.mainloop()
