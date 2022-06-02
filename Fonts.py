"""
This is the example script for working with different fonts in tkinter. Here I
show you the import and the definition of your own fonts and than how to use
them with your widgets
"""
# First we need our standard import
import tkinter as tk

# Than we have to import tkinter.font a module which allows us to create our own
# fonts for our GUI
import tkinter.font as font

# Now we create our Window with the Tk() Widget
root = tk.Tk()
# Now I can define my two fonts for my labels. Please do this after you created
# the window with the Tk() widget (line 12). When creating these fonts we can
# only use font families which are available to us in the operating system. So
# here I can NOT use Times for example, since its not installed in the VM. Each
# font has 6 different attributes (family, size, slant, weight, underline and
# overstrike), you can find the description of them in the presentation. Here
# I create an italic, underlined Bitstream font with a size of 20 and a bold
# Serif font with a size of 10.
myFont = font.Font(family="Bitstream", slant="italic", size=20, underline=1)
myFont2 = font.Font(family="Serif", weight="bold", size=10)
# After I defined my two fonts I can now use them for my Widgets. To be able to
# do this, I have to use the font attribute and hand over the name of your
# created font. Unfortunately we won't see any difference here in our VM :(
label1 = tk.Label(root, text="Hallo Christoph", font=myFont)
# Now I can put my label in my GUI
label1.pack()
# Now I create a second label which uses my second font
label2 = tk.Label(root, text="Hallo Christoph", font=myFont2)
label2.pack()
# Last but not least I intialize my GUI with mainloop()
root.mainloop()
