import tkinter as tk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

root = tk.Tk()
root.title("Scroll Canvas")

frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

yscrollbar = tk.Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)

canvas = tk.Canvas(frame, bd=0, yscrollcommand=yscrollbar.set, height=200)
canvas.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

yscrollbar.config(command=canvas.yview)

for i in range(1000):
    tk.Button(canvas, text="Button "+str(i)).pack()

frame.pack()

a=canvas.bbox('all')
print("a is: ")
print(a)
"""
print(b)
print(c)
print(d)
"""
#canvas.config(scrollregion=canvas.bbox(tk.ALL))
canvas.config(scrollregion=(0,0,1,100000))
canvas.bind('<Configure>', lambda event, canvas=on_configure(canvas))


root.mainloop()
