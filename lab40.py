'''Write a program to create a window that disappears automatically after 5
seconds.'''
from tkinter import *

# time function used to calculate time
from time import time

root = Tk()


print('Running...')

start = time()

root.after(5000, root.destroy)

mainloop()

end = time()
print('Destroyed after % d seconds' % (end-start))

