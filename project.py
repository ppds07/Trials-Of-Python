from tkinter import *
from tkinter import messagebox
import webbrowser

root = Tk()
root.geometry("500x500")
root.config(bg="grey")

def food():
    su1 = Tk()
    su1.geometry("500x500")
    su1.config(bg="grey")

    h1 = Label(su1,text="WELCOME TO FOOD PORTAL",bg="grey",fg="sky blue",font=("minecraft",23))
    h1.pack()

    h3 = Label(su1,text="",bg="grey")
    h3.pack()

    h2 = Label(su1,text="SELECT THE WEBSITE TO ORDER FOOD",fg="white",bg="grey",font=("code bold",15))
    h2.pack()

    bf1 = Button(su1,text="ZOMATO",fg="red",bg="grey",font=("code bold",15),command=zomato)
    bf1.place(x=70,y=180)

    bf2 = Button(su1,text="SWIGGY",fg="blue",bg="grey",font=("code bold",15),command=swiggy)
    bf2.place(x=70,y=260)

    bf3 = Button(su1,text="UBER EATS",fg="purple",bg="grey",font=("code bold",15),command=ubereats)
    bf3.place(x=280,y=180)
    
    bf4 = Button(su1,text="UBER EATS",fg="orange",bg="grey",font=("code bold",15),command=ubereats)
    bf4.place(x=280,y=180)
 


def electronics():
    su2 = Tk()
    su2.geometry("500x500")
    su2.config(bg="grey")

    h1 = Label(su2,text="WELCOME TO ELECTRONIC PORTAL",bg="grey",fg="sky blue",font=("minecraft",23))
    h1.pack()

    h3 = Label(su2,text="",bg="grey")
    h3.pack()

    h2 = Label(su2,text="SELECT THE WEBSITE TO ORDER",fg="white",bg="grey",font=("code bold",15))
    h2.pack()

    bf1 = Button(su2,text="FLIPKART",fg="red",bg="grey",font=("code bold",15),command=flipkart)
    bf1.place(x=70,y=180)

    bf2 = Button(su2,text="AMAZON",fg="blue",bg="grey",font=("code bold",15),command=amazon)
    bf2.place(x=70,y=260)

    bf3 = Button(su2,text="SNAPDEAL",fg="purple",bg="grey",font=("code bold",15),command=snapdeal)
    bf3.place(x=280,y=180)
    
    bf4 = Button(su2,text="EBAY",fg="orange",bg="grey",font=("code bold",15),command=ebay)
    bf4.place(x=280,y=260)

def sh():
    su3 = Tk()
    su3.geometry("500x500")
    su3.config(bg="grey")

    h1 = Label(su3,text="WELCOME TO SECOND HAND PORTAL",bg="grey",fg="sky blue",font=("minecraft",23))
    h1.pack()

    h3 = Label(su3,text="",bg="grey")
    h3.pack()

    h2 = Label(su3,text="SELECT THE WEBSITE TO ORDER",fg="white",bg="grey",font=("code bold",15))
    h2.pack()

    bf1 = Button(su3,text="OLX",fg="red",bg="grey",font=("code bold",15),command=olx)
    bf1.place(x=70,y=180)

    bf2 = Button(su3,text="QUICKR",fg="blue",bg="grey",font=("code bold",15),command=quickr)
    bf2.place(x=70,y=260)

    bf3 = Button(su3,text="2GUD",fg="purple",bg="grey",font=("code bold",15),command=gud)
    bf3.place(x=280,y=180)
    
    bf4 = Button(su3,text="AMAZON",fg="orange",bg="grey",font=("code bold",15),command=amzon)
    bf4.place(x=280,y=260)

def fur():
    su4 = Tk()
    su4.geometry("500x500")
    su4.config(bg="grey")

    h1 = Label(su4,text="WELCOME TO FURNITURE PORTAL",bg="grey",fg="sky blue",font=("minecraft",23))
    h1.pack()

    h3 = Label(su4,text="",bg="grey")
    h3.pack()

    h2 = Label(su4,text="SELECT THE WEBSITE TO ORDER",fg="white",bg="grey",font=("code bold",15))
    h2.pack()

    bf1 = Button(su4,text="AMAZON",fg="red",bg="grey",font=("code bold",15),command=amazon)
    bf1.place(x=70,y=180)

    bf2 = Button(su4,text="EVOK",fg="blue",bg="grey",font=("code bold",15),command=evok)
    bf2.place(x=70,y=260)

    bf3 = Button(su4,text="URBAN L",fg="purple",bg="grey",font=("code bold",15),command=ul)
    bf3.place(x=280,y=180)
    
    bf4 = Button(su4,text="PEPPERFRY",fg="orange",bg="grey",font=("code bold",15),command=pf)
    bf4.place(x=280,y=260)

h1 = Label(root,text="WELCOME TO EASE PORTAL",bg="grey",fg="sky blue",font=("minecraft",23))
h1.pack()

h3 = Label(root,text="",bg="grey")
h3.pack()

h2 = Label(root,text="Which Category do you want to surf?",fg="white",bg="grey",font=("code bold",15))
h2.pack()

b1 = Button(root,text="  FOOD  ",fg="red",bg="grey",font=("code bold",15),command=food)
b1.place(x=70,y=180)

b2 = Button(root,text="FURNITURE",fg="blue",bg="grey",font=("code bold",15),command=fur)
b2.place(x=70,y=260)

b3 = Button(root,text="SECOND HAND",fg="purple",bg="grey",font=("code bold",15),command=sh)
b3.place(x=280,y=180)

b4 = Button(root,text="ELECTRONICS",fg="orange",bg="grey",font=("code bold",15),command=electronics)
b4.place(x=280,y=260)

def zomato():
    webbrowser.open("www.zomato.com")

def swiggy():
    webbrowser.open("www.swiggy.com")

def ubereats():
    webbrowser.open("www.ubereats.com")

def flipkart():
    webbrowser.open("www.flipkart.com")

def amazon():
    webbrowser.open("www.amazon.in")

def snapdeal():
    webbrowser.open("www.snapdeal.com")

def ebay():
    webbrowser.open("www.ebay.in")

def quickr():
    webbrowser.open("www.quickr.com")

def amzon():
    webbrowser.open("https://www.amazon.in/b?ie=UTF8&node=10923096031")

def olx():
    webbrowser.open("www.olx.in")

def gud():
    webbrowser.open("www.2gud.com")

def ul():
    webbrowser.open("www.urbanladder.com")

def pf():
    webbrowser.open("www.pepperfry.com")

def evok():
    webbrowser.open("www.evok.in")

root.mainloop()