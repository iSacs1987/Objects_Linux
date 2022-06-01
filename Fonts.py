import tkinter as tk
import tkinter.font as font

root = tk.Tk()

myFont = font.Font(family="Bitstream", slant="italic", size=20, underline=1)
myFont2 = font.Font(family="Serif", weight="bold", size=10)

label1 = tk.Label(root, text="Hallo Christoph", font=myFont)
label1.pack()
label2 = tk.Label(root, text="Hallo Christoph", font=myFont2)
label2.pack()
root.mainloop()
