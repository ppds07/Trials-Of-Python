from tkinter.ttk import *
from tkinter import *

root = Tk()
root.geometry("400x400")

#COMBOBOX WIDGET

c1 = Combobox(root)
c1['values'] = ("PPDS","Ashwini","Harshita","Aadvik")
c1.grid(row = 0, column = 1)


root.mainloop()