"""
This is the program for frames. The color coding is the same as you saw in my
presentation. I won't add much comments here since this program is mainly for
showing you hwo to use pack ind combination with Frames to generate more complex
layouts.
"""

import tkinter as tk

root = tk.Tk()
####################### Plane 1 #####################
yellow_top = tk.Frame(root)
green = tk.Frame(root)  # big Frame in the center
yellow_bottom = tk.Frame(root)
####################### Plane 2 #####################
label8 = tk.Label(yellow_top, text="Label 8")
red = tk.Frame(green)  # frame on the left side of the center
brown = tk.Frame(green)  # frame on the right side of the center
label9 = tk.Label(yellow_bottom, text="Label 9")
####################### Plane 3 #####################
button0 = tk.Button(red, text="Button 0")
button1 = tk.Button(red, text="Button 1")
button2 = tk.Button(red, text="Button 2")
button3 = tk.Button(red, text="Button 3")
button4 = tk.Button(red, text="Button 4")
button5 = tk.Button(brown, text="Button 5")
button6 = tk.Button(brown, text="Button 6")
button7 = tk.Button(brown, text="Button 7")
button8 = tk.Button(brown, text="Button 8")
###################### Packing the Widgets ##########
# We don't have to follow the same order as above. We could even mix up the
# order completely as long as we place all of our Widgets at the end
###################### Plane 1 ######################
yellow_top.pack()
green.pack()
yellow_bottom.pack()
####################### Plane 2 #####################
label8.pack()
red.pack(side="left")
brown.pack(side="left")
label9.pack()
####################### Plane 3 #####################
button0.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
root.mainloop()
