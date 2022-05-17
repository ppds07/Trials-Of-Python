from tkinter import *
import time

root=Tk()
root.geometry("1600x1600")
root.config(bg="sky blue")

head=Label(root,text="SECRET MESSAGING APP",font=("Segoe Print",26,"bold"),fg="yellow",bg="purple")
head.pack(side=TOP)

head2=Label(root,text="Send your secrets to your friends from here!!",font=("Century",21,"bold"),fg="dark blue",bg="pink")
head2.place(x=440,y=80)

l1=Label(root, fg="black", bg="yellow", font=("Courier New", 15))
l1.place(x=690,y=140)


def check():
    for i in var2.get():
        secmsg=secmsg+ord(i)
    var5 = secmsg


        

def reset_button():
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
    var5.set("")

def digital_clock():
    time_live=time.strftime("%I:%M:%S %p")# capital I for 12 hour clock and capital H for 24 hour clock
    l1.config(text=time_live)
    l1.after(1000, digital_clock)

digital_clock()

name=Label(root,text="NAME:",font=("Century",21),fg="blue",bg="orange")
name.place(x=120,y=240)

var1=StringVar()
name_e=Entry(root,font=("Century",21),fg="black",textvariable=var1)
name_e.place(x=320,y=240)

message=Label(root,text="MESSAGE:",font=("Century",21),fg="blue",bg="orange")
message.place(x=120,y=320)

var2=StringVar()
message_e=Entry(root,font=("Century",21),fg="black",textvariable=var2)
message_e.place(x=320,y=320)

key=Label(root,text="KEY:",font=("Century",21),fg="blue",bg="orange")
key.place(x=120,y=380)

var3=StringVar()
key_e=Entry(root,font=("Century",21),fg="black",textvariable=var3)
key_e.place(x=320,y=380)

mode=Label(root,text="MODE:",font=("Century",21),fg="blue",bg="orange")
mode.place(x=120,y=460)

mode_extra=Label(root,text="e for encrypt and d for decrypt ",font=("Century",17),fg="blue",bg="yellow")
mode_extra.place(x=10,y=520)

var4=StringVar()
mode_e=Entry(root,font=("Century",21),fg="black",textvariable=var4)
mode_e.place(x=320,y=460)

result=Label(root,text="RESULT",font=("Century",21),fg="blue",bg="orange")
result.place(x=120,y=620)

var5=StringVar()
result_e=Entry(root,font=("Century",21),fg="black",textvariable=var5)
result_e.place(x=320,y=620)
result_e.set(text=secmsg)

show_message=Button(root,text="SHOW MESSAGE",font=("Century",19),fg="purple",bg="pink",command=check)
show_message.place(x=590,y=680)

reset=Button(root,text="RESET",font=("Century",19),fg="purple",bg="pink",command=reset_button)
reset.place(x=460,y=680)

exit_button=Button(root,text="EXIT",font=("Century",19),fg="purple",bg="pink",command=quit)
exit_button.place(x=840,y=680)

root.mainloop()