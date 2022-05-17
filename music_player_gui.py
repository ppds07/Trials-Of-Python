import os
from tkinter import *
import pygame
from tkinter.filedialog import askdirectory

root = Tk()
root.geometry("400x400")
root.config(bg="grey")

dire = askdirectory() # curent directory
os.chdir(dire) # to change the directory
song_list = os.listdir() # to list song 

play_list = Listbox(root,selectmode=SINGLE)

for i in song_list:
    count = 0
    play_list.insert(count,i)
    count = count + 1

pygame.init()
pygame.mixer.init()

var = StringVar()
song_title = Label(root,textvariable=var)
song_title.pack()

def play():
    pygame.mixer.music.load(play_list.get(ACTIVE))
    var.set(play_list.get(ACTIVE))
    pygame.mixer.music.play()

b1 = Button(root,text="PLAY",command=play)
b1.pack()

def pause():
    pygame.mixer.music.pause()

b2 = Button(root,text="PAUSE",command=pause)
b2.pack()

def unpause():
    pygame.mixer.music.unpause()
b3 = Button(root,text="UNPAUSE",command=unpause)
b3.pack()

def stop():
    pygame.mixer.music.stop()

b4 = Button(root,text="STOP",command=stop)
b4.pack()

play_list.pack()


root.mainloop()