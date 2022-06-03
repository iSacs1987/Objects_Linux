import tkinter as tk

def DisplayChoice():
    text = "Current Value: " + str(spinbox.get())
    label.configure(text = text)


root = tk.Tk()
frame = tk.Frame(root, width = 200, height = 80)
values = ["Apple", "Banana", "Cabbage", "Beans"]
spinbox = tk.Spinbox(root, from_ = 0, to = 10,increment = 1)
# spinbox = tk.Spinbox(root, from_ = 0, to = 10,increment = 1,command = DisplayChoice)
# spinbox = tk.Spinbox(root, from_ = 0, to = 10,increment = 1, values = values,command = DisplayChoice)
spinbox.pack()
text1 = "Current Value: " + str(spinbox.get())
label = tk.Label(root, text = text1)
label.pack()
button1 = tk.Button(root, text="Display Choice", command=DisplayChoice)
button1.pack()
frame.pack(padx = 10, pady = 10, expand = True, fill = tk.BOTH)
root.mainloop()