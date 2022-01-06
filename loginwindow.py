import sqlite3
import hpg as h
from tkinter import messagebox
from tkinter import *
from tkinter import *
from tkinter import ttk
def openloginwindow():
    logincon =sqlite3.connect("db.db",check_same_thread=False)
    logincur =logincon.cursor()
    logincur.execute('''create table IF NOT EXISTS Users(username char NOT NULL UNIQUE,password char NOT NULL)''')
    #logincur.execute('''insert into users values ('admin','admin');''')
    logincon.commit()
    logincur.execute('''create table IF NOT EXISTS Manufactured(MobileName text NOT NULL UNIQUE,ModelNo text NOT NULL UNIQUE,MRP double,ManufactureCost double, Quantity int,TestingCost double, TestingTime double,PartName text) ''')
    logincon.commit()
    logincur.execute('''create table if not exists Analysis (MobileName text,Software Rating float,Specification Rating float,Performance Rating float,Price Rating,Quality Rating float,Overall Rating float)''')
    logincon.commit()
    logincur.execute('''create table IF NOT EXISTS Inventory(PartNo string NOT NULL UNIQUE,PartName string NOT NULL,PartPrice float NOT NULL ,PartDelTime float NOT NULL,PartType strinG NOT NULL ,Quantity string NOT NULL ,SupplierNo string NOT NULL,SupplierName string NOT NULL);''')
    logincon.commit()
    


    loginwin = Tk()
    loginwin.title(" Mobile Maker ERP 1.0 :LoginPage")
    loginwin.geometry("1000x500")
    loginwin.configure(bg="#292929")
    loginwin.attributes('-topmost',1)
    def closeloginwin():
        lans=messagebox.askyesno("Close !","Closing this will not open Homepage !")
        if lans==True:
            loginwin.destroy()
    loginwin.protocol("WM_DELETE_WINDOW",closeloginwin)
    #label username
    usernamelabel = Label(loginwin,text="Username :",relief=FLAT,bg="#292929",fg="#ffa200",font=("Segoe UI Bold",18))
    usernamelabel.grid(row=1,column=1)
    #entrybox username
    global usernamevar
    usernamevar = StringVar(loginwin)
    usernameentry = Entry(loginwin,textvariable=usernamevar,width=35,bg="#ffa200",fg="#292929",font=("Segoe UI Bold",18))
    usernameentry.grid(row="1",column="2")

    #using this to add space at column zero & 3
    loginwin.grid_columnconfigure(0, weight=1)
    loginwin.grid_rowconfigure(0, weight=1)
    loginwin.grid_columnconfigure(3, weight=1)
    loginwin.grid_columnconfigure(5, weight=1)
    loginwin.grid_rowconfigure(7, weight=1)
    #password label
    passwordlabel=Label(loginwin,text="Password :",bg="#292929",relief=FLAT,fg="#ffa200",font=("Segoe UI Bold",18))
    passwordlabel.grid(row=2,column=1)

    global passwordvar
    passwordvar=StringVar()
    #password entrybox
    passwordentry =Entry(loginwin,show="*",textvariable=passwordvar,width=35,bg="#ffa200",fg="#292929",font=("Segoe UI Bold",18))
    passwordentry.grid(row=2,column=2)

    def dologin():
      #fetching username & password storing in variable
      usernametxt=usernamevar.get()
      passwordtxt=passwordvar.get()
      logincur.execute('''select * from Users where username=(?) and password=(?);''',(usernametxt,passwordtxt))
      logincon.commit()
      res=logincur.fetchall() #returns tuple ('admin','admin')
      print(res)
      # toremove data from tuple inside list
      res2=[item for t in res for item in t]
      print(res2)
      print(len(res))
      #checking if res==usernametxt+passwordtxt true then login,else textbox ko empty karo
      if len(res)!=0:
        if usernametxt!="" and passwordtxt!="" or passwordtxt!="" or usernametxt!="" and  res2[0]==usernametxt and passwordtxt==res2[1]:
          messagebox.showinfo('Loggin Success!'," Opening Mobile Maker ERP")
          usernameentry.delete(0,END)
          passwordentry.delete(0,END)
          loginwin.destroy()
          h.openhomepage()
          # ekde call kar tya module madlya function la 
          # openhomepage()

      if usernametxt!="" and passwordtxt!="" or passwordtxt!="" or usernametxt!="" and len(res)==0:
          if len(res)==0:
            usernameentry.delete(0,END)
            passwordentry.delete(0,END)
            messagebox.showerror("error","Invalid Username or Password ")  
        
      elif usernametxt=="" and passwordtxt=="" or passwordtxt=="" or usernametxt=="":
        messagebox.showerror("error","Field is empty")  
        usernameentry.delete(0,END)
        passwordentry.delete(0,END)
      
    def doregisterdef():
        usernametxt=usernamevar.get()
        passwordtxt=passwordvar.get()
        if usernametxt=="" and passwordtxt=="" or passwordtxt=="" or usernametxt=="":
            messagebox.showerror("error","Field is empty")  
            usernameentry.delete(0,END)
            passwordentry.delete(0,END)
        else:
        #clears entrybox text when we put invalid username & password
            logincur.execute('''insert into users values (?,?)''',[usernametxt,passwordtxt])
            logincon.commit()
            usernameentry.delete(0,END)
            passwordentry.delete(0,END)

    def docleardef():
        usernameentry.delete(0,END)
        passwordentry.delete(0,END)
    def aboutdef():
        messagebox.showwarning("WARNING", "We Hope You Are Authorized Personnel\n To Register & Login !!")
    #buttons LOGIN,CLEAR,REGISTER


    def loginbuttonentered(event):
      loginstatusbar.configure(text="Click this button to Login, After Filling username & password")

    def loginbuttonleft(event):
      loginstatusbar.configure(text="")

    loginbutton = Button(loginwin,text=" Login ",relief=FLAT ,command=dologin,bg="#ffa200",fg="#292929",font=("Segoe UI Bold",14))
    loginbutton.grid(row=6,column=2)
    loginbutton.bind("<Enter>",loginbuttonentered)
    loginbutton.bind("<Leave>",loginbuttonleft)



    registerbutton=Button(loginwin,text="Register",relief=FLAT ,command=doregisterdef,bg="#ffa200",fg="#292929",font=("Segoe UI Bold",14))
    registerbutton.grid(row=6,column=4)

    def regbuttonentered(event):
      loginstatusbar.configure(text=" Enter Your Name & Password, Click this button to register")

    def regbuttonleft(event):
      loginstatusbar.configure(text="")
    registerbutton.bind("<Enter>",regbuttonentered)
    registerbutton.bind("<Leave>",regbuttonleft)

    def clearbuttonentered(event):
      loginstatusbar.configure(text="Click this button to Clear Text")

    def clearbuttonleft(event):
      loginstatusbar.configure(text="")

    clearbutton=Button(loginwin,text="Clear",relief=FLAT ,command=docleardef,bg="#ffa200",fg="#292929",font=("Segoe UI Bold",14))
    clearbutton.grid(row=6,column=1)
    clearbutton.bind("<Enter>",clearbuttonentered)
    clearbutton.bind("<Leave>",clearbuttonleft)

    aboutbutton=Button(loginwin,text="About",relief=FLAT ,command=aboutdef,bg="#ffa200",fg="#292929",font=("Segoe UI Bold",14))
    aboutbutton.grid(row=6,column=0)

    loginstatusbar =Label(loginwin,text="",bg="#292929",fg="#ffa200",font=("Segoe UI Italic",12))
    loginstatusbar.grid(row=8,column=2)
    loginwin.mainloop()

