import tkinter as tk

class ScrollableGridFrame(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(root, borderwidth=0)
        self.frame  = tk.Frame(self.canvas)
        self.scroll = tk.Scrollbar(root, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll.set)
        
        self.scroll.grid(row=0, column=1)
        self.canvas.grid(row=0, column=0)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw", tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

    def populate(self):
        '''Put in some fake data'''
        for row in range(100):
            tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1", 
                     relief="solid").grid(row=row, column=0)
            t="this is the second column for row %s" %row
            tk.Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self, event):
        print(self.canvas.bbox('all'))
        print(event)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == '__main__':
    root = tk.Tk()
    #test = ScrollableFrame(root)
    test = ScrollableGridFrame(root)
    #"""
    for i in range(100):
        tk.Button(test.frame, text="Label "+str(i)).pack()
    #"""

    #test1.populate() 
    test.grid()
    root.mainloop()
