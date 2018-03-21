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
text = c.create_text(width/2, height-20, text="Score: 0", font=('Times', 30))
dotSpeed = 1
gravity = 0.05

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
    return isCol

def isCollideOneAxis(ax1, ax2, bx1, bx2):
    return ax1 < bx2 and ax2 > bx2 or \
           ax2 > bx1 and ax1 < bx1

def createPipe():
    global text
    holeY = randint(0, height-holeSize)
    first = c.create_rectangle(width+10, 0, width+10+pipeWidth, holeY, fill="green")
    second = c.create_rectangle(width+10, holeY+holeSize, width+10+pipeWidth, height, fill="green")
    c.tag_raise(text)
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
def isOut():
    global dot
    global c
    pos = c.coords(dot)
    return pos[1] < 0 or pos[3] > height

didScore = False
speed = 1
def movePipe(pipe):
    global didScore
    global pipes
    global speed
    c.move(pipe[0], -speed, 0)
    c.move(pipe[1], -speed, 0)
    speed += speed * 0.0002
    if (c.coords(pipe[0])[2] < 0):
        c.delete(pipe[0])
        c.delete(pipe[1])
        pipes.remove(pipe)
        didScore = False

score = 0
def incrementScore():
    global didScore
    global score
    global c
    global text
    if not(didScore):
        didScore = True    
        score=score+1
        c.itemconfig(text, text="Score: %s" % score)

def isNewScore():
    global pipes
    global dot
    global c
    dotPos = c.coords(dot)
    for pipe in pipes:
        pos = c.coords(pipe[0])
        if pos[2] < dotPos[0]:
            incrementScore()

def createNew():
    pipes.append(createPipe())
isRunning = False
def callback(e):
    global isRunning
    global dotSpeed
    if not(isRunning):
        pipes.append(createPipe())
        t.after(10, onTimer)
        isRunning = True
    dotSpeed = -2
def onTimer():
    global pipes
    global dotSpeed
    global gravity
    for i in pipes:
        movePipe(i)
    isNewScore()
    c.move(dot, 0, dotSpeed)
    dotSpeed += gravity
    if isCollide() or isOut():
        print("Collide")
    else:
        t.after(10, onTimer)
    if width - c.coords(pipes[-1][0])[0] > 200:
        pipes.append(createPipe())
    

t.bind("<space>", callback)
t.mainloop()