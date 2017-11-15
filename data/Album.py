""" manage the Picasa meta data """
import json

class Album():
    """ manage the Picasa meta data """
    def __init__(self):
        self.album = []         # Photo meta data
        self.thumbs = []        # Thumbnails of each photo
        self.folders = set()    # A list of folders to monitor

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

if __name__ == '__main__':
    print("Picasa database")
    # Consider reading the JSON and dumping
    with open('album', 'r') as f:
        album = json.load(f)
    print(album)
        