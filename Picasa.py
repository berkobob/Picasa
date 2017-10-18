import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import ttk

rootDir = "."
root = tk.Tk()
root.title("Picasa")

#dirName, subDirList, fileList = os.walk(rootDir)
treeFrame = tk.Frame(root)
tree = ttk.Treeview(treeFrame)
picFrame = tk.Frame(root)

photos=[]
size=100,100

for dirName, subDirList, fileList in os.walk(rootDir):
    print ("DirName: %s" %dirName)
    print("SubDirList: %s" %subDirList)
    tree.insert('', 'end', dirName, text=dirName)
    for fileName in fileList:
        f=os.path.join(dirName,fileName)
        print("\t%s" %f)
        tree.insert(dirName, 'end', fileName,text=fileName)
        try:
            pic = Image.open(f).thumbnail(size)
            pic = ImageTk.PhotoImage(pic)
            photos.append(pic)
            label = tk.Label(picFrame, image = pic)
            label.pack(side='right', fill = 'both', expand='yes')
        except:
            pass


tree.pack(fill='both', expand='True')
treeFrame.pack(side='left')

picFrame.pack(side='right')
root.mainloop()
