# Checking if a number is prime or not:
# This program is wirtten by M.H.Haddad
from tkinter import *

win = Tk()
win.geometry("200x200")
win.configure(background = "green")

def Prime_Number():
    x = n.get()
    t = 0
    for i in range(2,x-1):
        if x % i == 0:
            t+=1
        elif x % i != 0:
            pass
    if t == 0:
        l2.configure(text = "This number is Prime!",fg = "blue")
    else:
        l2.configure(text = "This number is NOT Prime!",fg = "blue")






l = Label(win, text = "Enter a number", fg = "black",bg = "green")
l.grid()

n = IntVar()

e = Entry(win,width="24",textvariable = n)
e.grid()

b = Button(win, text = "Check",bg = "blue",fg= "white",command = Prime_Number)
b.grid()


l2 = Label(win, text="",fg="green",bg="pink")
l2.grid()


win.mainloop()