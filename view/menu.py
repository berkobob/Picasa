"""
menubar for Picasa
"""

import tkinter as tk
from tkinter import messagebox

def quit_app(root):
    """ exit Picasa """
    root.quit()

def show_about(event=None):
    messagebox.showwarning("About", "My attempt at Picasa")

def show_msg(text):
    messagebox.showinfo("You pressed", text)
    print(text+" pressed")

def createmenu(root, controller):
    root=root
    menu = tk.Menu(root)
    controller = controller

    file_menu = tk.Menu(menu, tearoff=0)

    file_menu.add_command(label="Watch", command=lambda: controller("newfolder"))
    file_menu.add_command(label="Save",command=lambda: controller("save"))
    file_menu.add_command(label="Load",command=lambda: controller("load"))
    file_menu.add_separator()
    file_menu.add_command(label="Quit", command=lambda: quit_app(root))
    menu.add_cascade(label="File", menu=file_menu)

    view_menu = tk.Menu(menu, tearoff=0)
    line_numbers = tk.IntVar()
    line_numbers.set(1)

    view_menu.add_checkbutton(label="Line Numbers", variable=line_numbers)
    menu.add_cascade(label="View", menu=view_menu)

    help_menu = tk.Menu(menu, tearoff=0)
    help_menu.add_command(label="About",    
                    accelerator="Alt-A", 
                    command=show_about)
    menu.add_cascade(label="Help", menu=help_menu)
    root.bind('<Alt-A>', show_about)
    root.bind('<Alt-a>', show_about)


    root.config(menu=menu)

if __name__ == '__main__':
    root = tk.Tk()
    createmenu(root, None)
    root.mainloop()