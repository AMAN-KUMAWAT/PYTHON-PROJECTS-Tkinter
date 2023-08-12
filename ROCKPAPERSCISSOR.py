from tkinter import *
import random

root=Tk()
root.geometry()
root.title("Rock Paper Scissor Game")

def Rocks():
    match=random.randint(0,2)
    if match==0:
        dd="Match Draw"
        cc="Rock"
    elif match==1:
        dd="Computer Wins"
        cc="Paper"
    else:
        dd="You Win"
        cc="Scissor"
    l1.config(text="Rock")
    l3.config(text=cc)
    l4.config(text=dd)

def Papers():
    match=random.randint(0,2)
    if match==0:
        dd="You Wins"
        cc="Rock"
    elif match==1:
        dd="Match Draw"
        cc="Paper"
    else:
        dd="Computer Wins"
        cc="Scissor"
    l1.config(text="Paper")
    l3.config(text=cc)
    l4.config(text=dd)

    pass
def Scissors():
    match=random.randint(0,2)
    if match==0:
        dd="Computer Wins"
        cc="Rock"
    elif match==1:
        dd="You Win"
        cc="Paper"
    else:
        dd="Match Drwa"
        cc="Scissor"
    l1.config(text="Scissor")
    l3.config(text=cc)
    l4.config(text=dd)

def Reset():
    b1["state"]="active"
    b2["state"]="active"
    b3["state"]="active"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")

Label(root,text="Rock Paper Scissor",font="normal 20 bold",fg="blue").pack(pady=20)
frame=Frame(root)
frame.pack()
l1=Label(frame,text="Player",font="10")
l2=Label(frame,text="VS",font="normal 10 bold")
l3=Label(frame,text="Computer",font="10")
l4=Label(root,text="",font="normal 20 bold",bg="white",width=15,borderwidth=2,relief="solid")
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()
l4.pack(pady=20)
frame1=Frame(root)
frame1.pack()
b1=Button(frame1,text="Rock",font=10,width=7,command=Rocks)
b2=Button(frame1,text="Paper",font=10,width=7,command=Papers)
b3=Button(frame1,text="Scissor",font=10,width=7,command=Scissors)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack()
Button(root,text="Reset Game",font="10",bg="green",command=Reset).pack(pady=20)

root.mainloop()