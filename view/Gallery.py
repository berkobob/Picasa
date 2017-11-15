"""
Scroll through all the thumbnails in folder order
Try and make panaronmic ones wider
Try and make vids into gifs? 
Separator between folders.
"""
#pylint: disable-msg=W0621
import tkinter as tk
try:
    from view.Myframe import MyFrame
except:
    from Myframe import MyFrame

class Gallery(MyFrame):
    """ Scroll dem pictures """
    def __init__(self, parent, controller):
        MyFrame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(0, weight=5)
        self.rowconfigure(0, weight=1)

    def build(self, pics=["No pictures to display"]):
        """ put some data in """
        i = 0
        for pic in pics:
            tk.Label(super().get(), text=pic).grid(row=i) 
            i += 1

def controller(text=None):
    """ controller for testing """
    print(text)

if __name__ == '__main__':
    root = tk.Tk()
    frame = Gallery(root, controller)
    frame.grid()
    #frame.build(list(range(25)))
    frame.build()
    root.mainloop()