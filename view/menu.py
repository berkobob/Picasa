"""
menubar for Picasa
"""
#pylint: disable-msg=W0621
import tkinter as tk

def createmenu(root, controller):
    """ Build the main picasa menu """
    menu = tk.Menu(root)

    file_menu = tk.Menu(menu, tearoff=0)

    file_menu.add_command(label="Watch", accelerator='Alt-W',
                          command=lambda: controller('menu', "newfolder"))
    file_menu.add_command(label="Save", command=lambda: controller('menu', "save"))
    file_menu.add_command(label="Load", command=lambda: controller('menu', "load"))
    file_menu.add_separator()
    file_menu.add_command(label="Quit", command=lambda: controller('menu', "quit"))
    menu.add_cascade(label="File", menu=file_menu)

    view_menu = tk.Menu(menu, tearoff=0)
    line_numbers = tk.IntVar()
    line_numbers.set(1)

    view_menu.add_checkbutton(label="Line Numbers", variable=line_numbers)
    menu.add_cascade(label="View", menu=view_menu)

    help_menu = tk.Menu(menu, tearoff=0)
    help_menu.add_command(label="About",
                          accelerator="Alt-A",
                          command=lambda: controller('menu', 'about'))
    menu.add_cascade(label="Help", menu=help_menu)
    root.bind('<Alt-A>', lambda: controller('menu', 'about'))
    root.bind('<Alt-a>', lambda: controller('menu', 'about'))

    root.config(menu=menu)

def controller(text):
    """ controller for testing purposes only """
    print(text)

if __name__ == '__main__':
    win = tk.Tk()
    createmenu(win, controller)
    win.mainloop()
