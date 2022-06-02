"""
This is the example program for text fields. I will show you how to create such
a Widget and how to use the methods insert, get and delete
"""
# First we import tkinter
import tkinter as tk

# Now we define our functions to be used with the different Buttons. This first
# one inserts a text at the beginning of our text and than prints out the whole
# text in the terminal
def Text_Output():
    # First we use insrt, to write something in our Text Field. This is done
    # with the insert method that takes a positions (linenumber.columnnumber)
    # and a string as arguments. Here I insert something at the first line and
    # the first column.
    text1.insert(1.0, "This is a Test\n")
    # Now I can read out the whole text in my field with the get method. This
    # method takes two positions as arguments. Here I again start at the first
    # line and the first column. The second position is our special position
    # "end" which represents the last line and last column in our field
    Content = text1.get(1.0, "end")
    # I change the text of my label to tell the user what happened
    label1.config(text="Your pressed the first button")
    # I use two print out to show the text in my terminal
    print(Content)
    print(repr(Content))


# This is the second function that deletes the whole content of my text field
def Text_Clear():
    # Again I change the text in my label to tell the user what happened
    label1.config(text="Your pressed the second button")
    # Now I use the delete method, which similiar to get takes two positions as
    # arguments and removes the text between them. I use "end" again to be able
    # to delete the whole text
    text1.delete(1.0, "end")


# My last function counts how many characters are in my text field. Please
# keep in mind that line breaks also count as one character
def Text_length():
    # I show how many characters are in my label by using get, this time with
    # "end-1c" to ignore the last character, than len() the count how many
    # characters the returned string has. Since this returns an integer I have
    # to cast it to a str afterwards. Now I can use this string to create a
    # bigger string for my label by combining them with a "+"
    label1.config(
        text="You're text has " + str(len(text1.get(1.0, "end-1c"))) + " characters"
    )


# Here I create my GUI. First I create my Tk widget
root = tk.Tk()
# Now I create my text field with a yellow background so that its easier to see
# during our course.
text1 = tk.Text(root, background="yellow")
# Now I put my text field in my GUI
text1.pack()
# Afterwards I create three buttons which are associated with the functions
# above.
button1 = tk.Button(root, text="get Contents", command=Text_Output)
# Here I use the argument side="left" inside my pack command to specifiy the
# position where I want my Button to be. The options are left, right, top and
# bottom
button1.pack(side="left")
button2 = tk.Button(root, text="clear Text field", command=Text_Clear)
button2.pack(side="right")
button3 = tk.Button(root, text="Display Text length", command=Text_length)
button3.pack(side="bottom")
# Last but not least I create a label to display which button was pressed and
# how many characters are there in my text field
label1 = tk.Label(root, text="")
label1.pack(side="bottom")
# Last but not least I initialize my GUI with the mainloop()
root.mainloop()
