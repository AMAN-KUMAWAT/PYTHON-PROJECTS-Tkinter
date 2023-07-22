from tkinter import *
root = Tk()
e = Entry(root,width=35,borderwidth=5,background="PINK")
e.grid(row=0,column=0,columnspan=3)
count =0
def button_add(number):
    first = e.get()
    e.delete(0,END)
    e.insert(0,str(first)+str(number))
    # e.delete(0,END)
    # e.insert(0,str(first)+str(number))
def clrr():
    e.delete(0,END)
def button_ad():
    first = e.get()
    global f_num
    global mt 
    mt = "addition"
    f_num = first
    e.delete(0,END)
def eqll():
    second = e.get()
    e.delete(0,END)
    if mt == "addition":
        e.insert(0,float(f_num)+float(second))
    if mt == "subtraction":
        e.insert(0,float(f_num)-float(second))
    if mt == "multiply":
        e.insert(0,float(f_num)*float(second))
    if mt == "divide":
        e.insert(0,float(f_num)/float(second))
def button_sub():
    first = e.get()
    global f_num
    global mt
    mt = "subtraction"
    f_num = first
    e.delete(0,END)

def button_mul():
    first = e.get()
    global f_num
    global mt
    mt = "multiply"
    f_num = first
    e.delete(0,END)

def button_divi():
    first = e.get()
    global f_num
    global mt
    mt = "divide"
    f_num = first
    e.delete(0,END)
def buttbck():
    var = e.get()
    x = len(var)
    x-=1
    e.delete(x,END)
    
button_1 = Button(root,text="1",padx=40,pady=20,command=lambda:button_add(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda:button_add(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda:button_add(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_add(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_add(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda:button_add(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_add(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_add(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda:button_add(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda:button_add(0))
button_clr = Button(root,text="CLEAR",padx=74,pady=20,command=clrr)
button_pls = Button(root,text="+",padx=40,pady=20,command=button_ad)
button_eql = Button(root,text="=",padx=40,pady=20,command=eqll)
button_mins = Button(root,text="-",padx=40,pady=20,command=button_sub)
button_mult = Button(root,text="*",padx=40,pady=20,command=button_mul)
button_div = Button(root,text="/",padx=40,pady=20,command=button_divi)
button_ba = Button(root,text="backspace",padx=20,pady=20,command=buttbck)
#setting the buttons
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_clr.grid(row=4,column=1,columnspan=2)
button_pls.grid(row=5,column=0)
button_eql.grid(row=5,column=1)
button_mins.grid(row=6,column=0)
button_mult.grid(row=6,column=1)
button_div.grid(row=6,column=2)
button_ba.grid(row=5,column=2)
root.mainloop()