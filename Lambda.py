import tkinter as tk

def ChangeText1(Text):
    w.config(text=Text)
    print(Text)

root = tk.Tk()
root.geometry('300x200')
w = tk.Label(root, text="Hello World!")
w.pack()
button1 = tk.Button(root, text="Hello World!", command=lambda:ChangeText1("Hello Christoph"))
button1.pack()
root.mainloop()
