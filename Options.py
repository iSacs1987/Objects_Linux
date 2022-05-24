"""
This is the example for an option menu.
"""
import tkinter as tk


def display_selected(choice):
    choice = var1.get()
    print(choice)
    label1.config(text=choice)


def change_bg(choice):
    label1.config(bg=var2.get())


root = tk.Tk()
root.geometry("500x200")
var1 = tk.StringVar()
var2 = tk.StringVar()
var1.set("Option 1")
var2.set("snow")
menu = tk.OptionMenu(
    root, var1, "Option 1", "Option 2", "Option 3", command=display_selected,
)
menu.pack(side="left")
menu2 = tk.OptionMenu(root, var2, "blue", "snow", "grey", command=change_bg,)
menu2.pack(side="left")
label1 = tk.Label(root, text=var1.get(), bg=var2.get())
label1.pack(side="right")
root.mainloop()
