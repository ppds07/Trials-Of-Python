from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")

messagebox.showinfo("Correct","Done")
messagebox.showwarning("Warning","You are under Arrest")
messagebox.showerror("Error","Try Again")
messagebox.askokcancel("Cancel","Want to Leave?")
messagebox.askyesno("Sure","Yes or No")
messagebox.askretrycancel("Try Again","Please Wait for this window to close")

root.mainloop()