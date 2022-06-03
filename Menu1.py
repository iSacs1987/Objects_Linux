import tkinter as tk
 
def save():
    pass
 
def load():
    pass   
 
root = tk.Tk()
root.geometry("200x150")
mainmenu = tk.Menu(root)
mainmenu.add_command(label = "Save", command= save)  
mainmenu.add_command(label = "Load", command= load)
mainmenu.add_command(label = "Exit", command= root.destroy)
root.config(menu = mainmenu)
root.mainloop()