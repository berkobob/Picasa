"""
Create a class for the Tree structure that represents the folders that contain
photos.
"""
import tkinter as tk

class Tree(tk.Frame):
    """ create tree structure """
    def __init__(self, frame=None):
        tk.Frame.__init__(self, frame)

    def createtree(self):
        """ build the tree from available info """
        tk.Label(self, text="Tree").pack()
        return self

    def build(self, folders):
        """ rebuild the tree structure """
        for widget in self.winfo_children():
            widget.destroy()
        row = 0
        for folder in folders:
            print(folder)
            tk.Label(self, text=folder).pack()
            row+=1


if __name__ == '__main__':
    root = tk.Tk()
    tree = Tree(root)
    tree.createtree().pack()
    root.mainloop()