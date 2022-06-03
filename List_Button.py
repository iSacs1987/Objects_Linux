"""
The program for explaining List Boxes with a Button. So this is the simpler way
to work with this Widget.
"""
# First we import tkinter
import tkinter as tk

# Now I define my function, this time without any arguments as we already did
# multiple times before.
def items_selected():
    # First we read out the selected items in form of their indices
    selected_indices = listbox.curselection()
    # As I mentioned in List.py curselection() returns a tuple with the indices
    # Thus we have to use a loop to be able to use the get method here. So we
    # loop over these indices
    for index in selected_indices:
        # Now we can use the loop variable, which is an integer (the current
        # index) in combination with the get() method to read out the values of
        # our list.
        item = listbox.get(index)
        # Now I print out which items the user selected
        print("You selected:", item)


# Now we can create our GUI with the Tk widget first, this is identical to our
# other example.
root = tk.Tk()
root.geometry("200x200")
root.resizable(False, False)
root.title("Listbox")
# Now I define my list and my VarVar
langs = ["Java", "C#", "C", "C++", "Python", "Go", "JavaScript", "PHP", "Swift"]
langs_var = tk.StringVar(value=langs)
# Now I create my Listbox, here I included some additional attributes. The first
# one is selectmode, which allows me to eneable multiple selections for the user
# The second one is selectbackground which defines the color of the background
# in our listbox as soon as an element was selected. The third one selectfore-
# ground defines the text color as soon as an element is selected.
listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=9,
    background="snow",
    selectmode="multiple",
    selectbackground="blue",
    selectforeground="snow",
)
# Now I add a Button to be able to execute my function without an event listener
button1 = tk.Button(root, text="Click Me", command=items_selected)
# Now I can put my Widgets in my GUI. Here I add the attribute fill to my pack
# command to make sure that the Listbox occupies the whole width (left to right)
# of my GUI and not just a part of it, as we could see in List.py
listbox.pack(fill="both")
button1.pack()
# Last but not least I initialize my GUI.
root.mainloop()
