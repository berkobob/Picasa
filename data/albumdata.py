""" manage the Picasa meta data """
import json

class Album():
    """ manage the Picasa meta classa """
    def __init__(self):
        self.album = []
        self.thumbs = []
        self.folders = set()

    def addphoto(self, photo):
        """ add a photo to the album """
        self.album.append(photo)

    def addthumb(self, pic):
        """ add a thumbnail to the database """
        self.thumbs.append(pic)
        return self.thumbs.index(pic)

    def save(self):
        """ save the album to disk """
        with open('album', 'w') as f:
            json.dump(self.album, f)

    def __folders__(self):
        for pic in self.album:
            self.folders.add(pic['folder'])
        print(self.folders)

    def getalbum(self):
        return self.album

    def test(self):
        for pic in self.album:
            print(pic['folder'])
