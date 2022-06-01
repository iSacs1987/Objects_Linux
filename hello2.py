"""
This is the example script for working with Buttons in our GUI. Here I show you
how to create Buttons and how to associate functions with them.
"""
# First we have to import tkinter
import tkinter as tk

# Now I can define my function to be able to execute some code as soon as the
# associated Button is clicked. We can have a complete program inside this
# function and everything works similiar to executing a normal program. Here I
# define a function without any arguments, because these kind of functions are
# easier to associate with our Buttons.
def ChangeText1():
    # I use the setter method config() to change the text in my label and to
    # give it a different background color.
    label1.config(text="I have new Text", background="green")
    # I can also include print commands, that result in print outs in the
    # terminal
    print("I did something")


# Now I can  create my GUI. At first we have to create our window the Tk()
# widget as basis for our GUI.
root = tk.Tk()
# Now I create my label in the same way we saw in our first example program.
label1 = tk.Label(root, text="Hello World!")
# Don't forget to use pack() so that it's placed inside our GUI
label1.pack()
# Now I can create my buttons. The first One is responsible for changing the
# text in my label by invocing the function ChangeText1. This is done by
# associating my Button with my Function in form of the command attribute. As
# long as our functions don't need any arguments we can use this simple way of
# associating buttons with them.
button1 = tk.Button(root, text="Change Text", command=ChangeText1)
# Now I have to place my Button inside my GUI again with pack
button1.pack()
# Here I create a second Button that invokes the built.in command root.destroy
# of our Tk widget. This method closes our window (it destroys the widget).
# Other widgets have this built-in function as well, for example labels.
button2 = tk.Button(root, text="Close Window", command=root.destroy)
# Now I have to place my Button inside my GUI again with pack
button2.pack()
# Last but not least we have to initialize our GUI with the help of mainloop.
root.mainloop()
