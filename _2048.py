import _2048engine

from tkinter import *
t = Tk()

def callback(e):
    if e.keysym == 'Up':
        print(e)
    elif e.keysym == 'Down':
        print(e)

t.bind("<Up>", callback)

c = Canvas(t, width=400, height=400)
c.pack()

c.create_rectangle(0,0,40,40, fill="red", outline="red")
c.create_text(20,20, text="2048")

t.mainloop()

engine = _2048engine._2048()
engine.addItem()
engine.printBoard()