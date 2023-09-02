##################
# AUTHENTICATION #
##################

### IMPORT MODULES
from tkinter import *
from tkinter import messagebox
import json
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from systems import system
from modules import adminMenu, userMenu
import smtplib
from email.mime.text import MIMEText
## Import root from system.py 
root = system.root


#######################################################   Miscellaneous  #################################################################

### Clear Frame function
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
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        if not data:
            return []  # Return an empty list if the file is empty
        return data
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []  # Return an empty list if the file is missing
    except json.JSONDecodeError as e:
        print(f"JSON decoding error in {filename}: {e}")
        return []  # Return an empty list if JSON decoding fails
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []  # Return an empty list for other exceptions



## Store logged in username
user_id = None

#######################################################   User Section   #################################################################

## User Authentication Menu
def userAuth():
    clear_frame(root)
    

    bg = PhotoImage(file="./img/tribus.png")
    root.bg = bg # to prevent the image garbage collected

    #create canvas
    my_canvas = Canvas(root)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image((0,0), image=bg, anchor="nw")

    my_canvas.create_text(370, 60, text="TriBus Ticketing System",font="Verdana 25 bold", fill="white")
    my_canvas.create_text(370, 110, text="User Authentication", font="Helvetica 20", fill="white")

    frame = Frame(root, bg = "white")
    frame_window = my_canvas.create_window(370,280, window =frame, width = 380, height = 300)

    userLabel = Label(frame, text="\n\nUsername", font="Helvetica 10", bg="white").pack()
    userEntry = Entry(frame, width = 30, highlightbackground='#c99d9d', highlightthickness=1)
    userEntry.pack()

    userpasswordLabel = Label(frame, text="\nPassword", font="Helvetica 10", bg="white").pack()
    userpasswordEntry = Entry(frame, width = 30, show="*", highlightbackground='#c99d9d', highlightthickness=1)
    userpasswordEntry.pack()

    blankLabel = Label(frame, text="", bg="white").pack()
    loginButton = Button(frame, width=15, text="Login", command=lambda: userVerification(userEntry,userpasswordEntry)).pack()

    regLabel = Label(frame, text="\n\n\nNew to here?", font="Helvetica 10", bg="white").pack()
    regButton = Button(frame, width=20, text="Register user account", activeforeground="white",activebackground="black", command=lambda: userRegisterPlatform()).pack()

    adminButton = Button(root, width=20, text="Admin Site", command=lambda: adminAuth())
    adminButtonwin = my_canvas.create_window(30, 490, anchor=SW, window=adminButton)

    copyrightLabel = my_canvas.create_text(370, 520, text="© 2023 TriBus Ticketing System. All Rights Reserved.", fill="black")


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
            global user_id 
            user_id = username
            messagebox.showinfo("Welcome back!", "Login Successful!")
            userMenu.user_interface()
        else:
            messagebox.showinfo("Failed Authentication", "Username or Password is incorrect! \nPlease check if you have registered the account or not.")

## User Registration Pop-up Window
def userRegisterPlatform():
    
    ## Top Window Settings
    regTop = Toplevel(root)
    regTop.title("Register account")
    regTop.iconbitmap("./img/bus_icon.ico")
    regTop.configure(bg="#faf1e3")
    WIDTH = '400'
    HEIGHT = '320'
    regTop.geometry(WIDTH + 'x' + HEIGHT)
    regTop.resizable(False, False)
    
    ## Registration Inputs
    regLabel = Label(regTop, text="\nPlease fill in your information below",font="Times 13 bold", bg="#faf1e3").pack()    

    reguserLabel = Label(regTop, text="\n\nUsername", font="Times 10", bg="#faf1e3").pack()
    reguserEntry = Entry(regTop, width = 30)
    reguserEntry.pack()

    regpasswordLabel = Label(regTop, text="\nPassword", font="Times 10", bg="#faf1e3").pack()
    regpasswordEntry = Entry(regTop, width = 30, show="*")
    regpasswordEntry.pack()

    confregpasswordLabel = Label(regTop, text="\nConfirm Password", font="Times 10", bg="#faf1e3").pack()
    confregpasswordEntry = Entry(regTop, width = 30, show="*")
    confregpasswordEntry.pack()

    msg = StringVar()
    msgLabel = Label(regTop, textvariable = msg, bg="#faf1e3").pack()
    blankLabel = Label(regTop, text= '', bg="#faf1e3").pack()
    confregButton = Button(regTop, width=20, text="Register", 
                    fg="white", bg="#e0c787", activebackground="#ccb67c", font="Impact 10",
                    command=lambda: userRegisterConfirm(reguserEntry,regpasswordEntry,confregpasswordEntry,msg))
    confregButton.pack()

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

def adminAuth():
    global adminEmailEntry  
    clear_frame(root)
    bg = PhotoImage(file="./img/tribus.png")
    root.bg = bg  # To prevent the image from being garbage collected

    # Create canvas
    my_canvas = Canvas(root)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image((0, 0), image=bg, anchor="nw")

    my_canvas.create_text(370, 60, text="TriBus Ticketing System", font="Verdana 25 bold", fill="white")
    my_canvas.create_text(370, 110, text="Admin Authentication", font="Helvetica 20", fill="white")

    frame = Frame(root, bg="white")
    frame_window = my_canvas.create_window(370, 280, window=frame, width=380, height=300)

    adminLabel = Label(frame, text="\n\nAdmin Email", font="Helvetica 10", bg="white").pack()
    adminEmailEntry = Entry(frame, width=30, highlightbackground='#c99d9d', highlightthickness=1)
    adminEmailEntry.pack()

    adminpasswordLabel = Label(frame, text="\nPassword", font="Helvetica 10", bg="white").pack()
    adminpasswordEntry = Entry(frame, width=30, show="*", highlightbackground='#c99d9d', highlightthickness=1)
    adminpasswordEntry.pack()

    blankLabel = Label(frame, text="", bg="white").pack()
    adminloginButton = Button(frame, width=15, text="Login", command=lambda: adminVerification(adminEmailEntry, adminpasswordEntry)).pack()

    userButton = Button(root, width=20, text="User Site", command=lambda: userAuth())
    userButtonwin = my_canvas.create_window(30, 490, anchor=SW, window=userButton)

    copyrightLabel = my_canvas.create_text(370, 520, text="© 2023 TriBus Ticketing System. All Rights Reserved.", fill="black")

def adminVerification(adminEntry, adminpasswordEntry):
    email = adminEntry.get()
    password = adminpasswordEntry.get()

    if email == "":
        messagebox.showinfo("Error", "Please enter an email address!")
    elif password == "":
        messagebox.showinfo("Error", "Please enter a password!")
    else:
        data = view_json(dataDir + 'adminAcc.json')
        userExist = False

        for i in data:
            if email == (i.get('username')) and password == (i.get('password')):
                userExist = True
                break

        if userExist:
            messagebox.showinfo(f"Welcome back!", "Login Successful!")

            # Get the client's IP address
            client_ip = get_client_ip()

            if client_ip:
                print(f"Client IP Address: {client_ip}")
                # Send the email notification with the client's IP address
                send_email_notification(email, client_ip)
            else:
                print("Unable to retrieve client IP address.")

            adminMenu.admin_interface()
        else:
            messagebox.showinfo("Failed Authentication", "Email or Password is incorrect!")

def get_client_ip():
    try:
        # Get the client's IP address using socket
        client_ip = socket.gethostbyname(socket.gethostname())
        return client_ip
    except Exception:
        return None


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime  # Add this import for date and time

def send_email_notification(email, client_ip):
    sender_name = "TriBus Ticketing System"  # Your desired sender name
    sender_email = 'ojt.rms.group.4@gmail.com'  # Your email address
    sender_password = 'hbpezpowjedwoctl'  # Your email password
    recipient_email = email

    subject = 'Login Alert'
    current_datetime = datetime.datetime.now()  # Get the current date and time
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')  # Format date and time

    # HTML-formatted message with styling
    message = f"""
    <html>
        <head>
            <style>
                body {{
                    background-color: #f2f2f2;
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    max-width: 600px;
                    margin: 20px auto;
                }}
                h2 {{
                    color: #333;
                }}
                p {{
                    color: #555;
                }}
                ul {{
                    list-style: none;
                    padding: 0;
                }}
                li {{
                    margin-bottom: 10px;
                }}
                .footer {{
                    background-color: #333;
                    color: #fff;
                    text-align: center;
                    padding: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Hello Admin,</h2>
                <p>You have successfully logged in. Here are the details:</p>
                <ul>
                    <li><strong>Email:</strong> {recipient_email}</li>
                    <li><strong>IP Address:</strong> {client_ip}</li>
                    <li><strong>Login Date:</strong> {formatted_datetime.split()[0]}</li>
                    <li><strong>Login Time:</strong> {formatted_datetime.split()[1]}</li>
                </ul>
            </div>
            <div class="footer">
                &copy; 2023 TriBus Ticketing System. All Rights Reserved.
            </div>
        </body>
    </html>
    """

    msg = MIMEMultipart()
    msg.attach(MIMEText(message, 'html'))
    msg['Subject'] = subject
    msg['From'] = f'{sender_name} <{sender_email}>'  # Set sender name and email
    msg['To'] = recipient_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email notification sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

