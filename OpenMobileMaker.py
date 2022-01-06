import loginwindow as lw
from tkinter import *
from tkinter import ttk
from threading import Timer
import hpg as h
# creating window
splashwin =Tk()
splashwin.title(" Mobile Maker ERP ")
splashwin.geometry("1280x671")
splashwin.configure(bg="#3c3c3c")

s = ttk.Style()
s.theme_use('classic')
s.configure("blue.Horizontal.TProgressbar",background='blueviolet')
simg=PhotoImage(file="bg1.png")
splashimg=Label(splashwin,image=simg)
splashimg.pack()
pb = ttk.Progressbar(splashwin,style="blue.Horizontal.TProgressbar",orient="horizontal",length="1280",mode="determinate",value=0,maximum=100)
pb.pack()
pb.start(10)
pb.step(10)

def splashclose():
    splashwin.destroy()
    lw.openloginwindow()
    
timerr = Timer(1.2,splashclose)
timerr.start()
splashwin.mainloop()
