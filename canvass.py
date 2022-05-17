from tkinter import *

root = Tk()

c = Canvas(root,height=100,width=200)
c.pack()

c.create_rectangle(50,20,150,80)
c.create_rectangle(65,35,130,60)
c.create_line(0,0,50,20)
c.create_line(0,100,50,80)
c.create_line(150,20,200,0)
c.create_line(150,80,200,100)

root.mainloop()