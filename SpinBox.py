"""
This is the example program for creating spinboxes. Here I show you the creation
of three different spinboxes, by using different increments, associating a
function with them and associating a list of strings with it.
"""
# First we impor tkinter and tkinter.font
import tkinter as tk
import tkinter.font as font

# Now I define my function to show the chosen value in a label
def DisplayChoice():
    # I read in the value from my spinbox with get() and create a sring with it
    text = "Current Value: " + str(spinbox.get())
    # Now I can change the text of my label to display the result
    label.configure(text=text)


# Now we set up our GUI
root = tk.Tk()
# We define a cutom-made font for better visibility
myFont = font.Font(size=20)
# Now I create a list of strings which I will need later on.
values = ["Apple", "Banana", "Cabbage", "Beans"]
# Now I can define my first spinbox by handing over the parent (root) and the
# range of my values (from_ and to). Per default the increment of these values
# is 1 so we could exclude it here. I added this attribute here to show you the
# difference between the first and the second spinbox
spinbox = tk.Spinbox(root, from_=0, to=10, increment=1, font=myFont)
# Now I define my second spinbox. This time I changed the increment to 0.5 so
# now we get values from 0.0 , 0.5, 1.0 ... 9.5, 10.0. As you can see we now
# have values of the type float and not of the type integer anymore. So by
# using a floating point number increment we can change the type of of our input
# Furthermore I associated the function in line 11 with my spinbox with the help
# of the already known attribute command. Now any time the user clicks on one of
# the arrows or maneuvers through the spinbox via arrow keys the function is
# called back and the text in the label changes automatically.
# spinbox = tk.Spinbox(
#     root, from_=0, to=10, increment=0.5, command=DisplayChoice, font=myFont
# )
# Our third spinbox is now associated with a list of strings via the attribute
# values. The neat thing about this is, that now we don't have to specify a
# a range (from_ and to) or an increment, since the values of the list define
# these parameters.
# spinbox = tk.Spinbox(root, values=values, command=DisplayChoice, font=myFont)
# Now we can add our spinbox to our GUI
spinbox.pack()
# Now I define a string variable to display in our label. I use get() to show
# the starting value of our spinbox
text1 = "Current Value: " + str(spinbox.get())
# Now I create a label and a Button and put them into my GUI.
label = tk.Label(root, text=text1, font=myFont)
label.pack()
button1 = tk.Button(root, text="Display Choice", command=DisplayChoice, font=myFont)
button1.pack()
# Last but not Least I intialize my GUI
root.mainloop()
