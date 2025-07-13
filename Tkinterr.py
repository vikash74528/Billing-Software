from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk # for Combobox as select in html

top=Tk()
top.title('VIKASH KUMAR')
top.geometry('1200x600')

def insert():
    a=e1.get()
    b=int(e2.get())
    c=int(e3.get())
    e=e4.get()
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Python790@61',db='emp')
    cur=db.cursor()
    s="insert into emp44 values('%s','%s','%s','%s')"%(a,b,c,e)
    result=cur.execute(s)
    if(result>0):
        messagebox.showinfo("Result","Record insert successfully")
    else:
        messagebox.showinfo("Result","Record not deleted")   #not execute
    db.commit()

def Delete():
    a = e1.get()
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Python790@61', db='emp')
    cur=db.cursor()
    s="delete from emp44 where name=%s"
    result=cur.execute(s,a)
    if(result>0):
        messagebox.showinfo("Result","Record delete successfully")
    else:
        messagebox.showinfo("Result","Record not deleted") # not execute
    db.commit()

def Login():
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Python790@61',db='emp')
    cur=db.cursor()
    cur.execute("select * from emp44 where name=%s and salary=%s",(e1.get(),e2.get()))   # name and salary table se dekhkr dal fir Login kro,
    row=cur.fetchone()

    if row==None:
        messagebox.showerror("Error","Invalid Username and Password")
    else:
        top.destroy() #window close
        import datetimes  #other file link krna by login button,

#  backslace \ not allowed in image path
img=ImageTk.PhotoImage(Image.open('shoe.jpg'))
L6=Label(top,image=img)   #ye line sare label se upr deni hogi,
L6.pack()     #for apply full screen


c1=Checkbutton(top,text="java")
c1.place(x=800,y=300)
c2=Checkbutton(top,text='python')
c2.place(x=800,y=250)

r1=Radiobutton(top,text='male',value=1)
r1.place(x=1000,y=300)
r2=Radiobutton(top,text='female',value=2)
r2.place(x=1000,y=350)

k=['select','math','science','hindi','english','art','geography']
cb=ttk.Combobox(top,value=k,state='readonly')
cb.place(x=1000,y=50)
cb.current(0)


L1=Label(top,text='REGISTRATIONS FORM',fg='white',bg='green',font=('Arial 30 bold'))
L1.place(x=450,y=50)
L2=Label(top,text='Name',fg='white',bg='green',font=('Arial 20 bold'))
L2.place(x=300,y=200)
e1=Entry(top,bg='white',font=('Arial 20 bold'))
e1.place(x=400,y=200)
L3=Label(top,text='Salary',fg='white',bg='green',font=('Arial 20 bold'))
L3.place(x=300,y=250)
e2=Entry(top,font=('Arial 20 bold'))
e2.place(x=400,y=250)
L4=Label(top,text='Age',fg='white',bg='green',font=('Arial 20 bold'))
L4.place(x=300,y=300)
e3=Entry(top,font=('Arial 20 bold'))
e3.place(x=400,y=300)

L5=Label(top,text='Add',fg='white',bg='green',font=('Arial 20 bold'))
L5.place(x=300,y=350)
e4=Entry(top,font=('Arial 20 bold'))
e4.place(x=400,y=350)

b1=Button(top,text='Submit',font=('Arial 10 bold'),command=insert)
b1.place(x=500,y=400)
b2=Button(top,text='Delete',font=('Arial 10 bold'),command=Delete)
b2.place(x=575,y=400)
b2=Button(top,text='Login',font=('Arial 10 bold'),command=Login)
b2.place(x=650,y=400)


top.config(bg='blue')  #background color
top.mainloop()