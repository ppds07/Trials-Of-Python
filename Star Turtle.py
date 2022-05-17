import turtle
pen = turtle.Turtle()
c="gold"
side=90
pen.color("gold")
pen.fillcolor(c)
pen.begin_fill()
for i in range(5):
    pen.forward(side)
    pen.right(144)
pen.end_fill()

