import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import ttk
from ScrollableFrame import *

rootDir = "."
root = tk.Tk()
root.title("Picasa")

#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
ttk.Style().theme_use('vista')

tree = ttk.Treeview(root)
frame = tk.Frame(root)
picFrame = ScrollableGridFrame(frame)

photos=[]
size=100,100

row = 0
col = 1

for dirName, subDirList, fileList in os.walk(rootDir):
    tree.insert('', 'end', dirName, text=dirName)
    for fileName in fileList:
        f=os.path.join(dirName,fileName)
        try:
            tree.insert(dirName, 'end', fileName,text=fileName)
            p = Image.open(f)
            p.thumbnail(size)
            pic = ImageTk.PhotoImage(p)
            photos.append(pic)
            tk.Label(picFrame.frame, image=pic).grid(row=row, column=col)
            if col % 3 == 0:
                row+=1
                col=1
            else:
                col += 1
        except:
            pass


#tree.pack(side='left', fill='both', expand=True)
#picFrame.pack(side='right', expand=True, fill='both')

#tree.pack(side=tk.LEFT, fill='both', expand=True)
#picFrame.pack(side=tk.RIGHT)

tree.grid(column=0, sticky='nsew')
picFrame.grid(sticky='nsew')
frame.grid(row=0, column=1, sticky='nsew')

root.mainloop()
