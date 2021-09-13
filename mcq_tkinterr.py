from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("700x700")


head_label=Label(root,text="QUIZ",font=("calibri",20,"bold"))
head_label.pack()


q1=Label(root,text="Q1.What is the capital of canada?" , font=("calibri",13,"bold"),fg="red")
q1.place(x=30,y=60)

v1=IntVar()
q1r1=Radiobutton(root,text="1.Delhi",variable=v1,value=1, font=("calibri",13,"bold"),fg="blue")
q1r1.place(x=40,y=90)

q1r2=Radiobutton(root,text="2.Ottawa",variable=v1,value=2, font=("calibri",13,"bold"),fg="blue")
q1r2.place(x=40,y=120)

q1r3=Radiobutton(root,text="3.Kolkata",variable=v1,value=3, font=("calibri",13,"bold"),fg="blue")
q1r3.place(x=40,y=150)

q1r4=Radiobutton(root,text="4.London",variable=v1,value=4, font=("calibri",13,"bold"),fg="blue")
q1r4.place(x=40,y=180)


def question1():
    if v1.get() == 2:
        messagebox.showinfo("CORRECT","Your answer is correct")
    else:
        messagebox.showerror("WRONG","Your answer is wrong")

q1b1=Button(root,text="SUBMIT ANSWER",font=("calibri",12,"bold"),fg="purple",command=question1)
q1b1.place(x=60,y=220)

# QUESTION 2

q2=Label(root,text="Q2.What is the largest country in the world?" , font=("calibri",13,"bold"),fg="red")
q2.place(x=30,y=270)

v2=IntVar()
q2r1=Radiobutton(root,text="1.America",variable=v2,value=1, font=("calibri",13,"bold"),fg="blue")
q2r1.place(x=40,y=300)

q2r2=Radiobutton(root,text="2.France",variable=v2,value=2, font=("calibri",13,"bold"),fg="blue")
q2r2.place(x=40,y=330)

q2r3=Radiobutton(root,text="3.Canada",variable=v2,value=3, font=("calibri",13,"bold"),fg="blue")
q2r3.place(x=40,y=360)

q2r4=Radiobutton(root,text="4.Russia",variable=v2,value=4, font=("calibri",13,"bold"),fg="blue")
q2r4.place(x=40,y= 390)

def question2():
    if v2.get() == 4:
        messagebox.showinfo("CORRECT","Your answer is correct")
    else:
        messagebox.showerror("WRONG","Your answer is wrong")
q2b1=Button(root,text="SUBMIT ANSWER",font=("calibri",12,"bold"),fg="purple",command=question2)
q2b1.place(x=60,y=430)


def result():
    score=0
    if v1.get() == 2 and v2.get() == 4:
        score+=2
    elif v1.get() == 2:
        score+=1
    elif v2.get() == 4:
        score+=1
    elif v1.get() != 2 and v2.get() != 4:
        score-=2
    resultlabel=Label(root,font=("calibri",30,"bold"),fg="purple")
    resultlabel.config(text=score)
    resultlabel.pack(side=BOTTOM)

resultb=Button(root,text="SHOW RESULT",font=("calibri",12,"bold"),fg="green",command=result)
resultb.place(x=60,y=500)


root.mainloop()