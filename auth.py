from tkinter import *



def authentication(root):
    Label(root, text="\nBus Ticketing System",font="Helvetica 25 bold").pack()
    Label(root, text="\nAuthentication",font="Helvetica 20").pack()

    userLabel = Label(root, text="\n\nUsername", font="Helvetica 10").pack()
    userEntry = Entry(root, width = 30).pack()

    passwordLabel = Label(root, text="\nPassword", font="Helvetica 10").pack()
    passwordEntry = Entry(root, width = 30, show="*").pack()

    blankLabel = Label(root, text="").pack()
    loginButton = Button(root, width=15, text="Login", command=lambda: UserVerification(userEntry,passwordEntry)).pack()

    regLabel = Label(root, text="\n\n\nNew to here?", font="Helvetica 10").pack()
    regButton = Button(root, width=20, text="Register account", command=lambda: UserRegister()).pack()

    blankLabel = Label(root, text="\n").pack()
    adminButton = Button(root, width=20, text="Admin Site", command=lambda: adminAuth()).pack(anchor = "sw", padx=25,)

def UserVerification(userEntry,passwordEntry):
    return

def UserRegister():
    return

def adminAuth():
    return