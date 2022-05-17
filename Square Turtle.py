import turtle
pen = turtle.Turtle()
c="orange"
side=260
pen.fillcolor(c)
pen.begin_fill()
for i in range(4):
    pen.forward(side)
    pen.right(-90)
pen.end_fill()

