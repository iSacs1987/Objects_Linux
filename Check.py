"""
This is the first example for working with check boxes. Here I show you how to
create this buttons, associate VarVars and functions with them.
"""
# First we import tkinter
import tkinter as tk

# Now we define our function which we want to associate with our Checkbutton.
# This is a simple function that prints out the status of our Checkbutton in the
# Terminal. Please remember that these functions are only read by the
# interpreter after they were called back later on in the main program, or to be
# even clearer here after the user pressed the button.
def Print_Check():
    # I use the get method to read out the value of my VarVar checkValue. Since
    # this is a global variable which I defined in my main program I can simply
    # use it here.
    Checking = checkValue.get()
    # Now I can create my print command to tell the user whether his Checkbutton
    # is activated or not.
    print("Currently the value of your Checkbutton is", Checking)


# Now we can create our GUI by setting up our Tk widget and specify its geometry
root = tk.Tk()
root.geometry("150x100")
# Now we define our VarVar checkValue, which has to be of type Boolean to be
# able to associate it with the Checkbutton. We need one variable for each
# Checkbutton
checkValue = tk.BooleanVar()
# I set the value of my VarVar to True so that my Checkbutton is already checked
# when the GUI is loaded.
checkValue.set(True)
# Now I can create my Checkbutton. I add a small label with the text attribute,
# which is a neat thing since this text is also part of our button so we can
# even click on the text to interact with our Checkbutton. Than I associate my
# VarVar with the button with the help of the var attribute and lastly I
# associate a function with my Checkbutton, this is possible since as the name
# implies tkinter sees this as another form of button.
check1 = tk.Checkbutton(root, text="Check Box", var=checkValue, command=Print_Check)
# Now I put my Checkbutton in my GUI with pack
check1.pack(side="left")
# Last but not Least I initialize my GUI with the mainloop()
root.mainloop()
