"""
Create a status bar to go on the bottom of the screen
"""

import tkinter as tk

class Status(tk.Frame):

    """ Create a scroll bar """
    def __init__(self, parent, initial=None):
        tk.Frame.__init__(self, parent)
        self.status = tk.Label(self, text=initial)
        self.status.grid(sticky='w')

    def updatestatus(self, msg):
        """ update the status message """
        self.status.config(text=msg)

if __name__ == '__main__':
    root = tk.Tk()
    status = Status(root, "First status")
    status.grid(row=2)
    tk.Label(root, text="Let's see if this works").grid(row=0)
    b=tk.Button(root, text="Change status",
                command=lambda: status.updatestatus("new one"))
    b.grid(row=1)
    root.mainloop()
