import tkinter as tk

from tkinter import ttk

root = tk.Tk()
root.title("Picasa")

leftFrame = tk.Frame(root)
rightFrame = tk.Frame(root)

redbutton = tk.Label(leftFrame, text="Red", fg="red")
redbutton.pack(side = 'left')

greenbutton = tk.Label(leftFrame, text="Brown", fg="brown")
greenbutton.pack( side = 'left' )

bluebutton = tk.Label(leftFrame, text="Blue", fg="blue")
bluebutton.pack( side = 'left' )

blackbutton = tk.Label(leftFrame, text="Black", fg="black")
blackbutton.pack( side = 'left')

redbutton = tk.Button(rightFrame, text="Red", fg="red")
redbutton.grid(row=0,column=0)

greenbutton = tk.Button(rightFrame, text="Brown", fg="brown")
greenbutton.grid(row=0,column=1)

bluebutton = tk.Button(rightFrame, text="Blue", fg="blue")
bluebutton.grid(row=1,column=0)

blackbutton = tk.Button(rightFrame, text="Black", fg="black")
blackbutton.grid(row=1,column=1)

leftFrame.pack(side='left')
rightFrame.pack(side='right')
root.mainloop()