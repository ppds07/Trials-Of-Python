from tkinter import *
root = Tk()
root.geometry("300x300")

s1 = Scrollbar(root)
s1.pack(side=RIGHT,fill=Y)

l1 = Listbox(root,yscrollcommand=s1.set)

for i in range(30):
    l1.insert(END,"NUM: "+str(i))

l1.pack()

root.mainloop()