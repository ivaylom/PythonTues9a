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
print(engine.board)
for i in range(100):
    engine.move("right")
    engine.move("down")
    engine.move("up")
    engine.move("left")
print(engine.board)