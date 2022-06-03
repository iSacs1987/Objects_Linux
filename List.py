"""
The program for explaining list boxes without a button. I included an event
listener here to show you how to create such a thing at least once during our
course. You can ignore it if you want and just adjust the function to work with
a button as its shown in List_Button.py
"""
# First we import tkinter
import tkinter as tk

# Now I define my function which is executed as soon as the user clicks on our
# listbox later on. Since this function is associated with an event listener
# here we have to hand over the argument event. Otherwise we would get errors.
# The rest is the same as we saw for other functions before.
def items_selected(event):
    # To read out the information from our listbox we have to use the get()
    # method, unfortunately this method needs always an index as argument to
    # give us back the correct entry in our list. To get this index we have to
    # use the curselection() method, which returns a tuple that contains the
    # corresponding indices. Per default listboxes allow only a single selection
    # and thus we can use the return of this method on our get() method here. If
    # we allow multiple selections as we will see in List_Button.py than you
    # should NOT use it like this.
    print(listbox.curselection())
    selected_index = listbox.get(listbox.curselection())
    # Now I generate a simple print statement to tell the use what he chose.
    print("You selected:", selected_index)


# Now we can create our GUI with setting upp the Tk widget first
root = tk.Tk()
# Again I specify the dimensions of our GUI
root.geometry("200x200")
# I want that the user can't change the size of my GUI thus I use the resizable
# method and set both arguments to False. The first argument is for adjusting
# the width and the second for adjusting the height.
root.resizable(False, False)
# Furthermore I want my Window to have a "unique" title instead of the generic
# tk we saw so far.
root.title("Listbox")
# Now I define a list that contains the options of my listbox.
langs = ["Java", "C#", "C", "C++", "Python", "Go", "JavaScript", "PHP", "Swift"]
# Now I can define my VarVar. I use a StringVar and hand over my list to it in
# form of the attribute value. Now the VarVar langs_var contains all elements
# from my list langs
langs_var = tk.StringVar(value=langs)
# Now I can create my ListBox Widget. As arguments I have to hand over the
# parent (root) and than I have to associate my listbox with a VarVar by using
# the attribute listvariable here. Last but not least I can tell my listbox how
# many elements it should display on the loading of my GUI. Here I chose to
# display all nine elements of my list (height=9). So you can see that the
# attribute height takes the number of elements you want to display.
listbox = tk.Listbox(root, listvariable=langs_var, height=9, background="snow")
# Now I create my EventListener with the bind method. This allows me to execute
# my function as soon as the user clicks on an item in my list. The event here
# is called "ListboxSelect" and means that the user clicked on an item in our
# list.
listbox.bind("<<ListboxSelect>>", items_selected)
# Now I put my listbox in my GUI.
listbox.pack()
# Now I intialize my GUI with the mainloop
root.mainloop()
