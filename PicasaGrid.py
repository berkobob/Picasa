import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import ttk

rootDir = "Pics"
root = tk.Tk()
root.title("Picasa")

tree = ttk.Treeview(root)

photos=[]
size=150,150

row = 0
col = 1

for dirName, subDirList, fileList in os.walk(rootDir):
    print ("DirName: %s" %dirName)
    tree.insert('', 'end', dirName, text=dirName)
    for fileName in fileList:
        f=os.path.join(dirName, fileName)
        print("\t%s" %f)
        try:
            tree.insert(dirName, 'end', fileName,text=fileName)
        except:
            fileName = fileName+"1"
            tree.insert(dirName,'end', fileName, text=fileName)
        try:
            p = Image.open(f)
            p.thumbnail(size)
            pic = ImageTk.PhotoImage(p)
            photos.append(pic)
            label = tk.Label(root, image = pic)
            label.grid(row=row, column=col)
            print("row %d col %d" %(row, col))
            print(row % 3)
            if col % 3 == 0:
                row+=1
                col=1
            else:
                col += 1
        except:
            pass

#s=ttk.Scrollbar(self, orient=VERTICAL, command=listbox.yview)
#listbox.configure(yscrollcommand-s.set)
tree.grid(column=0)
root.mainloop()
