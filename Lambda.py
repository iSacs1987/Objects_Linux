"""
This is the example script for using the functional voodoo lambda. This lambda
keyword allows us to associate functions with arguments with our widgets and to
create so-called 'one-line functions'.
"""
# First we import tkinter and the font module
import tkinter as tk
import tkinter.font as font

# Now I define a small function that takes the argument Text to change the text
# of my label and to create a simple print out
def ChangeText1(Text):
    w.config(text=Text)
    print(Text)


# Now I create my GUI, define my font and set the geometry
root = tk.Tk()
myFont = font.Font(size=20)
root.geometry("300x200")
# Now I create a simple label that shows a simple text
w = tk.Label(root, text="Hello World!", font=myFont)
w.pack()
# Now I create my button. By using command=lambda:ChangeText1("Hello Christoph")
# I can invoke my funtion ChangeText1 with the argument "Hello Christoph". If we
# would leave out the lambda Python would see ChangeText1 as a call back of our
# function and thus execute it while generating our GUI. Furthermore we would
# NOT be able to invoke the funtion with a Button click. To suppress the call
# back of our function during the creation of our GUI we have to use lambda her
# We could even include multiple functions after this lambda by using something
# like this: command=lambda:[function1(parameters),function2(parameters)]
button1 = tk.Button(
    root,
    text="Hello World!",
    font=myFont,
    command=lambda: ChangeText1("Hello Christoph"),
)
button1.pack()
# Now we initialize our GUI
root.mainloop()
# I included an example for the usage of lambda in combination with one-line
# functions here. The line 43 defines a function called result that takes two
# arguments (x and y) and returns the multiplication product of these two.
result = lambda x, y: x * y
# Now we can call back this one-line function just like we would do for more
# complex functions that were created using the def keyword.
print(result(5, 4))
