from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = Tk()
root.geometry("500x500")

l1 = Label(root,text="DICTIONARY",font=("code bold",18))
l1.pack()

def info():
    meaning.config(text=dictionary.meaning(e1.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(e1.get()))
    antonym.config(text=dictionary.antonym(e1.get()))

#FRAME 1:
f1 = Frame(root)
l2 = Label(f1,text = "Enter Your Word",font=("code bold",14))
l2.pack()
e1 = Entry(f1,width=25)
e1.pack()
f1.pack()


#FRAME 2:
f2 = Frame(root)
l3 = Label(f1,text = "Meaning",font=("code bold",14))
l3.pack()
meaning = Label(f1,text="")
meaning.pack()
f2.pack()



#FRAME 3:
f3 = Frame(root)
l4 = Label(f1,text = "Antonym",font=("code bold",14))
l4.pack()
antonym = Label(f1,text="")
antonym.pack()
f3.pack()

#FRAME 4:
f4 = Frame(root)
l5 = Label(f1,text = "Synonym",font=("code bold",14))
l5.pack()
synonym = Label(f1,text="")
synonym.pack()
f3.pack()

b1 = Button(root,text="FIND",command=info)
b1.pack()

root.mainloop()
