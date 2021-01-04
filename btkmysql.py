import MySQLdb
import Tkinter
from Tkinter import *
import tkMessageBox
import tkFont
import os
db=MySQLdb.connect("localhost","root",'465231',"bank")
cursor=db.cursor()

def menu():
	global w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12
	w1=Tkinter.Tk()
	w1.geometry("1920x1080")
	w1.title("Indian Bank")
	x="*** Welcome to Indian Bank ***"
	z=Tkinter.Button(w1,text="Manager", command=managercheck,relief=GROOVE,height=3,width=20)
	z.place(x=30,y=100)
	c=Tkinter.Button(w1,text="Customer", command=customer,relief=GROOVE,height=3,width=20)
	c.place(x=30,y=300)
	w1.mainloop()


def managercheck():
	global ent1,ent2
	global t1,t2,w4
	w4=Tkinter.Tk()
	w4.geometry("1920x1080")
	a="*** Please enter your ID and Password ***"

	b=Label(w4,text=a)
	b.pack()
	lb=Label(w4,text="ID")
	lb.place(x=20,y=100)
	ent1=Tkinter.Entry(w4,bd=2)
	ent1.place(x=320,y=100)
	lb=Label(w4,text="Password")
	lb.place(x=20,y=200)
	ent2=Tkinter.Entry(w4,bd=2,show="*")
	ent2.place(x=320,y=200)
	bt1=Tkinter.Button(w4,text="Login",command=check,relief=GROOVE)
	bt1.place(x=20,y=300)
	b.pack()
	t1=ent1.get()
	t2=ent2.get()
	

def check():
	global t1,t2
	t1=ent1.get()
	t2=ent2.get()	
	idd="manager"
	pw="12345"
	if (t1==idd and t2==pw):
		w4.destroy()
		manager()
	else:
		w4.destroy()
def manager():
	w2=Tkinter.Tk()
	w2.geometry("1920x1080")
	w2.title("Manger")
	a="*** Welcome Sir/Mam ***"
	b=Label(w2,text=a)
	b.pack()
	bt1=Tkinter.Button(w2,text="Create Account",command=createaccount,relief=GROOVE)
	bt1.place(x=30,y=100)
	bt2=Tkinter.Button(w2,text="Check Balance",command=checkbl,relief=GROOVE)
	bt2.place(x=30,y=300)
	bt3=Tkinter.Button(w2,text="Add Money",command=addm,relief=GROOVE)
	bt3.place(x=30,y=500)
	bt3=Tkinter.Button(w2,text="View All Cutomer",command=vlc,relief=GROOVE)
	bt3.place(x=30,y=700)
	
def vlc():
	w12=Tkinter.Tk()
	w12.geometry("500x800")
	cursor.execute("""select * from cs""")
	a=cursor.fetchall()
	for i in a:
		lb=Label(w12,text=i)
		lb.pack()
def createaccount():
	global a1,a2,a3,a4,w3
	global ent1,ent2,ent3,ent4
	w3=Tkinter.Tk()
	w3.geometry("1920x1080")
	w3.title("Create Account")
	b="*** Enter the Account Holders Details ***"
	c=Label(w3,text=b)
	c.pack()
	lb=Label(w3,text="Name")
	lb.place(x=20,y=100)
	ent1=Tkinter.Entry(w3,bd=2)
	ent1.place(x=320,y=100)
	lb=Label(w3,text="Account Number")
	lb.place(x=20,y=200)
	ent2=Tkinter.Entry(w3,bd=2)
	ent2.place(x=320,y=200)
	lb=Label(w3,text="Balance")
	lb.place(x=20,y=300)
	ent3=Tkinter.Entry(w3,bd=2)
	ent3.place(x=320,y=300)
	lb=Label(w3,text="Mobile Number")
	lb.place(x=20,y=400)
	ent4=Tkinter.Entry(w3,bd=2)
	ent4.place(x=320,y=400)
	bt2=Tkinter.Button(w3,text="Submit",command=submit,relief=GROOVE)
	bt2.place(x=100,y=500)
	bt2=Tkinter.Button(w3,text="Clear",command=clear,relief=GROOVE)
	bt2.place(x=300,y=500)
	bt2=Tkinter.Button(w3,text="Exit",command=exit,relief=GROOVE)
	bt2.place(x=500,y=500)
	a1=ent1.get()
	a2=ent2.get()
	a3=ent3.get()
	a4=ent4.get()
def exit():
	w3.destroy()
def clear():
	w3.destroy()
	createaccount()
def submit():
	global a1,a2,a3,a4
	global ent1,ent2,ent3,ent4
	a1=ent1.get()
	a2=ent2.get()
	a3=ent3.get()
	a4=ent4.get()
	cursor.execute("""insert into cs(account_no,name,balance,contact_no) values('%s','%d','%s','%s')"""(a2,a1,a3,a4))
	db.commit()
	print ("successfully Submmited")


def checkbl():
	global ent1
	global t1
	w5=Tkinter.Tk()
	w5.geometry("1920x1080")
	w5.title("Check Balance")
	a="*** Please Enter the following ***"
	b=Label(w5,text=a)
	b.pack()
	lb=Label(w5,text="Account Number")
	lb.place(x=20,y=100)
	ent1=Tkinter.Entry(w5,bd=2)
	ent1.place(x=320,y=100)
	bt2=Tkinter.Button(w5,text="View",command=view,relief=GROOVE)
	bt2.place(x=50,y=150)
	t1=ent1.get()
def view():
	w6=Tkinter.Tk()
	w6.geometry("500x600")
	w6.title("Balance")
	t1=ent1.get()
	t1=int(t1)
	cursor.execute("""select balance from cs where account_no='%s'"""%(t1))
	a=cursor.fetchone()
	lb=Label(w6,text=a)
	lb.pack()
		

def addm():
	global t1,t2
	global ent1,ent2
	w7=Tkinter.Tk()
	w7.geometry("800x900")
	lb=Label(w7,text="Enter Account Number")
	lb.place(x=20,y=100)
	ent1=Tkinter.Entry(w7,bd=2)
	ent1.place(x=320,y=100)
	lb=Label(w7,text="Enter Amount")
	lb.place(x=30,y=200)
	ent2=Tkinter.Entry(w7,bd=2)
	ent2.place(x=320,y=200)
	bt1=Tkinter.Button(w7,text="Add",command=addd,relief=GROOVE)
	bt1.place(x=60,y=300)
	t1=ent1.get()
	t2=ent2.get()
	
def addd():
	global t1,t2,ent1,ent2
	t1=ent1.get()
	t2=ent2.get()
	t2=int(t2)
	cursor.execute(""" select Balance from cs where account_no='%s' """%(t1))
	a=cursor.fetchone()
	print a

	for h in a:
		kk = a[0]
	kk=int(kk)
	ll=kk+t2
	cursor.execute(""" update cs set balance='%d' where account_no='%s' """%(ll,t1))
	db.commit()
	print ll
	view()
def customer():
	w8=Tkinter.Tk()
	w8.geometry("1920x1080")
	bt1=Tkinter.Button(w8,text="Deposit",command=addm)
	bt1.place(x=30,y=100)
	bt2=Tkinter.Button(w8,text="Show Balance",command=shbl)
	bt2.place(x=30,y=200)
	bt3=Tkinter.Button(w8,text="withdraw",command=withdraw)
	bt3.place(x=30,y=300)
def shbl():
	global ent1
	global t1
	w9=Tkinter.Tk()
	w9.geometry("1920x1080")
	w9.title("Check Balance")
	a="*** Please Enter the following ***"
	b=Label(w9,text=a)
	b.pack()
	lb=Label(w9,text="Account Number")
	lb.place(x=20,y=100)
	ent1=Tkinter.Entry(w9,bd=2)
	ent1.place(x=320,y=100)
	bt2=Tkinter.Button(w9,text="View",command=view,relief=GROOVE)
	bt2.place(x=50,y=150)
	t1=ent1.get()

def withdraw():
	global t1,t2
	global ent1,ent2
	w10=Tkinter.Tk()
	w10.geometry("800x900")
	lb=Label(w10,text="Enter Account Number")
	lb.place(x=20,y=100)
	ent1=Tkinter.Entry(w10,bd=2)
	ent1.place(x=320,y=100)
	lb=Label(w10,text="Enter Amount")
	lb.place(x=30,y=200)
	ent2=Tkinter.Entry(w10,bd=2)
	ent2.place(x=320,y=200)
	bt1=Tkinter.Button(w10,text="Withdraw",command=withdrw,relief=GROOVE)
	bt1.place(x=60,y=300)
	t1=ent1.get()
	t2=ent2.get()
def withdrw():
	global t1,t2,ent1,ent2
	t1=ent1.get()
	t2=ent2.get()
	t2=int(t2)
	cursor.execute(""" select balance from cs where account_no='%s' """%(t1))
	a=cursor.fetchone()
	print a
	for h in a:
		kk = a[0]
	kk=int(kk)
	if kk>t2:
		ll=kk-t2
	else:
		w11=Tkinter.Tk()
		w11.geometry("500x800")
		a="Insuficent Balance"
		lb=Label(w11,text=a)
		lb.pack()
	cursor.execute(""" update cs set balance='%d' where account_no='%s' """%(ll,t1))
	db.commit()
	print ll
	view()





menu()
