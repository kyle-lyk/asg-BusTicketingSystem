###################
# BUS SELECTION #
##################

### IMPORT MODULES
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from json import *

from systems import system
from modules import auth, ticketHistory

## Import root from system.py 
root = Tk()
root.title('Bus Selection')
root.geometry('740x550')

### Frame Layout
treeframe = Frame(root)
functionframe = Frame(root)

def update_json(updated_data,filename):
    with open (filename,'w') as f:
        json.dump(updated_data,f,indent=4)




#######################################################   User Section   #################################################################

def user_interface():
    clear_frame(root)
    ### Frame Layout
    treeframe = Frame(root)
    functionframe = Frame(root)

    ### Treeview List 
    properties = ['Bus ID','Departure Date','Departure Time','Departure Town','Arrival Town','Total Seat','Fare/Seat']
    my_tree = ttk.Treeview(treeframe, show='headings')
    my_tree['columns']= properties


    ## Define Columns
    my_tree.column('Bus ID',width=50)
    my_tree.column('Departure Date',width=92)
    my_tree.column('Departure Time',width=92)
    my_tree.column('Departure Town',width=92)
    my_tree.column('Arrival Town',width=90)
    my_tree.column('Total Seat',width=82)
    my_tree.column('Fare/Seat',width=60)

### Treeview List 
properties = ['Bus ID','Departure Date','Departure Time','Departure Town','Arrival Town','Seat Available','Fare/Seat']
my_tree = ttk.Treeview(treeframe, show='headings')
my_tree['columns']= properties


## Define Columns
my_tree.column('Bus ID',width=50)
my_tree.column('Departure Date',width=92)
my_tree.column('Departure Time',width=92)
my_tree.column('Departure Town',width=92)
my_tree.column('Arrival Town',width=90)
my_tree.column('Seat Available',width=82)
my_tree.column('Fare/Seat',width=60)


<<<<<<< Updated upstream
=======
    ### Append data to Treeview from Database
    def show_all_data(my_tree):
        my_tree.delete(*my_tree.get_children())
        
        data = view_json(dataDir + 'busesInfo.json')

        for obj in data:
                my_tree.insert(parent='', index='end', text="", values=(
                    obj['bus_id'], 
                    obj['departure_date'], 
                    obj['departure_time'], 
                    obj['departure_town'],
                    obj['arrival town'], 
                    obj['total_seats'],
                    obj['fare per seat']
                    )
                    )
            
        
    def show_selected_data(my_tree,Date,DepartureTown,ArrivalTown):
        my_tree.delete(*my_tree.get_children())

        Date = Date.get()
        DepartureTown = DepartureTown.get()
        ArrivalTown = ArrivalTown.get()

        my_tree.delete(*my_tree.get_children())


        data = view_json(dataDir + 'busesInfo.json')

        for obj in data:
                if (obj.get('departure_date') == Date) and (obj.get('departure_town') == DepartureTown) and (obj.get('arrival town') == ArrivalTown):
                    my_tree.insert(parent='', index='end', text="", values=(
                        obj['bus_id'], 
                        obj['departure_date'], 
                        obj['departure_time'], 
                        obj['departure_town'],
                        obj['arrival town'], 
                        obj['total_seats'],
                        obj['fare per seat']
                        )
                        )


    ## Show all data first by default
    show_all_data(my_tree)

>>>>>>> Stashed changes

## Define Headings  
my_tree.heading('Bus ID', text= 'Bus ID')
my_tree.heading('Departure Date', text='Departure Date')
my_tree.heading('Departure Time', text='Departure Time')
my_tree.heading('Departure Town', text='Departure Town')
my_tree.heading('Arrival Town', text='Arrival Town')
my_tree.heading('Seat Available', text='Seat Available')
my_tree.heading('Fare/Seat', text='Fare/Seat')

<<<<<<< Updated upstream
=======
    title_Label = Label(treeframe, text= 'Bus Selection', font="Helvetica 15 bold").pack(anchor='n')
    username_Label = Label(functionframe, text= f'Welcome back,\n{auth.user_id}!').pack(pady=(20, 0))
>>>>>>> Stashed changes

## Define Rows
my_tree.insert(parent="", index="end", iid=0, text="", values=("A0001","27/2/2020","0020","TestTown", "TestTown", 30, "2" ))

<<<<<<< Updated upstream
####### WIDGETS #######
### Dates
date = Label(functionframe, text= 'Departure Date').pack(pady=(20, 0))
dateEntry = DateEntry(functionframe, width = 10).pack()
=======
    ### Dates
    dateLabel = Label(functionframe, text='Departure Date').pack(pady=(20, 0))
    dateEntry = DateEntry(functionframe, date_pattern = 'dd/mm/yy')
    dateEntry.pack()
>>>>>>> Stashed changes

### Location
stations = ["Ketereh,KLT", "Cyberjaya,SLG", "Ipoh,PRK", "Skudai,JHR", "Jawi,PNG"]

<<<<<<< Updated upstream
DepatureTown = StringVar()
DepatureTown.set(stations[0]) 
=======
    Date = dateEntry
    Date.pack()

    DepatureTown = StringVar()
    DepatureTown.set(stations[0]) 
>>>>>>> Stashed changes

ArrivalTown = StringVar()
ArrivalTown.set(stations[1])

DT_Label = Label(functionframe, text='Depature Town').pack(pady=(20, 0))
DT_OptionMenu = OptionMenu(functionframe, DepatureTown, *stations)
DT_OptionMenu.pack()

AT_Label = Label(functionframe, text='Arrival Town').pack(pady=(20, 0))
AT_OptionMenu = OptionMenu(functionframe, ArrivalTown, *stations)
AT_OptionMenu.pack()

<<<<<<< Updated upstream
SB_Button = Button(functionframe, text="Search",fg="white", bg="black",justify=CENTER,width=20)
SB_Button.pack(pady=(20, 0))

PB_Button = Button(functionframe, text="Proceed",fg="white", bg="black",justify=CENTER,width=20, command=show_selected)
PB_Button.pack(pady=(20, 0))
=======
    SB_Button = Button(functionframe, text="Search",fg="white", bg="black",justify=CENTER,width=10, command=lambda:show_selected_data(my_tree,dateEntry,DepatureTown,ArrivalTown))
    SB_Button.pack(pady=(20, 0))

    PB_Button = Button(functionframe, text="Proceed",fg="white", bg="black",justify=CENTER,width=10,)
    PB_Button.pack(pady=(20, 0))
>>>>>>> Stashed changes

TS_Button = Button(functionframe, width=20, text="Ticket History")
TS_Button.pack(pady=(60, 0))

AS_Button = Button(functionframe, width=20, text="Account Settings")
AS_Button.pack(pady=(40, 0))


### Frame Packing
my_tree.pack(expand=True, fill=BOTH)
treeframe.pack(anchor=N, side=LEFT, pady=20, padx=20, expand=True, fill=BOTH)
functionframe.pack(anchor=N, side=RIGHT, pady=20, padx=20)

<<<<<<< Updated upstream
=======
    def handle_click(event):
        if my_tree.identify_region(event.x, event.y) == "separator":
            return "break"

    ### Disable resizing tree column
    my_tree.bind('<Button-1>', handle_click)
>>>>>>> Stashed changes

#######################################################   Account Settings   #################################################################
def acc_settings():
    setting_Top = Toplevel(root)
    setting_Top.title("Account Settings")
    WIDTH = '400'
    HEIGHT = '320'
    setting_Top.geometry(WIDTH + 'x' + HEIGHT)

    def acc_settings_menu():
        clear_frame(setting_Top)
        AccSettings_Label = Label(setting_Top, text="Account Settings", font="Helvetica 12 bold").pack(pady=(10,0))
        chgpw_Button = Button(setting_Top, width=20, text="Change Password", command=lambda:ChgPw()).pack(pady=(30,0))
        logout_Button = Button(setting_Top, width=20, text="Log out",command=lambda:Logout()).pack(pady=(30,0))
        delacc_Button = Button(setting_Top, width=15, text="Delete Account", font="Helvetica 9 bold", bg="#FF0000",command=lambda:DelAcc())
        delacc_Button.pack(anchor='w',side=BOTTOM,padx=10,pady=10)

    acc_settings_menu()


    def ChgPw():

        def ChgPw_Verification():
            username = auth.user_id
            currentpw = currentpw_Entry.get()
            newpw = newpw_Entry.get()
            confirm_newpw = confirm_newpw_Entry.get()

            if currentpw == "" :
                msg.set("Please enter your current password!")

            elif newpw == "" :
                msg.set("Please enter a new password!")
            elif ' ' in newpw:
                msg.set("Do not put whitespace in password!")
            
            elif confirm_newpw != newpw :
                msg.set("Passwords doesn't match!")
                
            else:
                data = view_json(dataDir+'userAcc.json')

                for i in data:
                    if auth.user_id == (i.get('username')):
                        if currentpw == (i.get('password')):
                            i['password'] = newpw
                            update_json(data,dataDir+'userAcc.json')
                            
                            msg.set("Password changed successfully!")
                        else:
                            msg.set("Wrong Current Password, Please check again.")

            
        clear_frame(setting_Top)
        ChangePassword_Label = Label(setting_Top, text="Change Password", font="Helvetica 12 bold").pack(pady=(10,0))
        
        currentpw_Label = Label(setting_Top, text="Current password").pack(pady=(15,0))
        currentpw_Entry = Entry(setting_Top, width = 30)
        currentpw_Entry.pack()

        newpw_Label = Label(setting_Top, text="New password" ).pack(pady=(10,0))
        newpw_Entry = Entry(setting_Top, width = 30)
        newpw_Entry.pack()

        confirm_newpw_Label = Label(setting_Top, text="Confirm New password " ).pack(pady=(10,0))
        confirm_newpw_Entry = Entry(setting_Top, width = 30)
        confirm_newpw_Entry.pack()

        msg = StringVar()
        msgLabel = Label(setting_Top, textvariable = msg ).pack(pady=(5,0))

        confirm_Button = Button(setting_Top, width=20, text="Confirm", command=lambda:ChgPw_Verification()).pack(pady=(20,0))
        cancel_Button = Button(setting_Top, width=20, text="Cancel", command=lambda:acc_settings_menu()).pack(pady=(20,0))


    def Logout():
        confirmLogout = messagebox.askquestion ('Logout Confirmation','Are you sure you want to log out from your account?',icon = 'warning')
        if confirmLogout == 'yes':
            auth.userAuth()


    def DelAcc():
        clear_frame(setting_Top)
        Del_acc_Label = Label(setting_Top, text="Delete Account", font="Helvetica 12 bold", fg='#FF0000').pack(pady=(10,0))
        warning_Label = Label(setting_Top, text="Warning:\nYour account will be permanantly erased from system once deleted", font="Helvetica 8 bold", fg='#FF0000').pack(pady=(10,0))

        currentpw_Label = Label(setting_Top, text="Current password").pack(pady=(15,0))
        currentpw_Entry = Entry(setting_Top, width = 30)
        currentpw_Entry.pack()

        confirm_pw_Label = Label(setting_Top, text="Confirm password " ).pack(pady=(10,0))
        confirm_pw_Entry = Entry(setting_Top, width = 30)
        confirm_pw_Entry.pack()

        msg = StringVar()
        msgLabel = Label(setting_Top, textvariable = msg ).pack(pady=(5,0))

        confirm_Button = Button(setting_Top, width=20, text="Confirm", command=lambda:Del_acc_Verification()).pack(pady=(20,0))
        cancel_Button = Button(setting_Top, width=20, text="Cancel", command=lambda:acc_settings_menu()).pack(pady=(20,0))

        def Del_acc_Verification():
            username = auth.user_id
            currentpw = currentpw_Entry.get()
            confirm_pw = confirm_pw_Entry.get()

            if currentpw == "" :
                msg.set("Please enter your current password!")
            
            elif confirm_pw != currentpw :
                msg.set("Passwords doesn't match!")
                
            else:
                data = view_json(dataDir+'userAcc.json')

                for i in range(len(data)):
                    if auth.user_id == (data[i].get('username')) and currentpw == (data[i].get('password')):
                        confirm_del_acc = messagebox.askquestion ('Final Confirmation','Are you sure you want delete your account? \nYour account will be permanantly erased',icon = 'warning')
                        if confirm_del_acc == 'yes':
                            data.pop(i)
                            update_json(data,dataDir+'userAcc.json')
                            messagebox.showinfo("See you!", "Account has been deleted, Thank you for using us in the past time!")
                            auth.userAuth()
                    else:
                        msg.set("Wrong Current Password, Please check again.")