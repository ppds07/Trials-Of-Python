from tkinter import *

root = Tk()
root.geometry("400x400")

t1 = Text(root)
t1.insert(INSERT,"WRITE YOUR NAME HERE \n")
t1.insert(END,"OK BYE, HAVE A GREAT TIME")
t1.pack()

t1.tag_add("HERE","0.5","1.20")
t1.tag_add("START","1.8","1.10")

t1.tag_config("HERE",background="white",foreground="red")
t1.tag_config("START",background="white",foreground="red")

root.mainloop()
