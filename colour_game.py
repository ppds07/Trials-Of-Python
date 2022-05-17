import random
from tkinter import *

root = Tk()
root.geometry("250x250")

color = ["red","blue","orange","purple","white"]

result = random.choice(color)

fg_color = random.choice(color)

def changecolour():
    result = random.choice(color)
    fg_color = random.choice(color)
    l1 = Label(root,fg=fg_color,font=("minecraft",15))
    l1.config(text=result)
    l1.place(x=50,y=50)

b1 = Button(root,text="HIT", command=changecolour)
b1.pack()

root.mainloop()