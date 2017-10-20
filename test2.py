"""attempt to get a pack and  grid working side by side"""

import tkinter as tk
from tkinter import ttk
import os

root = tk.Tk()
root.title("Picasa")

photoFrame = tk.Frame(root)
tree = ttk.Treeview(root)

for dirs, sub, pics in os.walk("Pics"):
    tree.insert('', 'end', dirs, text=dirs)
    tree.item(dirs, open=True)
    for pic in pics:
        f = os.path.join(dirs,pic)
        tree.insert(dirs, 'end', f, text=pic)

tree.pack(fill='both', expand='True', side='left')

redbutton = tk.Button(photoFrame, text="Red", fg="red").grid(row=0,column=0)

greenbutton = tk.Button(photoFrame, text="Brown", fg="brown").grid(row=0,column=1)

bluebutton = tk.Button(photoFrame, text="Blue", fg="blue")
bluebutton.grid(row=1,column=0)

blackbutton = tk.Button(photoFrame, text="Black", fg="black")
blackbutton.grid(row=1,column=1)

redbutton = tk.Label(photoFrame, text="Red", fg="red")
redbutton.grid(row=0,column=2)

greenbutton = tk.Label(photoFrame, text="Brown", fg="brown")
greenbutton.grid(row=1,column=2)

bluebutton = tk.Label(photoFrame, text="Blue", fg="blue")
bluebutton.grid(row=2,column=0)

blackbutton = tk.Label(photoFrame, text="Black", fg="black")
blackbutton.grid(row=2,column=2)

photoFrame.pack(side='right')
root.mainloop()
