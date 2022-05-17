from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("600x600")

l1 = Listbox(root)
l1.place(x=200,y=150)

sl = [["1000","PPDS"],["1001","Vivek"],["1002","Swaroop"]]

def select_list():
    sl.sort()
    l1.delete(0,END)
    for id,name in sl:
        l1.insert(END,name)
select_list()

def add():
   if id_entry.get().isdigit() and name_entry.get().isalpha():
       sl.append([id_entry.get(),name_entry.get()])
       select_list()
   else:
       messagebox.showerror("WRONG","TRY AGAIN")

def view():


id_label = Label(root,text="Student ID:")
id_label.place(x=20,y=30)
id_entry = StringVar()
id_box = Entry(root,width=20,textvariable=id_entry)
id_box.place(x=130,y=35)
name_label = Label(root,text="Student Name")
name_label.place(x=20,y=60)
name_entry = StringVar()
name_box = Entry(root,width=20,textvariable=name_entry)
name_box.place(x=130,y=65)

b1 = Button(root,text="Add",command=add)
b1.place(x=50,y=100)
b2 = Button(root,text="View")
b2.place(x=50,y=130)
b3 = Button(root,text="Delete")
b3.place(x=50,y=160)




root.mainloop()
