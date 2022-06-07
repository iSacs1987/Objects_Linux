"""
This is the second exampl of working with top level menus. This time we create
submenus for our buttons at the top of our window, so we create a nested top
level menu. I only use two planes (the buttons at the top and a drop down menu)
here but you could nest together even more menus if you want.
"""
# First we import tkinter
import tkinter as tk

# Now I define an empty function again to be able to use the command attribute
# later on
def emptyfunc():
    pass


# Now we create our Window
root = tk.Tk()
# Now we create our top level menu (The buttons at the top of our window)
mainmenu = tk.Menu(root)
# Now we can create our first sub menu called filemenu, by defining the mainmenu
# as parent we can nest them together later on. The attribute tearoff=0 makes
# sure that the submenu can NOT be separated from the mainmenu. Normally you
# would be able to separate them from each other.
filemenu = tk.Menu(mainmenu, tearoff=0)
# Now we can add buttons to our submenu in a similiar manner as we did when we
# just had our top level menu in Menu1.py by using the add_command method here.
filemenu.add_command(label="Open", command=emptyfunc)
filemenu.add_command(label="Save", command=emptyfunc)
# We can add small lines to separate groups of buttons in our submenu with the
# help of the add_separator() method here. This allows us to create a menu that
# offers a better visual appeal
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
# To add our submenu to our mainmenu we have to use the add_cascade method that
# allows us to nest our menus together. This method again has an attribute label
# that represents the text that is written on the button in our top level menu
# and than the attribute menu takes a Menu Widget as argument to nest it into
# our top level menu.
mainmenu.add_cascade(label="File", menu=filemenu)
# Here we create and nest the second submenu called toolmenu. The approach is
# the same as for the first submenu
toolmenu = tk.Menu(mainmenu, tearoff=0)
toolmenu.add_command(label="Find", command=emptyfunc)
toolmenu.add_command(label="Debugger", command=emptyfunc)
toolmenu.add_command(label="Replace", command=emptyfunc)
mainmenu.add_cascade(label="Tools", menu=toolmenu)
# I add a third submenu called helpmen in the same way I did for the first two.
helpmenu = tk.Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Documentation", command=emptyfunc)
mainmenu.add_cascade(label="Help", menu=helpmenu)
# Now we associated our mainmenu with our window
root.config(menu=mainmenu)
# last but not Least we initialize our GUI.
root.mainloop()
