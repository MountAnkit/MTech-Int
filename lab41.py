'''Write a program to create a button and a label inside the frame widget. Button
should change the color upon hovering over the button and label should
disappear on clicking the button.'''
from tkinter import *
win= Tk()
win.geometry("750x250")
def on_enter(e):
   button.config(background='OrangeRed3', foreground= "white")
def on_leave(e):
   button.config(background= 'SystemButtonFace', foreground= 'black')
l = Label(win,text = "Hi",bg = "green",fg = "black").pack()
button= Button(win, text= "Click Me", font= ('Helvetica 13 bold'),command = lambda : l.pack_forget())
button.pack(pady= 20)
button.bind('<Enter>', on_enter)
button.bind('<Leave>', on_leave)
win.mainloop()