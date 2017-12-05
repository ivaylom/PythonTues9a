"""from tkinter import *
t = Tk()

def callback(e):
    print(e)

t.bind("<Up>", callback)
t.mainloop()
5"""

import _2048engine

engine = _2048engine._2048()
engine.addItem()
engine.printBoard()