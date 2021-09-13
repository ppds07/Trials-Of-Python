from tkinter import *
from PIL import Image,ImageTk
#PIL  -> Python Imaging Library
import random

root = Tk()
root.geometry("300x300")

dice = ['dice 1.png','dice 2.png','dice 3.png','dice 4.png','dice 5.png','dice 6.jpg']
DI = ImageTk.PhotoImage(Image.open(random.choice(dice)))

image_label = Label(root,image=DI)
image_label.image = DI
image_label.pack()

def rolling():
    DI = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    image_label.config(image = DI)
    image_label.image = DI

b1 = Button(root,text="Roll",command=rolling)
b1.pack()

root.mainloop()