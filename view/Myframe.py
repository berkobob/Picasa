""" My own frame that's scrollable. Add child widgets to self.frame """

import tkinter as tk

class MyFrame(tk.Frame):
    """ Scrollable grid frame """
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self)
        self.frame = tk.Frame(self.canvas)
        self.scroll = tk.Scrollbar(self, orient='vertical',
                                   command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll.set)

        self.scroll.grid(row=0, column=1, sticky='ns')
        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.canvas.create_window((0, 0), window=self.frame,
                                  anchor='nw', tags='self')
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def onFrameConfigure(self, event):
        """ resize scrollable area """
        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def get(self):
        """ return frame so that child can add widgets """
        return self.frame

if __name__ == '__main__':
    root = tk.Tk()
    test = MyFrame(root)
    for i in range(100):
        tk.Button(test.frame, text='Button'+str(i), relief='flat').grid(row=i)
    test.grid()
    root.mainloop()
