""" 
Create a status bar to go on the bottom of the screen
"""

import tkinter as tk

class Status(tk.Frame):
    
    """ Create a scroll bar """
    def __init__(self):
        tk.Frame.__init__(self)
        #self.status = tk.StringVar()
        #tk.Label(self, text=self.status).pack()
        self.status = tk.Label(self)
        self.status.grid()

    def createsttatusbar(self):
        """ display the status """
        #self.status = tk.Label(self, text="This is the status bar").pack()
        #self.status.set('This status will be show on the status bar')
        self.status.config(text="Welcome to the status bar")
        return self

    def updatestatus(self, msg):
        """ update the status message """
        self.status.config(text=msg)

if __name__ == '__main__':
    root = tk.Tk()
    frame = Status(root)
    frame.grid()
    tk.Label(frame, text="Let's see if this works").grid()
    frame.createsttatusbar()
    frame.updatestatus("A change in status going on here")
    root.mainloop()
