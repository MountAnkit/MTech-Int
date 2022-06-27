'''Write a program to create an arithmetic calculator using tkinter.'''
from tkinter import *
a = Tk()
a.title("Simple Calculator")
a.geometry("302x391")
a.maxsize(302,393)
expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    var.set(expression)

def equal():
    global expression
    value = str(eval(expression))
    var.set(value)
    expression = ""

def clear():
    global expression
    expression = ""
    var.set("")



var = StringVar()
ent = Entry(a,text = "",bg = "light grey",fg = "black",font=("comicsanms",20),textvariable=var).pack(fill = X,ipady = 10)

f1 = Frame(a,bg = "white", borderwidth=0,height = 333)
f1.pack(side = TOP,fill = X,pady = 2)

def Buttons():
    b1 = Button(f1,text = "1",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press(1))
    b1.grid(row = 1,column = 1,padx = 1)
    b2 = Button(f1,text = "2",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press(2))
    b2.grid(row = 1,column = 2,padx = 1)
    b3 = Button(f1,text = "3",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press(3))
    b3.grid(row = 1,column = 3,padx = 1)
    b4= Button(f1,text = "4",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press(4))
    b4.grid(row = 2,column = 1,padx = 1,pady = 1)
    b5 = Button(f1,text = "5",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press(5))
    b5.grid(row = 2,column = 2,padx = 1, pady =1)
    b6 = Button(f1,text = "6",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press(6))
    b6.grid(row = 2,column = 3,padx = 1,pady = 1)
    b7 = Button(f1,text = "7",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press(7))
    b7.grid(row = 3,column = 1,padx = 1,pady = 1)
    b8 = Button(f1,text = "8",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press(8))
    b8.grid(row = 3,column = 2,padx = 1,pady = 1)
    b9 = Button(f1,text = "9",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press(9))
    b9.grid(row = 3,column = 3,padx = 1,pady = 1)
    b0 = Button(f1,text = "0",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press(0))
    b0.grid(row = 4,column = 2,padx = 1,pady = 1)


    b_add = Button(f1,text = "+",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press("+"))
    b_add.grid(row = 1,column = 4,padx = 1,pady = 1)
    b_sub = Button(f1,text = "-",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press("-"))
    b_sub.grid(row = 2,column = 4,padx = 1,pady = 1)
    b_mul = Button(f1,text = "X",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press("*"))
    b_mul.grid(row = 3,column = 4,padx = 1,pady = 1)
    b_div = Button(f1,text = "÷",bg = "white",fg = "black",font = '1',borderwidth = 0,width = 6,height = 3,command = lambda: press("/"))
    b_div.grid(row = 4,column = 4,padx = 1,pady = 1)
    b_eq = Button(f1,text = "=",bg = "orange",fg = "white",font = '1',borderwidth = 0,width = 6,height = 3,command = equal)
    b_eq.grid(row = 4,column = 3,padx = 1,pady = 1)
    b_clear = Button(f1,text = "AC",bg = "violet",fg = "white",font = '1',borderwidth = 0,width = 6,height = 3,command =clear)
    b_clear.grid(row = 4,column = 1,padx = 1,pady = 1)
Buttons()


a.mainloop()