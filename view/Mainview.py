""" main view window """
import os

from tkinter import Tk
from tkinter import filedialog
from view.menu import createmenu
from view.Tree import Tree
from view.Gallery import Gallery
from view.Status import Status

class Mainview():
    """ build the main screen """
    def __init__(self, controller=None):
        self.controller = controller
        self.root = Tk()
        self.tree = Tree()
        self.gallery = Gallery()
        self.status = Status()

        createmenu(self.root, self.controller)
        self.tree.createtree(self.controller).grid(row=0, column=0, sticky=('nsw'))
        self.gallery.creategallery().grid(row=0, column=1, sticky=('nsew'))
        self.status.createsttatusbar().grid(row=1, column=0, columnspan=2,
                                            sticky=('ew'))

    def start(self):
        """ start the tkinter main loop """
        self.root.mainloop()

    def updatestatus(self, text):
        """ update the text in the status bar """
        self.status.updatestatus(text)

    def buildtree(self, folders):
        """ build the folder tree structure """
        self.tree.build(folders)

    def update(self):
        """ paint the screen """
        self.root.update()

    def getdir(self):
        """ Have the user specify a directory """
        return os.walk(filedialog.askdirectory())


