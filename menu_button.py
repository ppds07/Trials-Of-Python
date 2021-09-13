from tkinter import *

root = Tk()
root.geometry("400x400")
root.config(bg="grey")

l1 = Label(root,text="Dishes You May Like",bg="grey",fg="white",font=("code bold",18))
l1.pack()
l2 = Label(root,text="Click the Menu to check!!")
l1.pack()

m1 = Menubutton(root,text="Menu",bg="grey")

m1.menu = Menu(m1)
m1["menu"]=m1.menu


m1.menu.add_radiobutton(label = "Idly")
m1.menu.add_radiobutton(label = "Dosa")
m1.menu.add_radiobutton(label = "Aloo Paratha")
m1.menu.add_radiobutton(label = "Pav Bhaji")
m1.menu.add_radiobutton(label = "Dal Roti")
m1.menu.add_radiobutton(label = "Rotla")
m1.menu.add_radiobutton(label = "Khaman Dhokla")
m1.pack()

root.mainloop()