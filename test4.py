import tkinter as tk
from ScrollableFrame import ScrollableFrame

root = tk.Tk()
test4 = ScrollableFrame(root)

for i in range(100):
    tk.Label(test4.frame, text="OK people, this is button number "+str(i)).pack()

test4.pack()
root.mainloop()
