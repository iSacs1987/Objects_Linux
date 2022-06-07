"""
This is the first example program for creating top level menus for your GUIs.
Here I show you how to create a simple top level menu without drop down menus.
"""
# First we import tkinter
import tkinter as tk

# Now I define two empty functions to associate them with my Menu later on
def save():
    pass


def load():
    pass


# Now I create my Window and set its geometrys
root = tk.Tk()
root.geometry("200x150")
# Now I create my Menu and define its parent (root)
mainmenu = tk.Menu(root)
# Now I can add my Buttons to my menu with the add_command method. This method
# uses the label attribute for displaying text on the buttons and the command
# attribute to associate a function with the button. You can think of these
# buttons as childs of our mainmenu here. The first two buttons are associated
# with our empty functions at the top.
mainmenu.add_command(label="Save", command=save)
mainmenu.add_command(label="Load", command=load)
# The third button is associated with the root.destroy method, a tkinter method
# which allows us to close a specific Widget (here the Window). This method is
# also available for labels, buttons and so on. But be careful when using it.
mainmenu.add_command(label="Exit", command=root.destroy)
# To use our menu in our GUI we have to use the config method of our main window
# and use the menu attribute. By handing over the name of our custom made menu
# (mainmenu) as argument for the menu attribute we can associate our menu with
# our GUI. The command in line 38 does NOT work, so we can't use menu in
# combination with a geometry manager.
# mainmenu.pack()
root.config(menu=mainmenu)
# Last but not Least we initialize our GUI.
root.mainloop()
