from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("700x700")


head_label=Label(root,text="QUIZ",font=("code bold",20,"bold"))
head_label.pack()


q1=Label(root,text="Q1.Who is Mrwhosetheboss?" , font=("code bold",13,"bold"),fg="red")
q1.place(x=30,y=60)

v1=IntVar()
q1r1=Radiobutton(root,text="1.Arun Maini",variable=v1,value=1, font=("minecraft",12,"bold"),fg="blue")
q1r1.place(x=40,y=90)

q1r2=Radiobutton(root,text="2.Marques Brownlee",variable=v1,value=2, font=("minecraft",12,"bold"),fg="blue")
q1r2.place(x=40,y=120)

q1r3=Radiobutton(root,text="3.Priyadharshan",variable=v1,value=3, font=("minecraft",12,"bold"),fg="blue")
q1r3.place(x=40,y=150)

q1r4=Radiobutton(root,text="4.Gaurav Sharma",variable=v1,value=4, font=("minecraft",12,"bold"),fg="blue")
q1r4.place(x=40,y=180)


def question1():
    if v1.get() == 1:
        messagebox.showinfo("CORRECT","Your answer is correct")
    else:
        messagebox.showerror("WRONG","Your answer is wrong")


q1b1=Button(root,text="SUBMIT ANSWER",font=("calibri",12,"bold"),fg="purple",command=question1)
q1b1.place(x=60,y=210)


q2=Label(root,text="Q2.Who Owns Paypal?" , font=("code bold",13,"bold"),fg="red")
q2.place(x=30,y=280)

v2=IntVar()
q2r1=Radiobutton(root,text="1.Satyna Nadella",variable=v2,value=1, font=("minecraft",12,"bold"),fg="blue")
q2r1.place(x=40,y=310)

q2r2=Radiobutton(root,text="2.YUP, It's Me",variable=v2,value=2, font=("minecraft",12,"bold"),fg="blue")
q2r2.place(x=40,y=340)

q2r3=Radiobutton(root,text="3.Elon Musk",variable=v2,value=3, font=("minecraft",12,"bold"),fg="blue")
q2r3.place(x=40,y=370)

q2r4=Radiobutton(root,text="4.Jeff Bezoz",variable=v2,value=4, font=("minecraft",12,"bold"),fg="blue")
q2r4.place(x=40,y=400)


def question2():
    if v2.get() == 3:
        messagebox.showinfo("CORRECT","Your answer is correct my boi")
    else:
        messagebox.showerror("WRONG","Your answer is wrong. Try again homie")

q2b1=Button(root,text="SUBMIT ANSWER",font=("calibri",12,"bold"),fg="purple",command=question1)
q2b1.place(x=60,y=440)

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
    resultlabel=Label(root,font=("code bold",30,"bold"),fg="purple")
    resultlabel.config(text=score)
    resultlabel.pack(side=BOTTOM)


resultb=Button(root,text="SHOW RESULT",font=("code bold",12,"bold"),fg="green",command=result)
resultb.place(x=60,y=500)


root.mainloop()