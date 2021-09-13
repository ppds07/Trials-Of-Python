from tkinter import *
from tkinter import messagebox
from datetime import date

root = Tk()
root.geometry("400x400")
root.config(bg="black")


heading_label = Label(root,text=" AGE CALCULATOR ",bg="orange",fg="black",font=("minecraft",15))
heading_label.pack()

name_label = Label(root,text="NAME:",bg="black",fg="orange",font=("minecraft",13))
name_label.place(x=30,y=50)
nam = StringVar()
name_entry = Entry(root,width=30,textvariable=nam)
name_entry.place(x=120,y=55)

year_label = Label(root,text="YEAR:",bg="black",fg="orange",font=("minecraft",13))
year_label.place(x=30,y=80)
yr = StringVar()
year_entry = Entry(root,width=30,textvariable=yr)
year_entry.place(x=120,y=85)


m_label = Label(root,text="MONTH:",bg="black",fg="orange",font=("minecraft",13))
m_label.place(x=30,y=110)
m_entry = Entry(root,width=30)
m_entry.place(x=120,y=115)

day_label = Label(root,text="DAY:",bg="black",fg="orange",font=("minecraft",13))
day_label.place(x=30,y=140)
day_entry = Entry(root,width=30)
day_entry.place(x=120,y=145)

cal_button = Button(root,text="Calculate Age",bg="dark green",fg="light green",font=("minecraft",14))
cal_button.place(x=130,y=190)

root.mainloop()