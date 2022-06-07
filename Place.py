"""
This is the example program for using the geometry manager place. This Gemoetry
manager allows absolute as well as relative positioning in our GUI. The main
advantage of it is its usage of pixel instead of text units for determining
the dimensions of your widget
"""
# first we import tkinter
import tkinter as tk

# Now we set up our GUI. Here I use simply 3 Labels to show you the effect of
# place in action
root = tk.Tk()
root.geometry("500x500")
# Now I create my three labels
label1 = tk.Label(root, text="Label1", background="white", foreground="red")
label2 = tk.Label(root, text="Label2", background="white", foreground="blue")
label3 = tk.Label(root, text="Label3", background="white", foreground="green")
# For the first two labels I use absolute positioning with the attribtues x and
# y to specify the coordinates and width and height to specify the dimension of
# my widgets. These attributes take whole numbers as arguments that represent
# the corresponding pixel number. You can think of your GUI as a form of
# coordinate system. The top left corner has x=0 and y=0, the top right corner
# has x=500 and y=0 (for our example here), the bottom left corner has x=0 and
# y=500 and the bottom right corner has x=500 and y=500.
label1.place(width=75, height=20, x=100, y=200)
label2.place(width=125, height=50, x=300, y=400)
# As mentioned above we can aslo use relative positioning. This is done with the
# attributes relx and rely for the position and relwidth and relheight for the
# size. Now the position and the size of our Widget depend on the size of our
# Window and thus are even changed automatically when its resized.
label3.place(relwidth=0.2, relheight=0.1, relx=0.5, rely=0.5)
# Last but not least we initialize our GUI
root.mainloop()
