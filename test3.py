"""attempt to get a pack and  grid working side by side"""

import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def thumbnail(f):
    """ change photo into thumbnail """
    try:
        pic = Image.open(f)
        pic.thumbnail((150, 150))
        pic = ImageTk.PhotoImage(pic)
        return pic
    except:
        return False

root = tk.Tk()
root.title("Picasa")

tree = ttk.Treeview(root)
right = tk.Frame(root)
photoFrame = tk.Canvas(right, scrollregion=(0, 0, 500, 500))
test = ttk.ScrolledFrame() 

photos = []
thumbnails = []

for dirs, sub, pics in os.walk("Pics"):
    tree.insert('', 'end', dirs, text=dirs)
    tree.item(dirs, open=True)
    for pic in pics:
        f = os.path.join(dirs, pic)
        tree.insert(dirs, 'end', f, text=pic)
        photos.append(f)

row, col = 0, 0

for photo in photos:
    pic = thumbnail(photo)
    if pic:
        thumbnails.append(pic)
        label = tk.Label(photoFrame, image=pic).grid(row=row, column=col)
        if col == 3 :
            row += 1
            col = 0
        else:
            col += 1

vbar = tk.Scrollbar(right, orient=tk.VERTICAL)
vbar.pack(side=tk.RIGHT, fill='y')
vbar.config(command=photoFrame.yview)
photoFrame.config(yscrollcommand=vbar.set)
photoFrame.config(width=300, height=300)
photoFrame.pack(side=tk.LEFT, expand='true', fill=tk.BOTH)


tree.pack(fill='both', expand='True', side='left')
right.pack(side='right', fill='both', expand=True)
root.mainloop()
