"""
This is the example script for working with Entry Fields and the associated
VarVars. I will show you how to create Entry Fields, how to define VarVars and
how to work with them.
"""
# First we have to import tkinter
import tkinter as tk

# Now I can define my function that I associate with my button later on. You
# need to define these functions before you can create your GUI otherwise, the
# button is not able to recognize it.
def add_up():
    # First I read out the value from my two VarVars input1 and input2. What
    # happens here is that the get() method takes the string that is in the
    # associated entry field (edit1 or edit2), reads it in and assigns it to
    # the VarVar. Now I can assign this value to a new variable with the help
    # of our getter method. Here I do all things step wise, but you could use
    # the get() method also in line 23 for example
    number1 = input1.get()
    number2 = input2.get()
    # Now I add up my two values. Since both VarVars are StringVars I have to
    # cast them to floats here so that I can run my mathematical calculation.
    result = float(number1) + float(number2)
    # Now I use the setter method of my label to display the result of my
    # calculation in my GUI. Please keep in mind that the variable result is of
    # type float, but our label can only display strings. So we have to cast it
    # to string to be able to display it.
    label1.config(text=str(result))


# Now we can create our GUI, by first creating our window the Tk widget
root = tk.Tk()
# Afterwards I can define my two VarVars. Here I use StringVars, but during our
# course we saw that you can also use IntVars or DoubleVars in combination with
# Entry fields. Please keep in mind that you have to define these VarVars after
# you created your Tk widget.
input1 = tk.StringVar()
input2 = tk.StringVar()
# Now I can create my Entry fields and associate them with my VarVars. This is
# done with the help of the attribute textvariable. Unfortunately this is NOT
# a general attribute that all Widgets have. We will see that different Widgets
# have different attributes to associate them with VarVars and we just have to
# remember how these attributes are named. Here I also use the attributes font
# and width to create a bigger GUI so that it's easier to see what happens.
edit1 = tk.Entry(root, textvariable=input1, font=15, width=33)
edit2 = tk.Entry(root, textvariable=input2, font=15, width=33)
# Now I can put my Entry fields in my GUI with the pack() method. The order of
# your Widgets in your GUI depends on the order of your pack commands. That
# means the Widget you pack first is at the top, than comes the second one
# beneath it and so on. This is the default behavior. We will learn how to
# change this behavior and how to use other methods to align our Widgets later.
edit1.pack()
edit2.pack()
# Now I create my Button that is associated with my function add_up
button1 = tk.Button(root, text="Click Me", command=add_up, width=30, font=15)
# I put my Button in my GUI
button1.pack()
# Lastly I create a Label to display the results. By leaving out the text
# attribute I can create an "empty" label that doesn't display anything.
label1 = tk.Label(root, font=15, width=33)
# I put my Label in my GUI
label1.pack()
# Now I intialize my GUI with mainloop()
root.mainloop()
