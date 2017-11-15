"""
This is my attempt to replicate Picasa. I want to be able to scroll through
all of my photos without going into folders, one at a time. Eventually, I want
to search photos for people and things

Antoine Lever
"""
#pylint: disable-msg=W0703
import os

from data.Album import Album
from view.Mainview import Mainview
from PIL import Image, ImageTk


def newfolder():
    """ import all the files and folders in a directory """
    for path, __, fileList in mview.getdir():
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
                mview.updatestatus(e)
    album.save()
    album.__folders__()
    mview.buildtree(album.folders)
    mview.update()


def controller(action):
    """ process all view commands """
    functions = {'newfolder': newfolder}
    try:
        functions[action]()
    except Exception:
        mview.updatestatus(action+" function not yet implemented")


if __name__ == '__main__':
    album = Album()
    mview = Mainview(controller)
    mview.start()
