from tkinter import *
from random import randint
t = Tk()

h = 600
w = 600
r = 40
barW = 30
barH = 100
barOffset = 30
barSpeed = 10
vectorX = 2
vectorY = 1
c = Canvas(t, width=w, height=h)
c.pack()

dot = c.create_oval((w-r)/2, (h-r)/2, (w+r)/2, (h+r)/2, fill="blue")
bar = c.create_rectangle(barOffset, (h-barH)/2, barOffset + barW, (h+barH) / 2, fill = "red")
text = c.create_text(w/2, h-20, text="Score: 0", font=('Times', 30))

isRunning = False
def startIfNot():
    global isRunning
    if not(isRunning):
        isRunning = True
        t.after(10, onTimer)

def isCollide(side):
    global dot
    coords = c.coords(dot)
    if side == "up":
        return coords[1] <= 0
    if side == "down":
        return coords[3] >= h
    if side == "right":
        return coords[2] >= w
    if side == "left":
        return coords[0] <= 0

def reflect(side):
    global vectorX
    global vectorY
    if side == "up" or side == "down":
        vectorY *= -1
    if side == "left" or side == "right":
        vectorX *= -1

def up(e):
    startIfNot()
    c.move(bar, 0, -barSpeed)

def down(e):
    startIfNot()
    c.move(bar, 0, barSpeed)

def onTimer():
    c.move(dot, vectorX, vectorY)
    for side in ["up", "down", "left", "right"]:
        if isCollide(side):
            reflect(side)
    t.after(10, onTimer)

t.bind("<Up>", up)
t.bind("<Down>", down)
t.mainloop()