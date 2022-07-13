from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Months")
var  = StringVar()
com = ttk.Combobox(window,width=50,textvariable=var)
com['values'] = ("January","February","March","April","March","May","June","July","August","September","October","November","December")

com.grid(column = 1,row = 6)
com.current(3)#The position in list where you want to show default month (April)
window.mainloop()