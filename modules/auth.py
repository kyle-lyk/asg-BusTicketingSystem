############################
# AUTHENTICATION FUNCTIONS #
############################

from tkinter import *

#######################################################   Miscellaneous  #################################################################

## Clear Frame function
def clear_frame(root):
    for widget in root.winfo_children():
        widget.destroy()

### Json functions

def save_to_json_file(data, filename):
    with open(filename,"w") as file_obj:
        json.dump(data, file_obj, indent=4)

def open_from_json_file(filename):
    with open(filename) as file_obj:
        return 

def show_books(data):
  return

#######################################################   User Section   #################################################################

## User Authentication Menu
def userAuth(root):
    clear_frame(root)

    Label(root, text="\nBus Ticketing System",font="Helvetica 25 bold").pack()
    Label(root, text="\nUser Authentication",font="Helvetica 20").pack()

    userLabel = Label(root, text="\n\nUsername", font="Helvetica 10").pack()
    userEntry = Entry(root, width = 30).pack()

    userpasswordLabel = Label(root, text="\nPassword", font="Helvetica 10").pack()
    userpasswordEntry = Entry(root, width = 30, show="*").pack()

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
    userpassword = userpasswordEntry.get()

    return


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
    reguserEntry = Entry(regTop, width = 30).pack()

    regpasswordLabel = Label(regTop, text="\nPassword", font="Helvetica 10").pack()
    regpasswordEntry = Entry(regTop, width = 30, show="*").pack()

    confregpasswordLabel = Label(regTop, text="\nConfirm Password", font="Helvetica 10").pack()
    confregpasswordEntry = Entry(regTop, width = 30, show="*").pack()

    blankLabel = Label(regTop, text="").pack()
    confregButton = Button(regTop, width=20, text="Register", command=lambda: userRegisterConfirm() ).pack()

##User Registration Confirm
def userRegisterConfirm():
    return


#######################################################   Admin Section   #################################################################

## Admin Authentication Menu
def adminAuth(root):
    clear_frame(root)

    Label(root, text="\nBus Ticketing System",font="Helvetica 25 bold").pack()
    Label(root, text="\nAdmin Authentication",font="Helvetica 20",bg = "grey",width = 500).pack()

    adminLabel = Label(root, text="\n\nAdmin Username", font="Helvetica 10").pack()
    adminEntry = Entry(root, width = 30).pack()

    adminpasswordLabel = Label(root, text="\nPassword", font="Helvetica 10").pack()
    adminpasswordEntry = Entry(root, width = 30, show="*").pack()

    blankLabel = Label(root, text="").pack()
    adminloginButton = Button(root, width=15, text="Login", command=lambda: adminVerification(adminEntry,adminpasswordEntry)).pack()

    adminregLabel = Label(root, text="\n\n\nNew to here?", font="Helvetica 10").pack()
    adminregButton = Button(root, width=20, text="Register admin account", command=lambda: adminRegisterPlatform(root)).pack()

    blankLabel = Label(root, text="\n").pack()
    userButton = Button(root, width=20, text="User Site", command=lambda: userAuth(root) ).pack(anchor = "sw", padx=25,)

    copyrightLabel = Label(root, text="© 2021 Bus Ticketing System. All Rights Reserved.").pack()

## Admin Login Verification    
def adminVerification(adminEntry,adminpasswordEntry):
    return

## Admin Registration Pop-up Window
def adminRegisterPlatform(root):
    ## Register Interface
    amregTop = Toplevel(root)
    amregTop.title("Register admin account")

    HEIGHT = '320'
    WIDTH = '400'
    amregTop.geometry(WIDTH + 'x' + HEIGHT)
    
    ## Registration Inputs
    amregLabel = Label(amregTop, text="\nPlease fill in your information below",font="Helvetica 10 bold").pack()    

    amreguserLabel = Label(amregTop, text="\n\nAdmin Username", font="Helvetica 10").pack()
    amreguserEntry = Entry(amregTop, width = 30).pack()

    amregpasswordLabel = Label(amregTop, text="\nPassword", font="Helvetica 10").pack()
    amregpasswordEntry = Entry(amregTop, width = 30, show="*").pack()

    amconfregpasswordLabel = Label(amregTop, text="\nConfirm Password", font="Helvetica 10").pack()
    amconfregpasswordEntry = Entry(amregTop, width = 30, show="*").pack()

    blankLabel = Label(amregTop, text="").pack()
    amconfregButton = Button(amregTop, width=20, text="Register", command=lambda: adminRegisterConfirm() ).pack()


## Admin Registration Confirm
def adminRegisterConfirm():
    return