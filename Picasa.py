"""
This is my attempt to replicate Picasa. I want to be able to scroll through
all of my photos without going into folders, one at a time. Eventually, I want
to search photos for people and things

Antoine Lever
"""

from tkinter import Tk
from tkinter import filedialog
from menu import createmenu
from view.Tree import Tree
from view.Gallery import Gallery
from view.Status import Status

def newfolder():
    """ import all the files and folders in a directory """
    print(filedialog.askdirectory())

def controller(stuff):
    """ process all view commands """
    print(stuff)
    if stuff == 'Import':
        newfolder()

if __name__ == '__main__':
    root = Tk()
    tree = Tree(root)
    gallery = Gallery(root)
    status = Status(root)

    createmenu(root, controller)
    tree.createtree().grid(row=0, column=0)
    gallery.creategallery().grid(row=0, column=1, sticky=('nsew'))
    status.createsttatusbar().grid(row=1, column=0, columnspan=2, sticky=('ew'))

    root.mainloop()
