import sys
import tkinter
from tkinter import *
import time

def times():
    currenttime=time.strftime('%I:%M:%S')
    clock.config(text=currenttime)
    clock.after(200,times)


root=Tk()
root.geometry('500x250')
clock=Label(root,font=('times',50,'bold'),bg='white')
clock.grid(row=2,column=2,pady=25,padx=100)
times()

digi=Label(root,text='Digital clock By Nihal')
digi.grid(row=0,column=2)

nota=Label(root,text='Hours  Minutes  Seconds')
nota.grid(row=3,column=2)

root.mainloop()


