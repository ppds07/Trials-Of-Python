import turtle
pen = turtle.Turtle()
c="red"
side=180
pen.fillcolor(c)
pen.begin_fill()
for i in range(6):
    pen.forward(side)
    pen.right(-60)
pen.end_fill()

