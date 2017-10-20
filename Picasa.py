import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import ttk

rootDir = "."
root = tk.Tk()
root.title("Picasa")

#dirName, subDirList, fileList = os.walk(rootDir)
# treeFrame = tk.Frame(root)
tree = ttk.Treeview(root)
# picFrame = tk.Frame(root)

photos=[]
size=100,100

row = 0
col = 1

for dirName, subDirList, fileList in os.walk(rootDir):
    print ("DirName: %s" %dirName)
    print("SubDirList: %s" %subDirList)
    tree.insert('', 'end', dirName, text=dirName)
    for fileName in fileList:
        f=os.path.join(dirName,fileName)
        print("\t%s" %f)
        tree.insert(dirName, 'end', fileName,text=fileName)
        try:
            p = Image.open(f)
            p.thumbnail(size)
            pic = ImageTk.PhotoImage(p)
            photos.append(pic)
            label = tk.Label(root, image = pic)
            label.grid(row=row, col=col)
            if row % 3 == 0:
                row+=1
                col=1
            else:
                col += 1
        except:
            pass


#tree.pack(fill='both', expand='True')
tree.grid(col=0)
#treeFrame.pack(side='left')

#picFrame.pack(side='right')
root.mainloop()
