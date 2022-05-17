from tkinter import *

root = Tk()
root.geometry("500x500")

c1 = Canvas(root,width=500, height=300)
c1.pack()

i1 = PhotoImage(file="dice 1.png")
c1.create_image(240,150, image=i1)

root.mainloop()