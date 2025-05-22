#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kaint
#
# Created:     22-05-2025
# Copyright:   (c) Kaint 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Tkinter Calculator
import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry("500x500")
window.config(bg="#EDC1AB")
## Inpot box to get unputs from buttons
e = Entry(window, width=80, borderwidth=10)
e.place(x=0,y=0)
## define functions for buttons
def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))
##Buttons
btn1 = Button(window, text="1", width=10,bg="#c7254e", command=lambda:click(1))
btn1.place(x=10,y=60)
btn2 = Button(window, text="2", width=10,bg="#c7254e", command=lambda:click(2))
btn2.place(x=80,y=60)
btn3 = Button(window, text="3", width=10,bg="#c7254e", command=lambda:click(3))
btn3.place(x=160,y=60)
btn4 = Button(window, text="4", width=10,bg="#c7254e" , command=lambda:click(4))
btn4.place(x=10,y=100)
btn5 = Button(window, text="5", width=10,bg="#c7254e", command=lambda:click(5))
btn5.place(x=80,y=100)
btn6 = Button(window, text="6", width=10,bg="#c7254e", command=lambda:click(6))
btn6.place(x=160,y=100)
btn7 = Button(window, text="7", width=10,bg="#c7254e", command=lambda:click(7))
btn7.place(x=10,y=140)
btn8 = Button(window, text="8", width=10,bg="#c7254e", command=lambda:click(8))
btn8.place(x=80,y=140)
btn9 = Button(window, text="9", width=10,bg="#c7254e", command=lambda:click(9))
btn9.place(x=160,y=140)
btn0 = Button(window, text="0", width=10,bg="#c7254e" , command=lambda:click(0))
btn0.place(x=10,y=180)

## operators
def add():
    n1= e.get()
    global i
    global math
    math = "addition"
    i= int(n1)
    e.delete(0,END)
btn = Button(window, text="+", width=10,bg="#c7254e", command=add)
btn.place(x=80,y=180)
def sub():
    n1= e.get()
    global i
    global math
    math = "subtraction"
    i= int(n1)
    e.delete(0,END)
btn = Button(window, text="-", width=10,bg="#c7254e", command=sub)
btn.place(x=160,y=180)
def mul():
    n1= e.get()
    global i
    global math
    math = "multplication"
    i= int(n1)
    e.delete(0,END)
btn = Button(window, text="*", width=10,bg="#c7254e", command=mul)
btn.place(x=10,y=220)
def div():
    n1= e.get()
    global i
    global math
    math = "division"
    i= int(n1)
    e.delete(0,END)
btn = Button(window, text="/", width=10,bg="#c7254e", command=div)
btn.place(x=80,y=220)

def equal():
    n2= e.get()
    e.delete(0,END)
    if math =="addition":
        e.insert(0, i+int(n2))
    elif math=="subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i/ int(n2))

btn = Button(window, text="=", width=10,bg="#c7254e", command=equal)
btn.place(x=160,y=220)

def clear():
    e.delete(0,END)
btn = Button(window, text="clear", width=10,bg="#c7254e", command= clear)
btn.place(x=10,y=260)

window.mainloop()