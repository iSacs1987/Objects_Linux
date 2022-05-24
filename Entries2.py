import tkinter as tk


def add_up():
    zahl1 = input1.get()
    zahl2 = input2.get()
    ergebnis = float(zahl1) + float(zahl2)
    print(ergebnis)


root = tk.Tk()
input1 = tk.StringVar()
input2 = tk.StringVar()
edit1 = tk.Entry(root, textvariable=input1)
edit2 = tk.Entry(root, textvariable=input2)
edit1.pack()
edit2.pack()
root.mainloop()
