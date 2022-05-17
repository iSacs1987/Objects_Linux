import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
label1 = tk.Label(root,text="Hello World",background="white",foreground="red")
label1.place(width=75,height=20,x=100,y=200)
label2 = tk.Label(root,text="Hello World",background="white",foreground="blue")
label2.place(width=75,height=20,x=300,y=400)
label3 = tk.Label(root,text="Hello World",background="white",foreground="green")
label3.place(relwidth=0.2,relheight=0.1,relx=0.5,rely=0.5)

root.mainloop()