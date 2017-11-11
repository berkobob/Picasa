"""
Scroll through all the thumbnails in folder order
Try and make panaronmic ones wider
Try and make vids into gifs? 
Separator between folders.
"""
import tkinter as tk

class Gallery(tk.Frame):
    """ Scroll dem pictures """
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)

    def creategallery(self):
        """ put some data in """
        tk.Label(self, text="This is where the pictures will go").pack()
        return self

if __name__ == '__main__':
    root = tk.Tk()
    frame = Gallery(root)
    frame.pack()
    tk.Label(frame, text="Let's see if this works").pack()
    root.mainloop()