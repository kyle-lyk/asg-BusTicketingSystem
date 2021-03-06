###################
# TICKET HISTORY #
##################

### IMPORT MODULES
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import json

from systems import system
from modules import auth, userMenu

## Import root from system.py 
root = system.root
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

def update_json(updated_data,filename):
    with open (filename,'w') as f:
        json.dump(updated_data,f,indent=4)


#######################################################   USER TICKET HISTORY FUNCTIONS   #################################################################

def th_interface():
    clear_frame(root)
    ### Frame Layout
    treeframe = Frame(root, bg="#f3e0ca")
    functionframe = Frame(root, bg="#f3e0ca")

    ### Treeview Scrollbar
    tree_scroll = Scrollbar(treeframe)
    tree_scroll.pack(side=RIGHT, fill=Y)
    ### Treeview List 
    properties = ['Bus ID','Departure Date','Departure Time','Departure Town','Arrival Town','Selected Seat','Total Fare']
    my_tree = ttk.Treeview(treeframe, yscrollcommand=tree_scroll.set, show='headings')
    tree_scroll.config(command=my_tree.yview)
    my_tree['columns']= properties


    ## Define Columns
    my_tree.column('Bus ID', anchor=CENTER, width=50)
    my_tree.column('Departure Date', anchor=CENTER, width=92)
    my_tree.column('Departure Time', anchor=CENTER, width=92)
    my_tree.column('Departure Town', anchor=CENTER, width=93)
    my_tree.column('Arrival Town', anchor=CENTER, width=93)
    my_tree.column('Selected Seat', anchor=CENTER, width=82)
    my_tree.column('Total Fare', anchor=CENTER, width=60)


    ## Define Headings  
    my_tree.heading('Bus ID', text= 'Bus ID')
    my_tree.heading('Departure Date', text='Departure Date')
    my_tree.heading('Departure Time', text='Departure Time')
    my_tree.heading('Departure Town', text='Departure Town')
    my_tree.heading('Arrival Town', text='Arrival Town')
    my_tree.heading('Selected Seat', text='Selected Seat')
    my_tree.heading('Total Fare', text='Total Fare')


    ### Append data to Treeview from Database
    def show_all_data(my_tree):
        my_tree.delete(*my_tree.get_children()) # To clear and refresh the table
        
        data = view_json(dataDir + 'ticketHistory.json')

        for obj in data:
            if obj.get('user_id') == auth.user_id:
                total_fare = ("{:.2f}".format(obj['total_fare']))
                my_tree.insert(parent='', index='end', text="", values=(
                    obj['bus_id'], 
                    obj['departure_date'], 
                    obj['departure_time'], 
                    obj['departure_town'],
                    obj['arrival town'], 
                    obj['selected_seat'],
                    total_fare
                    )
                    )
            

    def show_selected_data(my_tree,Date,DepartureTown,ArrivalTown):
        my_tree.delete(*my_tree.get_children())

        Date = Date.get()
        DepartureTown = DepartureTown.get()
        ArrivalTown = ArrivalTown.get()


        data = view_json(dataDir + 'ticketHistory.json')

        for obj in data:
            if DepartureTown == ArrivalTown:
                messagebox.showwarning("Error", "Departure Town can not be same as Arrival Town", parent=treeframe)
                show_all_data(my_tree)
                break
            elif (obj.get('user_id') == auth.user_id):
                if (obj.get('departure_date') == Date) and (obj.get('departure_town') == DepartureTown) and (obj.get('arrival town') == ArrivalTown):
                    total_fare = ("{:.2f}".format(obj['total_fare']))
                    my_tree.insert(parent='', index='end', text="", values=(
                        obj['bus_id'], 
                        obj['departure_date'], 
                        obj['departure_time'], 
                        obj['departure_town'],
                        obj['arrival town'], 
                        obj['selected_seat'],
                        total_fare
                        )
                        )
                

    ## Show all data first by default
    show_all_data(my_tree)

    ####### WIDGETS #######
    ### Texts
    title_Label = Label(root, text= 'Ticket History', font="Helvetica 15 bold", bg="#f3e0ca").pack(anchor='n', pady=(10,0), padx=(0, 140))
    username_Label = Label(functionframe, text= f'Welcome back,\n{auth.user_id}!', font="Helvetica 10 bold", bg="#f3e0ca").pack()

    ### Dates
    dateLabel = Label(functionframe, text='Departure Date', bg="#f3e0ca").pack(pady=(15, 0))
    dateEntry = DateEntry(functionframe, date_pattern = 'dd/mm/yy')
    dateEntry.pack()

    ### Location
    stations = ["Ketereh,KLT", "Cyberjaya,SLG", "Ipoh,PRK", "Skudai,JHR", "Jawi,PNG"]

    DepartureTown = StringVar()
    DepartureTown.set(stations[0]) 

    ArrivalTown = StringVar()
    ArrivalTown.set(stations[1]) 

    DT_Label = Label(functionframe, text='Departure Town', bg="#f3e0ca").pack(pady=(15, 0))
    DT_OptionMenu = OptionMenu(functionframe, DepartureTown, *stations)
    DT_OptionMenu.config(bg="#c5bab0")
    DT_OptionMenu.pack()

    AT_Label = Label(functionframe, text='Arrival Town', bg="#f3e0ca").pack(pady=(15, 0))
    AT_OptionMenu = OptionMenu(functionframe, ArrivalTown, *stations)
    AT_OptionMenu.config(bg="#c5bab0")
    AT_OptionMenu.pack()

    SB_Button = Button(functionframe, text="Search",fg="black", bg="white",justify=CENTER,width=13, command=lambda:show_selected_data(my_tree,dateEntry,DepartureTown,ArrivalTown))
    SB_Button.pack(pady=(25, 0))

    AB_Button = Button(functionframe, text="Show All",fg="black", bg="white",justify=CENTER,width=13, command=lambda:show_all_data(my_tree))
    AB_Button.pack(pady=(10, 0))

    BS_Button = Button(functionframe, text="Bus Selection", justify=CENTER, width=20, command=lambda:userMenu.user_interface())
    BS_Button.pack(pady=(100, 0))

    AS_Button = Button(functionframe, width=20, text="Account Settings", command=lambda:acc_settings())
    AS_Button.pack(pady=(20, 0))


    ### Frame Packing
    my_tree.pack(expand=True, fill=BOTH)
    treeframe.pack(anchor=N, side=LEFT, pady=(0,15), padx=15, expand=True, fill=BOTH)
    functionframe.pack(anchor=N, side=RIGHT, pady=(10,15), padx=10)

    def handle_click(event):
        if my_tree.identify_region(event.x, event.y) == "separator":
            return "break"

    ### Disable resizing tree column
    my_tree.bind('<Button-1>', handle_click)


#######################################################   Account Settings   #################################################################
def acc_settings():
    setting_Top = Toplevel(root)

    ## Top Window Settings
    setting_Top.title("Account Settings")
    setting_Top.iconbitmap("./imgs/bus_icon.ico")
    setting_Top.configure(bg="#e9d3bf")
    WIDTH = '400'
    HEIGHT = '320'
    setting_Top.geometry(WIDTH + 'x' + HEIGHT)
    setting_Top.resizable(False, False)

    def acc_settings_menu():
        clear_frame(setting_Top)
        AccSettings_Label = Label(setting_Top, text="Account Settings", font="Helvetica 12 bold", bg="#e9d3bf").pack(pady=(60,0))
        chgpw_Button = Button(setting_Top, width=20, text="Change Password", command=lambda:ChgPw()).pack(pady=(30,0))
        logout_Button = Button(setting_Top, width=20, text="Log out",command=lambda:Logout()).pack(pady=(30,0))
        delacc_Button = Button(setting_Top, width=15, text="Delete Account", font="Helvetica 9 bold", bg="#e61212", activeforeground="white",activebackground="#990f0f",command=lambda:DelAcc())
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
                            break
                        else:
                            msg.set("Wrong Current Password, Please check again.")

            
        clear_frame(setting_Top)
        ChangePassword_Label = Label(setting_Top, text="Change Password", font="Helvetica 12 bold", bg="#e9d3bf").pack(pady=(10,0))
        
        currentpw_Label = Label(setting_Top, text="Current password", bg="#e9d3bf").pack(pady=(15,0))
        currentpw_Entry = Entry(setting_Top, width = 30)
        currentpw_Entry.pack()

        newpw_Label = Label(setting_Top, text="New password", bg="#e9d3bf").pack(pady=(10,0))
        newpw_Entry = Entry(setting_Top, width = 30)
        newpw_Entry.pack()

        confirm_newpw_Label = Label(setting_Top, text="Confirm New password", bg="#e9d3bf").pack(pady=(10,0))
        confirm_newpw_Entry = Entry(setting_Top, width = 30)
        confirm_newpw_Entry.pack()

        msg = StringVar()
        msgLabel = Label(setting_Top, textvariable = msg, bg="#e9d3bf").pack(pady=(5,0))

        confirm_Button = Button(setting_Top, width=20, text="Confirm", command=lambda:ChgPw_Verification()).pack(pady=(20,0))
        cancel_Button = Button(setting_Top, width=20, text="Cancel", command=lambda:acc_settings_menu()).pack(pady=(20,0))


    def Logout():
        confirmLogout = messagebox.askquestion ('Logout Confirmation','Are you sure you want to log out from your account?',icon = 'warning')
        if confirmLogout == 'yes':
            auth.userAuth()


    def DelAcc():
        clear_frame(setting_Top)
        Del_acc_Label = Label(setting_Top, text="Delete Account", font="Helvetica 12 bold", fg='#FF0000', bg="#e9d3bf").pack(pady=(20,0))
        warning_Label = Label(setting_Top, text="Warning:\nYour account will be permanantly erased from system once deleted", font="Helvetica 8 bold", fg='#FF0000', bg="#e9d3bf").pack(pady=(10,0))

        currentpw_Label = Label(setting_Top, text="Current password", bg="#e9d3bf").pack(pady=(15,0))
        currentpw_Entry = Entry(setting_Top, width = 30)
        currentpw_Entry.pack()

        confirm_pw_Label = Label(setting_Top, text="Confirm password", bg="#e9d3bf").pack(pady=(10,0))
        confirm_pw_Entry = Entry(setting_Top, width = 30)
        confirm_pw_Entry.pack()

        msg = StringVar()
        msgLabel = Label(setting_Top, textvariable = msg, bg="#e9d3bf").pack(pady=(5,0))

        confirm_Button = Button(setting_Top, width=20, text="Confirm", command=lambda:Del_acc_Verification()).pack(pady=(20,0))
        cancel_Button = Button(setting_Top, width=20, text="Cancel", command=lambda:acc_settings_menu()).pack(pady=(15,0))

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
