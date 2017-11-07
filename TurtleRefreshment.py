import turtle
t = turtle.Pen()

t.speed(0)

a = 20
size = 1
for _ in range(50):
    t.fd(a)
    t.rt(144)
    size *= 1.05
    t.pensize(size)
    a *= 1.07
