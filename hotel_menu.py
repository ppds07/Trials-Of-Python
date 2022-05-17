from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")

h1 = Label(root,text="WELCOME TO CY HOTEL",fg="red",font=("minecraft",15))
h1.pack()

mb=  Menubutton ( root, text="Drinks" )
mb.pack()
mb.menu =  Menu ( mb )
mb["menu"] =  mb.menu

ajvar = IntVar()
lnvar = IntVar()
ojvar = IntVar()
cdvar = IntVar()

mb.menu.add_checkbutton ( label="Apple Juice",
                          variable=ajvar )
mb.menu.add_checkbutton ( label="Lemonade",
                          variable=lnvar )
mb.menu.add_checkbutton ( label="Orange Juice",
                          variable=ojvar )
mb.menu.add_checkbutton ( label="Cool Drinks",
                          variable=cdvar )

si=  Menubutton ( root, text="South Indian" )
si.pack()
si.menu =  Menu ( si )
si["menu"] =  si.menu

idvar = IntVar()
dsvar = IntVar()
upvar = IntVar()
vavar = IntVar()

si.menu.add_checkbutton ( label="Idly",
                          variable=idvar )
si.menu.add_checkbutton ( label="Dosa",
                          variable=dsvar )
si.menu.add_checkbutton ( label="Upma",
                          variable=upvar )
si.menu.add_checkbutton ( label="Vada",
                          variable=vavar )
si.place(x=30,y=50)

root.mainloop()