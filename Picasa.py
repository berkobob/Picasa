"""
This is my attempt to replicate Picasa. I want to be able to scroll through
all of my photos without going into folders, one at a time. Eventually, I want
to search photos for people and things

Antoine Lever
"""
import os

from tkinter import Tk
from tkinter import filedialog
from menu import createmenu
from view.Tree import Tree
from view.Gallery import Gallery
from view.Status import Status
from data.Album import Album
from PIL import Image, ImageTk

def newfolder():
    """ import all the files and folders in a directory """
    for path, __, fileList in os.walk(filedialog.askdirectory()):
        for fileName in fileList:
            f = os.path.join(path, fileName)
            try:
                photo = Image.open(f)
                photo.thumbnail((200, 200))
                thumb = album.addthumb(ImageTk.PhotoImage(photo))
                pic = {'file': fileName,
                       'folder': path.split('\\')[-1],
                       'thumb': thumb,
                       'path': path
                      }
                album.addphoto(pic)
            except Exception as e:
                status.updatestatus(e)
    album.save()
    album.__folders__()
    tree.build(album.folders)
    root.update()


def controller(stuff):
    """ process all view commands """
    functions = {'newfolder': newfolder}
    functions[stuff]()


if __name__ == '__main__':
    album = Album()

    root = Tk()
    tree = Tree()
    gallery = Gallery()
    status = Status()
 
    createmenu(root, controller)
    tree.createtree(controller).grid(row=0, column=0, sticky=('nsw'))
    gallery.creategallery().grid(row=0, column=1, sticky=('nsew'))
    status.createsttatusbar().grid(row=1, column=0, columnspan=2, sticky=('ew'))

    root.mainloop()
