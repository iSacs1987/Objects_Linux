"""
This is the example for working with grid. Here I create a small login screen.
"""
# We import tkinter
import tkinter as tk

# Now we create our Window, set the geometry, the title and suppress the
# resizing by the user. As you can see resizeable takes either True/False or 1/0
root = tk.Tk()
root.geometry("320x100")
root.title("Login")
root.resizable(0, 0)
# Now I want one of my columns to be bigger than the remaining columns. To do
# this I have to use columnconfigure and define one standard column (here column
# 0) with a weight of 1. So now all remaining columns have the same size as
# this column 0. Now I can specify that column 100 should three times as big by
# setting the weight to 3 in my columnconfigure. I use column 100 in this
# example to show you what I meant with gaps in the indices. By using a column
# index of 100 for my second column, I'm able to add more widgets in between the
# first and second columns simply by using indices like 50 or so.
root.columnconfigure(0, weight=1)
root.columnconfigure(100, weight=3)
# Now I create a label
username_label = tk.Label(root, text="Username:")
# Now I can use grid() to place my Widget in my GUI. You ALWAYS have to specify
# the column and the row, everything else is optional. I put this label in my
# first column (0) and my first row (0 as well). Than I use the sticky method
# in combination with tk.W to tell the grid that this label should be glued to
# the left side of my field. Furthermore I add a bit of padding around my widget
# padx and pady take pixel values and add the padding accordingly (x on the left
# and the right, y on the top and the bottom).
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
# Now I create my first Entry Field
username_entry = tk.Entry(root)
# Now I can place my Entry field on my grid. This time I use tk.E to glue my
# widget to the right side of my Field
username_entry.grid(column=100, row=0, sticky=tk.E, padx=5, pady=5)
# Now I can add a second label and a second Entry field to my grid by simply
# using row=1 to tell grid, to create a second row on my GUI.
password_label = tk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
# For this Entry I included the attribute show that allows to hide the typed in
# text behind any character (here an asterisk). The neat thing about this is,
# that this does NOT change the contenrs of the String but just how its shown
# on our GUI.
password_entry = tk.Entry(root, show="*")
password_entry.grid(column=100, row=1, sticky=tk.E, padx=5, pady=5)
# Lst but not least I add a button to my GUI.
login_button = tk.Button(root, text="Login")
# I place this button in the third row of my grid, but use an index of 3 so that
# I leave me the option of adding an additional row in between my Label/Entry
# lines and my Button
login_button.grid(column=100, row=3, sticky=tk.E, padx=5, pady=5)
# Last but not least I initialize my GUI
root.mainloop()
