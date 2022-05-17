from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("700x700")

def submit():
    if v1.get()==1:
        h1 = Label(root,text="India")
        h1.place(x=50,y=230)
    if v1.get()==2:
        h2 = Label(root,text="USA")
        h2.place(x=50,y=230)
    if v1.get()==3:
        h3 = Label(root,text="Japan")
        h3.place(x=50,y=230)
    if v1.get()==4:
        h4 = Label(root,text="UK  ")
        h4.place(x=50,y=230)


v1=IntVar()
q1r1=Radiobutton(root,text="1.India",variable=v1,value=1, font=("minecraft",12,"bold"))
q1r1.place(x=40,y=90)

q1r2=Radiobutton(root,text="2.USA",variable=v1,value=2, font=("minecraft",12,"bold"))
q1r2.place(x=40,y=120)

q1r3=Radiobutton(root,text="3.Japan",variable=v1,value=3, font=("minecraft",12,"bold"))
q1r3.place(x=40,y=150)

q1r4=Radiobutton(root,text="4.UK",variable=v1,value=4, font=("minecraft",12,"bold"))
q1r4.place(x=40,y=180)

b1 = Button(root,text="SUBMIT",command=submit)
b1.place(x=160,y=90)




root.mainloop()
