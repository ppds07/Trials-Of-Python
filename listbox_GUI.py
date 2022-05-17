from tkinter import *
root = Tk()
root.geometry("500x500")

name_label = Label(root,text="SUBJECTS",font=("arial",20,"bold"),bg="white",fg="red")
name_label.pack()

l1 = Listbox(root)
l1.insert(1,"English")
l1.insert(2,"Maths")
l1.insert(3,"Hindi")
l1.insert(4,"Tamil")
l1.insert(5,"History")
l1.place(x=180,y=60)

b1 = Button(root,text="OK",font=("arial",18))
b1.place(x=100,y=260)

b2 = Button(root,text="CANCEL",font=("arial",18))
b2.place(x=230,y=260)

root.mainloop()