""" main view window """
import os

from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox
from view.menu import createmenu
from view.Tree import Tree
from view.Gallery import Gallery
from view.Status import Status

class Mainview():
    """ build the main screen """
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.tree = Tree(self.root, self.controller)
        self.gallery = Gallery(self.root, self.controller)
        self.status = Status(self.root, "Welcome back")
        createmenu(self.root, self.controller)

        self.tree.grid(row=0, column=0, stick=('nsw'))
        self.gallery.grid(row=0, column=1, sticky=('nsew'))
        self.status.grid(row=1, column=0, columnspan=2,sticky=('ew'))

        self.tree.build()
        self.gallery.build()

        self.root.title("Picasa")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def start(self):
        """ start the tkinter main loop """
        self.root.mainloop()

    def updatestatus(self, text):
        """ update the text in the status bar """
        self.status.updatestatus(text)

    def buildtree(self, folders=None):
        """ build the folder tree structure """
        self.tree.build(folders)

    def update(self):
        """ paint the screen """
        self.root.update()

    def getdir(self):
        """ Have the user specify a directory """
        return os.walk(filedialog.askdirectory())

    def quit(self):
        """ quit the app """
        self.root.quit()

    def message(self, title, text):
        """ display a pop up with a message """
        messagebox.showinfo(title, text)


