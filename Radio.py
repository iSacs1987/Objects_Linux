"""
This is the example of working with radio buttons. Here I will show and explain
in detail how to create Radiobuttons and how to group them together by using
the same VarVar for multiple Widgets.
"""
# First we import tkinter
import tkinter as tk

# Now we define a small function that just reads out the Value of our VarVar and
# than prints it in the terminal.
def ShowChoice():
    print(var.get())


# Now we create our GUI with the Tk widget
root = tk.Tk()
# Now I define my VarVar. Here I use a VarVar of the type Sttring but you could
# use other types of VarVars as well. Just make sure that the values you assign
# to your Radiobuttons later on match the type of your VarVar
var = tk.StringVar()
# Now I hand over a predefined value to my VarVar so that only one button is
# checked on the start of my GUI. If you leave this out all buttons are checked
# and if you use var.set(None) all buttons are unchecked. So you have multiple
# options here how you want your Radiobuttons to behave. But to circumvent any
# kind of problems I always would set a default value here.
var.set("Python")
# Here I create a simple lable to tell the user what he can do.
label1 = tk.Label(root, text="Pick one of the following")
label1.pack()
# Now I can create my Radiobuttons. I have to hand over the parent and than I
# can hand over the different attributes. The text is again a small label for my
# Button, variable associates this Button with my VarVar, value specifies the
# value I want my Button and thus my VarVar to have if the Button is checked and
# lastly I associate my function with the button.
radio1 = tk.Radiobutton(
    root, text="Python", variable=var, value="Python", command=ShowChoice,
)
# Now I can put my Radiobutton in my GUI with pack(), this time I use the
# attribute anchor to tell pack where to put the buttons. This atrribute takes
# values like "w" for left, "e" for right, "s" for bottom and "n" for top to
# specify where you want your Radiobutton to appear.
radio1.pack(anchor="w")
# Now I can create additional Radiobuttons and group them together with my first
# one ba associating the same VarVar with them (variable=var). Of course your
# Radiobuttons should have different values associated with them (the value
# attribute). If you associate multiple Radiobuttons with the same value all of
# them will be checked as soon as you click on one of them.
radio2 = tk.Radiobutton(
    root, text="Perl", variable=var, value="Perl", command=ShowChoice,
)
# Now I can put my second Radiobutton in my GUI.
radio2.pack(anchor="w")
# Now I can include even more Radiobuttons in my group. There is no limit to the
# number of Radiobuttons your group together using the same VarVar.
radio3 = tk.Radiobutton(
    root, text="Java", variable=var, value="Java", command=ShowChoice,
)
radio3.pack(anchor="w")
radio4 = tk.Radiobutton(
    root, text="C++", variable=var, value="C++", command=ShowChoice,
)
radio4.pack(anchor="w")
# Last but not least I initialize my GUI using mainloop().
root.mainloop()
