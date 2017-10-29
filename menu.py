import tkinter as tk
from tkinter import messagebox

root=tk.Tk()

def quit_app():
    root.quit()

def show_about(event=None):
    messagebox.showwarning("About", "My attempt at Picasa")

def show_msg(text):
    messagebox.showinfo("You pressed", text)
    print(text+" pressed")

menu = tk.Menu(root)

file_menu = tk.Menu(menu, tearoff=0)

file_menu.add_command(label="Open", command=lambda: show_msg("Open"))
file_menu.add_command(label="Save",command=lambda: show_msg("Save"))
file_menu.add_command(label="Load",command=lambda: show_msg("Load"))
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_app)
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

root.mainloop()