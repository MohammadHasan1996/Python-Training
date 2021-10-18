from tkinter import *
from subprocess import check_output
import os

win = Tk()



def Find_Drive():
    drive = ["A:","B:","C:","D:","E:","F:","G:","H:","I:","J:","K:","O:","Z:"]
    sys_Drive =[]
    cmd = check_output("wmic logicaldisk get name",shell= True)
    for i in drive:
        if i in str(cmd):
            sys_Drive.append(i)

    l1.configure(text= sys_Drive,fg ="green")
    return sys_Drive




def DIR():
    cmd = check_output("dir",shell = True)
    l2.configure(text = cmd , fg = "red")




lable1 = Label(win, text="Please Choose one of this options:   ")
lable1.grid()

button1 = Button(win,text="Find_Drive",command= Find_Drive,bg="blue")
button1.grid()
l1 = Label(win, text="",fg="green")
l1.grid()

button2 = Button(win,text="DIR",command=DIR,bg="green")
button2.grid(ipadx=10,column=2,row=1)
l2 = Label(win, text="",fg="red")
l2.grid()

win.mainloop()
