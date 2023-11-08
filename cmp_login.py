import tkinter as tk
from tkinter import messagebox

import mysql.connector
from tkinter import *

import os
win = Tk()

def cancel():
	win.destroy()
	os.system('common.py')

def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)

def close():
	win.destroy()


def login():
	if user_id.get()=="" or password.get()=="":
		messagebox.showerror("Error","Enter User Name And Password")
	else:
		try:
			con = mysql.connector.connect(host="localhost",user="root",password="csprogrammer",database="placement")
			cur = con.cursor()

			cur.execute("select * from company where company_id=%s and Password=%s",(user_id.get(),password.get()))
			row = cur.fetchall()

			if row:
				messagebox.showinfo("Success", "Successfully Login")
				win.destroy()
				os.system('company.py')

			else:
				messagebox.showerror("Error", "Invalid User Name And Password")
				win.destroy()

			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error Due to : {str(es)}")

def signup():
	win.destroy()
	os.system('cmp_signup.py')



win.title("Company login")

win.maxsize(width=500, height=500)
win.minsize(width=500, height=500)


heading = Label(win, text="Company Login", font='Verdana 25 bold',bg='cadet blue', fg='white')
heading.place(x=80, y=150)

username = Label(win, text="User ID :", font='Verdana 10 bold',bg='cadet blue', fg='white')
username.place(x=80, y=220)

userpass = Label(win, text="Password :", font='Verdana 10 bold',bg='cadet blue', fg='white')
userpass.place(x=80, y=260)


user_id = StringVar()
password = StringVar()

userentry = Entry(win, width=40, textvariable=user_id)
userentry.focus()
userentry.place(x=200, y=223)

passentry = Entry(win, width=40, show="*", textvariable=password)
passentry.place(x=200, y=260)



btn_login = Button(win, text="Login", font='Verdana 10 bold', command=login)
btn_login.place(x=150, y=293)

btn_login = Button(win, text="Clear", font='Verdana 10 bold', command=clear)
btn_login.place(x=210, y=293)

btn_login = Button(win, text="SignUp", font='Verdana 10 bold', command=signup)
btn_login.place(x=270, y=293)

btn_home = Button(win, text="Home", font='Verdana 10 bold', command=cancel)
btn_home.place(x=340, y=293)

win.config(bg="#5f9ea0")
win.mainloop()
