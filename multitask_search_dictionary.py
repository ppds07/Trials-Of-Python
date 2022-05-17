from tkinter import *
import webbrowser
from PyDictionary import PyDictionary

root = Tk()
root.geometry("300x300")
root.config(bg="white")

def check():
    if e_se.get() == "search" or e_se.get() =="search engine" or e_se.get() == "searchbox" or e_se.get() ==  "SEARCHBOX" or e_se.get() ==  "SEARCH ENGINE" or e_se.get() ==  "SEARCH":
        def search():
            v1 = e1.get()
            webbrowser.open(v1)

        l1 = Label(root,text="R3DLX SEARCH",font=("algerian",18))
        l1.pack(side=TOP)

        l2 = Label(root,text="Enter: ",font=("calibri",15))
        l2.place(x=20,y=60)

        e1 = Entry(root,width=24)
        e1.place(x=100,y=65)

        b1 = Button(root,text="SEARCH",command=search)
        b1.place(x=80,y=120)

        b2 = Button(root,text="QUIT",command=quit)
        b2.place(x=160,y=120)
        



l_se = Label(root,text="Search: ")
l_se.place(x=40,y=90)
e_se = Entry(root,width=20)
e_se.place(x=120,y=90)
b_se = Button(root,text="Search")
b_se.place(x=130,y=130)



root.mainloop()



