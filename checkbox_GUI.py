from tkinter import *
root = Tk()
root.geometry("500x500")

name_label = Label(root,text="Select Your Version",fon=("arial",15,"bold"))
name_label.pack()

c1 = Checkbutton(root,text="Minecraft Bedrock Edition")
c1.place(x=60,y=60)
c2 = Checkbutton(root,text="Minecraft Caves & Cliffs Edition")
c2.place(x=60,y=100)
c3 = Checkbutton(root,text="Minecraft Java Edition")
c3.place(x=60,y=140)
c4 = Checkbutton(root,text="Minecraft Hardcore Edition")
c4.place(x=60,y=180)

root.mainloop()