from tkinter import *
from tkinter import messagebox
import webbrowser

root = Tk()
root.geometry("300x300")
root.config(bg="grey")
root.title("Shopping Portal")

def window2():
    root1 = Tk()
    root1.geometry("300x300")
    root1.config(bg="grey")
    root1.title("Shopping Portal")

    def flipkart():
        webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open("flipkart.com")
    def amazon():
        webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open("amazon.in")
    def snapdeal():
        webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open("snapdeal.com")

    titlee = Label(root1,text="Welcome to Shopping Portal",bg="grey")
    titlee.pack()
    info = Label(root1,text="Kindly Select any one of the sites to access the website",bg="grey")
    info.pack()

    b1 = Button(root1,text = "FLIPKART",bg = "grey",command = flipkart)
    b1.pack()
    b2 = Button(root1,text="AMAZON",bg="grey",command=amazon)
    b2.pack()
    b3 = Button(root1,text="SNAPDEAL",bg="grey",command = snapdeal)
    b3.pack()
    root1.mainloop()

bb1 = Button(root,text="Electronics",bg = "grey",command=window2)
bb1.pack()
root.mainloop()


