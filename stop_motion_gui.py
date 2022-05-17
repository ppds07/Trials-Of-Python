from tkinter import *
from PIL import Image,ImageTk
import random

root = Tk()
root.geometry("300x300")

pi = ['stop 1.png','stop 2.png','stop 3.png','stop 4.png','stop 5.png']
pics = ImageTk.PhotoImage(Image.open(random.choice(pi)))

image_label = Label(root,image=pics)
image_label.image = pics
image_label.pack()

def next():
    pics = ImageTk.PhotoImage(Image.open(random.choice(pi)))
    image_label.config(image=pics)
    image_label.image = pics

b1 = Button(root,text="Next",command=next)
b1.pack()

root.mainloop()