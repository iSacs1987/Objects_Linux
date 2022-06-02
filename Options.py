"""
This is the example for an option menu. A small little hint, this could be
important for your LEK.
"""
# First we import tkinter
import tkinter as tk

# Now we define two functions, one for each OptionMenu. The first one changes
# the text displayed in the label and prints out the chosen option to the
# terminal. When we associate functions with an OptionMenu, we always have to
# hand over the argument choice, otherwise we get the following error message:
# TypeError: display_selected() takes 0 positional arguments but 1 was given
def display_selected(choice):
    # Now I read out the value of my first VarVar that is associated with the
    # same menu as this funtion. Since this is a StringVar I can use the value
    # simply in print commands and similiar things.
    choice = var1.get()
    # Now I print out the value in my terminal
    print(choice)
    # Now I change the text of my label to let it display the chosen option
    label1.config(text=choice)


# This second function is associated with my second menu and allows me to change
# the background color of my label. Again I have to hand over the argument
# choice here
def change_bg(choice):
    # Now I can use config to change the background color of my label (bg) to
    # the value I get from my StringVar. Please keep in mind that this attribute
    # takes strings in form of color words (blue, yellow, green etc.) as values
    label1.config(bg=var2.get())


# Now we can create our GUI by first creating our Window
root = tk.Tk()
# Here I included a new command called geometry. This command allows you to
# specify the dimensions of your window on the start in pixel. Hand over a
# string of the following form widthxheight to use this method. Here my window
# has a width (left to right) of 500 pixel and a height (top to bottom) of 200
# pixel.
root.geometry("500x200")
# Now I define my two StringVars, one for each menu I want to create. At the
# moment these VarVars do NOT have a value
var1 = tk.StringVar()
var2 = tk.StringVar()
# Now I can assign a predefined value to my StringVars using set()
var1.set("Option 1")
var2.set("snow")
# Now I create my first OptionMenu. I have to specify the parent first (root),
# than the associated VarVar (var1) and than I can hand over the options I want
# to include in my Menu in form of comma separated Strings. There is no limit
# to the number of options you can create here. Lastly I add the command
# attribute to execute one of the functions above as soon as the user clicks on
# an option.
menu = tk.OptionMenu(
    root, var1, "Option 1", "Option 2", "Option 3", command=display_selected
)
# Now I can put my OptionMenu in my GUI with pack, again I chose to put to the
# left side of my GUI.
menu.pack(side="left")
# Now I create my second OptionMenu, which allows me to change the background
# color of my label according to the chosen option.
menu2 = tk.OptionMenu(root, var2, "blue", "snow", "grey", command=change_bg)
# Again I put this OptionMenu in my GUI with the help of pack. I chose to put it
# also to the left side of my GUI but because of the behavior of pack (more
# about this later) it's on the right side of my first menu.
menu2.pack(side="left")
# Now I create my Label which displays the chosen option (text) from the first
# menu and is colored according to the chosen option (bg) of the second menu. As
# you can see I use the get method from my StringVars here to hand over the
# predefined values of my menus.
label1 = tk.Label(root, text=var1.get(), bg=var2.get())
# Again I put my label in my GUI
label1.pack(side="right")
# Last but not least I initialize my GUI with the mainloop).
root.mainloop()
