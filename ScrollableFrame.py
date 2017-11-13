import tkinter as tk

class ScrollableFrame(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(root, borderwidth=0)
        self.frame  = tk.Frame(self.canvas)
        self.scroll = tk.Scrollbar(root, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll.set)
        
        self.scroll.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw", tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event):
        print(self.canvas.bbox('all'))
        print(event)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class ScrollableGridFrame(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(self)
        self.frame  = tk.Frame(self.canvas)
        self.scroll = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll.set)
        
        self.scroll.grid(row=0, column=1, sticky='ns')
        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.canvas.create_window((0,0), window=self.frame, anchor="nw", tags="self.frame")
        #self.canvas.create_window((0,0), window=self, anchor="nw", tags="frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event):
        self.frame.update_idletasks() 
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def getframe(self):
        return self.frame

if __name__ == '__main__':
    root = tk.Tk()
    #myFrame = tk.Frame(root)
    #test = ScrollableFrame(root)
    test = ScrollableGridFrame(root)
    #test = test.getframe()
    #"""
    for i in range(100):
        tk.Button(test.frame, text="Label "+str(i)).grid(row=i)
    #"""

    test.grid() 
    #root.grid(row=0, column=1)
    tk.Label(root, text="hi",bd=1).grid(row=0, column=0)
    tk.Label(root, text="to").grid(row=1, column=0)
    tk.Label(root, text="you").grid(row=2, column=0)
    root.mainloop()
