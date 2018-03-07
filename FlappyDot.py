from tkinter import *
from random import randint
t = Tk()

height = 400
width = 400
c = Canvas(t, width=width, height=height)
c.pack()

x = 50
y = 200
r = 40
minY = 0
maxY = 400-r
holeSize = 150
pipeWidth = 60

dot = c.create_oval(x, y, x+r, y+r, fill="blue")

def callback(e):
    if e.keysym == "Up" and c.coords(dot)[1] > minY:
        c.move(dot, 0, -10)
    elif e.keysym == "Down" and c.coords(dot)[1] < maxY:
        c.move(dot, 0, 10)

def isCollideObj(a, b):
    aPos = c.coords(a)
    bPos = c.coords(b)
    isCol = (isCollideOneAxis(aPos[0], aPos[2], bPos[0], bPos[2]) or \
           isCollideOneAxis(bPos[0], bPos[2], aPos[0], aPos[2])) and \
           (isCollideOneAxis(aPos[1], aPos[3], bPos[1], bPos[3]) or \
           isCollideOneAxis(bPos[1], bPos[3], aPos[1], aPos[3]))
    if isCol:
        c.itemconfig(b, fill="red")
    else:
        c.itemconfig(b, fill="green")

def isCollideOneAxis(ax1, ax2, bx1, bx2):
    return ax1 < bx2 and ax2 > bx2 or \
           ax2 > bx1 and ax1 < bx1

def createPipe():
    holeY = randint(0, height-holeSize)
    first = c.create_rectangle(width+10, 0, width+10+pipeWidth, holeY, fill="green")
    second = c.create_rectangle(width+10, holeY+holeSize, width+10+pipeWidth, height, fill="green")
    return (first, second)
pipes = []

def isCollide():
    global pipes
    global dot
    for p in pipes:
        for rect in p:
            if isCollideObj(dot, rect):
                return True
    return False

def movePipe(pipe):
    global pipes
    c.move(pipe[0], -10, 0)
    c.move(pipe[1], -10, 0)
    if (c.coords(pipe[0])[2] < 0):
        c.delete(pipe[0])
        c.delete(pipe[1])
        pipes.remove(pipe)

def createNew():
    pipes.append(createPipe())
counter = 20
def onTimer():
    global counter
    global pipes
    for i in pipes:
         movePipe(i)
    t.after(100, onTimer)
    counter += 1
    if (counter > 20):
        pipes.append(createPipe())
        counter = 0
    if isCollide():
        print("Collide")
    else:
        print("-")

t.bind("<Up>", callback)
t.bind("<Down>", callback)
t.after(100, onTimer)

t.mainloop()