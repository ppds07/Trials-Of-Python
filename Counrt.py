from tkinter import *
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("300x300")
root.config(bg="white")

def tts():
    msg = var1.get()
    speech = gTTS(text=msg)
    speech.save("demo2.mp3")
    playsound("demo2.mp3")

def reset():
    var1.set("")

label = Label(root,text="Text To Speech",font=("Algerian",20,"bold"),bg="white",fg="red")
label.pack()

l1 = Label(root,text="Enter the text: ",font=("arial",14),bg="white",fg="blue")
l1.place(x=30,y=50)

var1=StringVar()
l1_entry = Entry(root,width=20,textvariable=var1)
l1_entry.place(x=150,y=55)

b1 = Button(root,text="Play",fg="green",bg="white",font=("Arial",13),command=tts)
b1.place(x=120,y=90)

b2 = Button(root,text="Reset",bg="white",fg="red",font=("arial",13),command=reset)
b2.place(x=120,y=135)

b3 = Button(root,text="Exit",bg="white",fg="red",font=("arial",13),command=quit)
b3.place(x=120,y=175)
root.mainloop()