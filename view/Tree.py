"""
Create a class for the Tree structure that represents the folders that contain
photos.
"""
import tkinter as tk
from view.Myframe import MyFrame

class Tree(MyFrame):
    """ create tree structure using scrollable frame """
    def __init__(self, root=None):
        MyFrame.__init__(self, root)
        self.frame = super().get()

    def createtree(self, controller):
        self.controller = controller
        return self

    def build(self, folders):
        i=0
        for folder in folders:
            tk.Button(super().get(), text=folder, relief='flat').grid(row=i, sticky='w')
            i+=1

if __name__ == '__main__':
    root = tk.Tk()
    tree = Tree(root)
    #tree.createtree().pack()
    root.mainloop()