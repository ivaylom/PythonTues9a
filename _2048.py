"""from tkinter import *
t = Tk()

def callback(e):
    print(e)

t.bind("<Up>", callback)
t.mainloop()
"""

import _2048engine

engine = _2048engine._2048()
engine.addItem()
engine.addItem()
engine.addItem()
engine.addItem()
print(engine.board)

engine.move("right")
print(engine.board)