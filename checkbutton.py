from tkinter import *
from tkinter import ttk
win = Tk()
win.title("CHECKBUTTON")
win.minsize(width = 100,height = 100)
win.maxsize(width = 800,height = 500)
chkbut1=IntVar()
chkbut2=IntVar()
def func():
    print(chkbut1.get())
    print(chkbut2.get())
def close():
    win.destroy()

chk1 = Checkbutton(win,text="Male",variable=chkbut1,onvalue=1,offvalue=0,pady=2).place(x = 10,y = 30)
chk2 = Checkbutton(win,text="Female",variable=chkbut2,onvalue=1,offvalue=0,pady=2).place(x = 10,y = 60)
but1= Button(win,text="Submit",bg = "grey",command=func)
but1.place(x=5,y=100)
but2= Button(win,text="Quit",bg = "grey",command=close)
but2.place(x = 70,y = 100)
win.mainloop()