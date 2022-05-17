from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("400x400")

v2 = IntVar()

def question2():
    if v1.get() == 3:
        messagebox.showinfo("CAPITAL QUIZ","YOUR ANSWER IS CORRECT. YOU MAY PROCEED")

        root2 = Tk()
        root2.geometry("400x400")

        q1=Label(root2,text="What is the capital of Taiwan ?")
        q1.pack()

        q2r1=Radiobutton(root2,text="Delhi",variable=v2,value=1,tristatevalue=0)
        q2r1.pack()

        q2r2=Radiobutton(root2,text="Taipei",variable=v2,value=2,tristatevalue=0)
        q2r2.pack()

        q2r3=Radiobutton(root2,text="Washington",variable=v2,value=3,tristatevalue=0)
        q2r3.pack()

        q2r4=Radiobutton(root2,text="Kabul",variable=v2,value=4,tristatevalue=0)
        q2r4.pack()


        q2b1=Button(root2,text="SUBMIT",command=question3)
        q2b1.pack()
        q2b2=Button(root2,text="QUIT",command=quit)
        q2b2.pack()
        
    else:
        messagebox.showerror("CAPITAL QUIZ","YOUR ANSWER IS WRONG")
        messagebox.showerror("CAPITAL QUIZ","SCORE: 0/5")
        root.destroy()
   

def question3():
    if v2.get() == 2:
        messagebox.showinfo("CAPITAL QUIZ","YOUR ANSWER IS CORRECT. YOU MAY PROCEED")

        root3 = Tk()
        root3.geometry("400x400")

        q3=Label(root3,text="What is the capital of Norway ?")
        q3.pack()

        v3=IntVar()
        q3r1=Radiobutton(root3,text="Kolkata",variable=v3,value=1,tristatevalue=0)
        q3r1.pack()

        q3r2=Radiobutton(root3,text="Ottawa",variable=v3,value=2,tristatevalue=0)
        q3r2.pack()

        q3r3=Radiobutton(root3,text="Karachi",variable=v3,value=3,tristatevalue=0)
        q3r3.pack()

        q3r4=Radiobutton(root3,text="Oslo",variable=v3,value=4,tristatevalue=0)
        q3r4.pack()

        q3b1=Button(root3,text="SUBMIT")
        q3b1.pack()
        q3b2=Button(root3,text="QUIT",command=quit)
        q3b2.pack()
    else:
        messagebox.showerror("CAPITAL QUIZ","YOUR ANSWER IS WRONG")
        messagebox.showerror("CAPITAL QUIZ","SCORE: 1/5")
        root.destroy()



q1=Label(root,text="What is the capital of Iran ?")
q1.pack()

v1=IntVar()
q1r1=Radiobutton(root,text="Canberra",variable=v1,value=1)
q1r1.pack()

q1r2=Radiobutton(root,text="Baghdad",variable=v1,value=2)
q1r2.pack()

q1r3=Radiobutton(root,text="Tehran",variable=v1,value=3)
q1r3.pack()

q1r4=Radiobutton(root,text="Istanbul",variable=v1,value=4)
q1r4.pack()

q1b1=Button(root,text="SUBMIT",command=question2)
q1b1.pack()
q1b2=Button(root,text="QUIT",command=quit)
q1b2.pack()

root.mainloop()