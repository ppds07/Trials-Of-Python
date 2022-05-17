import turtle

pen = turtle.Turtle()

c="brown"

side=260


pen.fillcolor(c)

pen.begin_fill()

for i in range(3):
    pen.backward(side)
    pen.right(-120)
pen.backward(side)
for i in range(3):
    pen.forward(side)
    pen.right(-120)

    
pen.end_fill()

