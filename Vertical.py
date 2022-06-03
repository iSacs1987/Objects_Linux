"""
The program for explaining vertical scales. Here I show you how you can create
such widgets and how to read out the value from them.
"""
# First we import tkinter
import tkinter as tk

# Now we define a small little function that allows us to read read out the
# value of our scale and write it inside a label. This function does NOT need
# any arguments.
def show1():
    # Since we use a simple DoubleVar() here we can use our get() method to
    # read out the value. Please keep in mind that the returned value is of type
    # float and thus to use it inside a label we have to cast it to a string.
    sel = "Vertical Scale Value = " + str(v1.get())
    # Now we can show the String we generated in our label.
    label2.config(text=sel)


# Now we create our GUI with the Tk widget and set the geometry
root = tk.Tk()
root.geometry("400x300")
# Now I define my VarVar
v1 = tk.DoubleVar()
# Now I create my Scale. I have to hand over the parent, the VarVar I want to
# associate with it (variable) and than define the range with a starting point
# (from_) (DO NOT FORGET THE UNDERSCORE) and the endpoint (to). Per default the
# step size of your scale is 1. If you hand over an endpoint like 95.3 your
# maximum value would be 95 and for 95.5 or bigger it would be 96, so tkinter
# rounds here. Last but not least I can define the orientation of my scale with
# the attribute orient, which can be vertical or horizontal. Per default these
# scales are vertical.
scale1 = tk.Scale(root, variable=v1, from_=1, to=100, orient="vertical")
# Now I create two labels and a Button to complete my GUI.
label1 = tk.Label(root, text="Vertical Scaler")
button1 = tk.Button(root, text="Display Vertical", command=show1, bg="yellow")
label2 = tk.Label(root)
# Now I can put my Widgets in my GUI. Here I add the anchor="center" attribute
# to make sure that the text of my widget is centered.
scale1.pack(anchor="center")
label1.pack()
button1.pack(anchor="center")
label2.pack()
# Last but not Least I initialize my GUI.
root.mainloop()
