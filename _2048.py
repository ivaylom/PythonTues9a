import _2048engine

from tkinter import *
t = Tk()

c = Canvas(t, width=400, height=400)
c.pack()

boardR = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
boardT = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(4):
    for j in range(4):
        boardR[i][j] = c.create_rectangle(j*100,i*100,j*100+90, i*100+90, fill="#FFFFFF", outline="black", outlineoffset='-1,-1,-1,-1')
        boardT[i][j] = c.create_text(j*100+45,i*100+45, text="", font=("Purisa", 24))

engine = _2048engine._2048()
engine.addItem()

def refreshBoard():
    global engine
    global boardR
    global boardT
    global c
    for i in range(4):
        for j in range(4):
            if engine.board[i][j] == 0:
                c.itemconfig(boardT[i][j], text = "")
            else:
                c.itemconfig(boardT[i][j], text = engine.board[i][j])
            red = engine.board[i][j] / 256
            if red > 1: red = 1
            red = int(255-(red*255))
            c.itemconfig(boardR[i][j], fill="#FF%0.2X%0.2X" % (red, red))
            

def callback(e):
    global engine
    engine.move(e.keysym)
    refreshBoard()


t.bind("<Up>", callback)
t.bind("<Down>", callback)
t.bind("<Right>", callback)
t.bind("<Left>", callback)

t.mainloop()