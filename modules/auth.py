############################
# AUTHENTICATION FUNCTIONS #
############################

import tkinter
from tkinter import *
from tkinter import messagebox
import json

#######################################################   Miscellaneous  #################################################################

## Clear Frame function
def clear_frame(root):
    for widget in root.winfo_children():
        widget.destroy()

### Json functions
dataDir = './data/'

def add_json(new_data,filename):
    with open (filename,"r") as f:
        temp = json.load(f)
        temp.append(new_data)
    with open (filename,"w") as f:
        json.dump(temp, f, indent = 4)

def view_json(filename):
    with open (filename,'r') as f:
        data = json.load(f)
    return data

#######################################################   User Section   #################################################################

## User Authentication Menu
def userAuth(root):
    clear_frame(root)

    Label(root, text="\nBus Ticketing System",font="Helvetica 25 bold").pack()
    Label(root, text="\nUser Authentication",font="Helvetica 20").pack()

    userLabel = Label(root, text="\n\nUsername", font="Helvetica 10").pack()
    userEntry = Entry(root, width = 30)
    userEntry.pack()

    userpasswordLabel = Label(root, text="\nPassword", font="Helvetica 10").pack()
    userpasswordEntry = Entry(root, width = 30, show="*")
    userpasswordEntry.pack()

    blankLabel = Label(root, text="").pack()
    loginButton = Button(root, width=15, text="Login", command=lambda: userVerification(userEntry,userpasswordEntry)).pack()

    regLabel = Label(root, text="\n\n\nNew to here?", font="Helvetica 10").pack()
    regButton = Button(root, width=20, text="Register user account", command=lambda: userRegisterPlatform(root)).pack()

    blankLabel = Label(root, text="\n").pack()
    adminButton = Button(root, width=20, text="Admin Site", command=lambda: adminAuth(root)).pack(anchor = "sw", padx=25,)

    copyrightLabel = Label(root, text="© 2021 Bus Ticketing System. All Rights Reserved.").pack()

## User Login Verification
def userVerification(userEntry,userpasswordEntry):
    username = userEntry.get()
    password = userpasswordEntry.get()

    if username == "" :
        messagebox.showinfo("Error", "Please enter a username!")
    elif password == "" :
        messagebox.showinfo("Error", "Please enter a password!")
    else:
        data = (view_json(dataDir+'userAcc.json'))
        userExist = False

        for i in data:
            if username == (i.get('username')) and password == (i.get('password')):
                userExist = True
                break

        if userExist:
            messagebox.showinfo(f"Welcome back!", "Login Successful!")
        else:
            messagebox.showinfo("Failed Authentication", "Username or Password is incorrect! \nPlease check if you have registered the account or not.")

## User Registration Pop-up Window
def userRegisterPlatform(root):
    ## Register Interface
    regTop = Toplevel(root)
    regTop.title("Register account")

    HEIGHT = '320'
    WIDTH = '400'
    regTop.geometry(WIDTH + 'x' + HEIGHT)
    
    ## Registration Inputs
    regLabel = Label(regTop, text="\nPlease fill in your information below",font="Helvetica 10 bold").pack()    

    reguserLabel = Label(regTop, text="\n\nUsername", font="Helvetica 10").pack()
    reguserEntry = Entry(regTop, width = 30)
    reguserEntry.pack()

    regpasswordLabel = Label(regTop, text="\nPassword", font="Helvetica 10").pack()
    regpasswordEntry = Entry(regTop, width = 30, show="*")
    regpasswordEntry.pack()

    confregpasswordLabel = Label(regTop, text="\nConfirm Password", font="Helvetica 10").pack()
    confregpasswordEntry = Entry(regTop, width = 30, show="*")
    confregpasswordEntry.pack()

    msg = StringVar()
    msgLabel = Label(regTop, textvariable = msg ).pack()
    blankLabel = Label(regTop, text= '' ).pack()
    confregButton = Button(regTop, width=20, text="Register", command=lambda: userRegisterConfirm(reguserEntry,regpasswordEntry,confregpasswordEntry,msg) ).pack()

##User Registration Confirm
def userRegisterConfirm(reguserEntry,regpasswordEntry,confregpasswordEntry,msg):

    username = reguserEntry.get()
    password = regpasswordEntry.get()
    pwconfirm = confregpasswordEntry.get()

    if username == "" :
        msg.set("Please enter a username!")
    elif ' ' in username:
        msg.set("Do not put whitespace in username!")

    elif password == "":
        msg.set("Please enter a password!")
    elif ' ' in password:
        msg.set("Do not put whitespace in password!")

    elif pwconfirm != password:
        msg.set("Passwords doesn't match!")
    else:
        data = (view_json(dataDir+'userAcc.json'))
        userExist = False

        for i in data:
            if username == (i.get('username')):
                msg.set('Username already exists. Please register another username.')
                userExist = True
        if not userExist:
            msg.set("Account created successfully! You may proceed to login.")
            data = {
                'username': username ,
                'password': password
                }
            add_json(data, dataDir+'userAcc.json')  


#######################################################   Admin Section   #################################################################

## Admin Authentication Menu
def adminAuth(root):
    clear_frame(root)

    Label(root, text="\nBus Ticketing System",font="Helvetica 25 bold").pack()
    Label(root, text="\nAdmin Authentication",font="Helvetica 20",bg = "grey",width = 500).pack()

    adminLabel = Label(root, text="\n\nAdmin Username", font="Helvetica 10").pack()
    adminEntry = Entry(root, width = 30)
    adminEntry.pack()

    adminpasswordLabel = Label(root, text="\nPassword", font="Helvetica 10").pack()
    adminpasswordEntry = Entry(root, width = 30, show="*")
    adminpasswordEntry.pack()

    blankLabel = Label(root, text="").pack()
    adminloginButton = Button(root, width=15, text="Login", command=lambda: adminVerification(adminEntry,adminpasswordEntry)).pack()

    blankLabel = Label(root, text="",height=6).pack()

    blankLabel = Label(root, text="\n").pack()
    userButton = Button(root, width=20, text="User Site", command=lambda: userAuth(root) ).pack(anchor = "sw", padx=25,)

    copyrightLabel = Label(root, text="© 2021 Bus Ticketing System. All Rights Reserved.").pack()

## Admin Login Verification    
def adminVerification(adminEntry,adminpasswordEntry):
    username = adminEntry.get()
    password = adminpasswordEntry.get()

    if username == "" :
        messagebox.showinfo("Error", "Please enter a username!")
    elif password == "" :
        messagebox.showinfo("Error", "Please enter a password!")
    else:
        data = (view_json(dataDir+'adminAcc.json'))
        userExist = False

        for i in data:
            if username == (i.get('username')) and password == (i.get('password')):
                userExist = True
                break

        if userExist:
            messagebox.showinfo(f"Welcome back!", "Login Successful!")
        else:
            messagebox.showinfo("Failed Authentication", "Username or Password is incorrect!")

