"""
This si the program for frames
"""

import tkinter as tk


class pack_folien_layout:
    def __init__(self):
        self.root = tk.Tk()
        ####################### Plane 1 #####################
        self.yellow_top = tk.Frame(self.root)
        self.green = tk.Frame(self.root)
        self.yellow_bottom = tk.Frame(self.root)
        ####################### Plane 2 #####################
        self.label8 = tk.Label(self.yellow_top, text="Label 8")
        self.red = tk.Frame(self.green)
        self.brown = tk.Frame(self.green)
        self.label9 = tk.Label(self.yellow_bottom, text="Label 9")
        ####################### Plane 3 #####################
        self.button0 = tk.Button(self.red, text="Button 0")
        self.button1 = tk.Button(self.red, text="Button 1")
        self.button2 = tk.Button(self.red, text="Button 2")
        self.button3 = tk.Button(self.red, text="Button 3")
        self.button4 = tk.Button(self.red, text="Button 4")
        self.button5 = tk.Button(self.brown, text="Button 5")
        self.button6 = tk.Button(self.brown, text="Button 6")
        self.button7 = tk.Button(self.brown, text="Button 7")
        ###################### Packing the Widgets ##########
        ###################### Plane 1 ######################
        self.yellow_top.pack()
        self.green.pack()
        self.yellow_bottom.pack()
        ####################### Plane 2 #####################
        self.label8.pack()
        self.red.pack(side="left")
        self.brown.pack(side="left")
        self.label9.pack()
        ####################### Plane 3 #####################
        self.button0.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        self.button6.pack()
        self.button7.pack()
        self.root.mainloop()


pack_folien_layout()
