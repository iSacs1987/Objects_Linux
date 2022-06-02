"""
This is the second example for working with check boxes. Here I included a
button to execute my function instead of associating it with my Checkbutton.
"""
# We import tkinter
import tkinter as tk

# Now we define our function
def Print_Check():
    # First I read out the value of my VarVar with the get method again
    Checking = checkValue.get()
    # Now I create an if statement to show you how you can use Boolean variables
    # in combination with if. When the Checkbutton is activated (has a check),
    # the value of checkValue is True and thus Checking also has a value of True
    # Therefore the predicate in line 15 states if True
    if Checking:
        # Thisprint out is given when the button is checked
        print("You're Check Box is activated")
    else:
        # This print out is given when the button is NOT checked
        print("You're Check Box is not activated")


# Now I create my GUI in a nearly identical manner to Check.py
# First creat Tk widget
root = tk.Tk()
# Set geometry of Tk widget
root.geometry("300x100")
# Define VarVar
checkValue = tk.BooleanVar()
# Set value of VarVar to True
checkValue.set(True)
# This time I only associate my VarVar with the Checkbutton and no function
check1 = tk.Checkbutton(root, text="Check Box", var=checkValue)
# Put the Checkbutton into the GUI
check1.pack(side="left")
# Here is the main difference, since I include a button on this GUI to execute
# my function.
button1 = tk.Button(
    root, text="Check your input", width=80, fg="blue", bg="grey", command=Print_Check
)
# Put the Button into the GUI
button1.pack(side="right")
# Initialize the GUI
root.mainloop()
