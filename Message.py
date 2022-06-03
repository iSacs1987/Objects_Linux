"""
The program for explaining message boxes. These are Widgets that are very
similar to labels but are a bit more flexible in their way to display text
"""
# First we import tkinter
import tkinter as tk

# Now we create our GUI
root = tk.Tk()
# We define a string variable which contains the text we want to display
whatever = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
# Now we can create our Messagebox by handing over the parent and the text we
# want to be displayed, in our case the variable whatever.
msg = tk.Message(root, text=whatever)
# Now I can adjust the format of the text in my Messagebox with config.
# Unfortunately this does NOT work in our VM but I showed you the effect outside
# of it.
msg.config(bg="lightgreen", font=("times", 24, "italic"))
# Now I put my Messagebox in my GUI
msg.pack()
# Lastly I initialize my GUI.
root.mainloop()
