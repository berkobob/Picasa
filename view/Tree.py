"""
Create a class for the Tree structure that represents the folders that contain
photos.
"""
#pylint: disable-msg=W0702
#pylint: disable-msg=W0621
import tkinter as tk

try:
    from view.Myframe import MyFrame
except:
    from Myframe import MyFrame

class Tree(MyFrame):
    """ create tree structure using scrollable frame """
    def __init__(self, parent, controller):
        MyFrame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def build(self, folders=["Add folder to watchlist"]):
        """ create a tree structure from the list of folders """
        i = 0
        for folder in folders:
            page = tk.Button(super().get(), text=folder, relief='flat')
            page.grid(row=i, sticky='w')
            page.configure(command=lambda p=page: self.controller(p))
            i += 1

def controller(text):
    """" A controller for testing purposes """
    print(text['text'])
    print(type(text))
    #print(text)

if __name__ == '__main__':
    root = tk.Tk()
    tree = Tree(root, controller)
    tree.build(list(range(25)))
    tree.grid()
    root.mainloop()
