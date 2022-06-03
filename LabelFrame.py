import tkinter as tk

root = tk.Tk()
root.geometry('300x200')
label_frame = tk.LabelFrame(root, text = "LABELFRAME WIDGET")
label_frame.pack()
var = tk.IntVar()
radio1 = tk.Radiobutton(label_frame, text = "Option1",variable = var, value = 1)
radio1.pack()
radio2 = tk.Radiobutton(label_frame, text = "Option2",variable = var, value = 2)
radio2.pack()
radio3 = tk.Radiobutton(label_frame, text = "Option3",variable = var, value = 3)
radio3.pack()
root.mainloop()