from tkinter import *
from random import randint
t = Tk()

h = 600
w = 600
r = 40
barW = 30
barH = 100
barOffset = 30
barSpeed = 5
vectorX = 2
vectorY = 1
score = 0
isUp = False
isDown = False
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
    global bar
    global vectorX
    coords = c.coords(dot)
    if side == "up":
        return coords[1] <= 0
    if side == "down":
        return coords[3] >= h
    if side == "right":
        return coords[2] >= w
    if side == "left":
        return coords[0] <= 0
    if side == "bar":
        barCoords = c.coords(bar)
        return vectorX < 0 and coords[0] <= barCoords[2] and \
               coords[3] >= barCoords[1] and coords[1] <= barCoords[3]
            
def reflect(side):
    global vectorX
    global vectorY
    if side == "up" or side == "down":
        vectorY *= -1
    if side == "left" or side == "right" or side == "bar":
        vectorX *= -1

def up():
    coords = c.coords(bar)
    if coords[1] > 0:
        c.move(bar, 0, -barSpeed)

def down():
    coords = c.coords(bar)
    if coords[3] < h:
        c.move(bar, 0, barSpeed)

def callback(e):
    global isUp
    global isDown
    startIfNot()
    if e.keysym == "Up" and e.state == 262152:
        isUp = True
    if e.keysym == "Up" and e.state == 8:
        isUp = False
    if e.keysym == "Down" and e.state == 262152:
        isDown = True
    if e.keysym == "Down" and e.state == 8:
        isDown = False

def incrementScore():
    global text
    global score
    score += 1
    c.itemconfig(text, text="Score: %s" % score)

def endGame():
    global text
    global score
    c.itemconfig(text, text="Game Over!. Score: %s" % score)

def onTimer():
    global isUp
    global isDown
    if isUp:
        up()
    if isDown:
        down()
    c.move(dot, vectorX, vectorY)
    for side in ["up", "down", "right", "bar"]:
        if isCollide(side):
            reflect(side)
            if side == "bar":
                incrementScore()
    if isCollide("left"):
        endGame()
    else:
        t.after(10, onTimer)

t.bind("<KeyPress-Up>", callback)
t.bind("<KeyPress-Down>", callback)
t.bind("<KeyRelease-Up>", callback)
t.bind("<KeyRelease-Down>", callback)
t.mainloop()