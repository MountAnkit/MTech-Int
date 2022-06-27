'''Write a program to draw colored shapes (line, rectangle, oval) on canvas.'''
from tkinter import *
app = Tk()
app.title("Canvas")

canvas = Canvas(app)
canvas.pack()

#Line
canvas.create_line(10, 10, 100, 100)

#Rectangle
canvas.create_rectangle(150,150,250,250,fill = "yellow")

#Oval
canvas.create_oval(10,150,100,200,fill="blue")
app.mainloop()