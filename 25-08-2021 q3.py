from tkinter import *
from PIL import Image,ImageTk
import random

root = Tk()
root.geometry("300x300")

dice_img = ['dice 1.png','dice 2.png','dice 3.png','dice 4.png','dice 5.png','dice 6.jpg']
DI = ImageTk.PhotoImage(Image.open(random.choice(dice_img)))

image_label = Label(root,image=DI)
image_label.image = DI
image_label.pack()

def rolling():
    DI = ImageTk.PhotoImage(Image.open(random.choice(dice_img)))
    image_label.config(image = DI)
    image_label.image = DI

roll = Button(root,text="Roll",command=rolling)
roll.pack()

root.mainloop()