from tkinter import *
from tkinter import messagebox
root=Tk()

root.geometry("300x300")
root.config(bg="white")

pas=StringVar()
nam=StringVar()
def color_game():
    def check():
        if e == "red":
            messagebox.showinfo("Information","Correct")
        else:
            messagebox.showwarning("Information","Wrong")

    root1=Tk()
    root1.geometry("300x300")

    color_label = Label(root1, text="Green",font=("arial",15),fg="red")
    color_label.pack()

    e=StringVar()
    color_entry = Entry(root1, width=25,textvariable=e)
    color_entry.place(x=110,y=80)

b_cg = Button(root,text="Colour Game",command=color_game)
b_cg.place(x=120,y=80)

root.mainloop()