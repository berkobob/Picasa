"""
Create a class for the Tree structure that represents the folders that contain
photos.
"""
import tkinter as tk

class Tree:
    """create tree structure"""

    def __init__(self, frame):
        self.frame = frame

    def createtree(self):
        """ build the tree from available info """
        return tk.Label(self.frame, text="Tree")

if __name__ == '__main__':
    root = tk.Tk()
    tree = Tree(root)
    tree.createtree().pack()
    root.mainloop()