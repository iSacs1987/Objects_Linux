"""
This is the example for working with grid
"""

import tkinter as tk

root = tk.Tk()
root.geometry("240x100")
root.title("Login")
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.columnconfigure(100, weight=3)
username_label = tk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(column=100, row=0, sticky=tk.E, padx=5, pady=5)
password_label = tk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(column=100, row=1, sticky=tk.E, padx=5, pady=5)
login_button = tk.Button(root, text="Login")
login_button.grid(column=100, row=3, sticky=tk.E, padx=5, pady=5)
root.mainloop()
