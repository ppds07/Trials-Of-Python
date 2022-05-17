from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x300")


def calc():
    if name_e.get().isalpha() == True and maths_e.get().isdigit() == True and english_e.get().isdigit() == True and science_e.get().isdigit() == True and social_e.get().isdigit() ==True and comp_e.get().isdigit() == True:
        total = int(maths_e.get()) + int(english_e.get()) + int(science_e.get()) + int(social_e.get()) + int(comp_e.get())
        avg = (total/500)*100
        total_s = str(total)
        per_s = str(avg)
        root2 = Tk()

        h1 = Label(root2,text=name_e.get()+" Marksheet", font=("minecraft",15))
        h1.pack()

        tot = Label(root2,text="TOTAL: "+total_s+" of 500",font=("code bold",12))
        tot.pack()

        per = Label(root2,text="PERCENTAGE: "+per_s+" %",font=("code bold",12))
        per.pack()

        if avg > 50:
            passs = Label(root2,text="YOU HAVE PASSED THE EXAM",font=("code bold",12),fg="green")
            passs.pack()

        else:
            sad = Label(root2,text="YOU HAVE FAILED THE EXAM",font=("code bold",12),fg="red")
            sad.pack()
    else:
        messagebox.showerror("CALCUATOR","Kindly Enter the details properly.")
        
        


h1 = Label(root,text="PERCENTAGE CALCULATOR",font=("minecraft",20))
h1.pack()
null = Label(root,text="")
null.pack()

name = Label(root,text="Name:",font=("code bold",12))
name.place(x=20,y=60)
name_e = Entry(root,width=30)
name_e.place(x=120,y=60)

null = Label(root,text="")
null.pack()

h2 = Label(root,text="ENTER THE MARKS BELOW AS FOLLOWS",font=("minecraft",14))
h2.pack()

maths_l = Label(root,text="Maths:",font=("code bold",12))
maths_l.place(x=20,y=140)
maths_e = Entry(root,width=20)
maths_e.place(x=120,y=140)

english_l = Label(root,text="English:",font=("code bold",12))
english_l.place(x=20,y=170)
english_e = Entry(root,width=20)
english_e.place(x=120,y=170)

science_l = Label(root,text="Science:",font=("code bold",12))
science_l.place(x=20,y=200)
science_e = Entry(root,width=20)
science_e.place(x=120,y=200)

social_l = Label(root,text="Social:",font=("code bold",12))
social_l.place(x=20,y=230)
social_e = Entry(root,width=20)
social_e.place(x=120,y=230)

comp_l = Label(root,text="Computer:",font=("code bold",12))
comp_l.place(x=20,y=260)
comp_e = Entry(root,width=20)
comp_e.place(x=120,y=260)

b_submit = Button(root,text="Submit",font=("code bold",12),command=calc)
b_submit.place(x=360,y=150)

b_cancel = Button(root,text="Cancel",font=("code bold",12),command=quit)
b_cancel.place(x=360,y=220)



root.mainloop()