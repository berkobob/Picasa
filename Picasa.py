import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import ttk
from ScrollableFrame import *
from menu import createmenu

rootDir = "."
root = tk.Tk()
root.title("Picasa")
#root.attributes("-fullscreen", True)
root.state("zoomed")

#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
ttk.Style().theme_use('vista')

def test(a):
    print("It worked " + str(a))

createmenu(root, test)

tree = ttk.Treeview(root)
swidth = (root.winfo_screenwidth())
sheight = root.winfo_screenheight()
frame = ttk.Frame(root)
picFrame = ScrollableGridFrame(frame)

#tree.grid_propagate()
#frame.grid_propagate()

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

photos=[]
size=300,300

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
#frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
