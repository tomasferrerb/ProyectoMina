# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
B1 = Button(top, text = "How are you", command = helloCallBack)
B2= Button(top, text = "bye", command = helloCallBack)
B.place(x = 30,y = 30)
B1.place(x = 50,y = 50)
B2.place(x = 70,y = 70)
top.mainloop()