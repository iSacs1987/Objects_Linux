"""
This is our first example script for working with tkinter. Here we create a GUI
with one label, to show you the general principles of creating such GUIs.
"""
# First we have to import our module tkinter with the help of an alias
import tkinter as tk

# Now we can start by creating our GUI. The first thing we have to do, is
# creating our window, the so called Tk widget. This widget carries all other
# widgets and functions as parent to all our other widgets.
root = tk.Tk()
# Now we can create our first Widget. Here we create a simple Label, a Widget
# that is used to display text on our GUI. This is the most basic Widget of
# them all. Whenever we create a new Widget we have to hand over the parent
# of it as first argument (root). Than we can add attributes to our Widget.
# Here I chose the attributes text (the text that is displayed on our label)
# height (the height of our widget in text units) and width (the width of our
# widget also in text units)
label1 = tk.Label(root, text="Hello World!", height=5, width=30)
# After I created my label I have to use some kind of geometry manager to place
# it inside of my GUI. For our first examples we will simply use pack() as the
# most basic form. We will talk about other methods later. PLEASE always use
# some kind of geometry manager, otherwise you will NOT see your Widget on your
# GUI.
label1.pack()
# The last thing we have to do is initializing our GUI by invoking the
# mainloop() method of our root. If you forget this line of code, your GUI will
# NOT start. So make sure to always include it in your programs.
root.mainloop()
