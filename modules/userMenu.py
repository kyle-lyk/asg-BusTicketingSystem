###################
# BUS SELECTION #
##################

### IMPORT MODULES
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import json

from systems import system
from modules import auth, ticketHistory, seatSelection

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




#######################################################   User Section   #################################################################

def user_interface():
    clear_frame(root)
    root.configure(bg="#f3e0ca")
    ### Frame Layout
    treeframe = Frame(root, bg="#f3e0ca")
    functionframe = Frame(root, bg="#f3e0ca")

    tree_scroll = Scrollbar(treeframe)
    tree_scroll.pack(side=RIGHT, fill=Y)

    ### Treeview List 
    properties = ['Bus ID','Departure Date','Departure Time','Departure Town','Arrival Town','Total Seat','Fare(RM)']
    my_tree = ttk.Treeview(treeframe, yscrollcommand=tree_scroll.set, show='headings')
    tree_scroll.config(command=my_tree.yview)
    my_tree['columns']= properties


    ## Define Columns
    my_tree.column('Bus ID', anchor=CENTER, width=50)
    my_tree.column('Departure Date', anchor=CENTER, width=92)
    my_tree.column('Departure Time', anchor=CENTER, width=93)
    my_tree.column('Departure Town', anchor=CENTER, width=93)
    my_tree.column('Arrival Town', anchor=CENTER, width=92)
    my_tree.column('Total Seat', anchor=CENTER, width=82)
    my_tree.column('Fare(RM)', anchor=CENTER, width=60)

    ## Define Headings  
    my_tree.heading('Bus ID', text= 'Bus ID')
    my_tree.heading('Departure Date', text='Departure Date')
    my_tree.heading('Departure Time', text='Departure Time')
    my_tree.heading('Departure Town', text='Departure Town')
    my_tree.heading('Arrival Town', text='Arrival Town')
    my_tree.heading('Total Seat', text='Seat Available')
    my_tree.heading('Fare(RM)', text='Fare(RM)')


    ### Append data to Treeview from Database
    ## Function to check how many seats available for each bus
    def available_seats(busid):
        data = (view_json(dataDir+'busesInfo.json'))
        for i in data:
            if (i.get('bus_id')) == busid:
                letter_id = []
                if i['total_seats']== 20:
                    letter_id = ["A", "B", "C", "D", "E"]
                    button_list = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4', 'e1', 'e2', 'e3', 'e4']
                    break

                elif i['total_seats'] == 30:
                    letter_id = ["A", "B", "C", "D", "E", "F", "G"]
                    button_list = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4', 'e1', 'e2', 'e3', 'e4',
                    'f1', 'f2', 'f3', 'f4', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6']
                    break

                elif i['total_seats'] == 40:
                    letter_id = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
                    button_list = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4', 'e1', 'e2', 'e3', 'e4',
                    'f1', 'f2', 'f3', 'f4', 'g1', 'g2', 'g3', 'g4', 'h1', 'h2', 'h3', 'h4', 'i1', 'i2', 'i3', 'i4', 'j1', 'j2', 'j3', 'j4']
                    break

        data2 = (view_json(dataDir+'seatInfo.json'))
        iter_letter = iter(letter_id)
        letter = next(iter_letter)

        id_list = []

        global SeatsAvailable
        SeatsAvailable = 0

        for i in data2:
            busID = i["bus_id"]
            id_list.append(busID)    

        get_id = busid
        if get_id in id_list:
            id_index = id_list.index(get_id)

        n = 0
        for i in button_list:
            if data2[id_index]["bus_id"] == busid:
                if n < ((len(data2[id_index][letter]))):
                    if(data2[id_index][letter][n]) == True:
                        SeatsAvailable += 1  

                elif n == ((len(data2[id_index][letter]))): 
                    n = 0
                    letter = next(iter_letter)
                    if(data2[id_index][letter][n]) == True:
                        SeatsAvailable += 1

                n += 1

### Show all data


    def show_all_data(my_tree):
        my_tree.delete(*my_tree.get_children())

        data = view_json(dataDir + 'busesInfo.json')

        for obj in data:
            available_seats(obj['bus_id'])
            fare_per_seat = ("{:.2f}".format(obj['fare per seat']))
            my_tree.insert(parent='', index='end', text="", values=(
                obj['bus_id'], 
                obj['departure_date'], 
                obj['departure_time'], 
                obj['departure_town'],
                obj['arrival town'], 
                str(SeatsAvailable) + "/" +str(obj['total_seats']),
                fare_per_seat
                )
            )
            
        
    def show_selected_data(my_tree,Date,DepartureTown,ArrivalTown):
        my_tree.delete(*my_tree.get_children())

        Date = Date.get()
        DepartureTown = DepartureTown.get()
        ArrivalTown = ArrivalTown.get()


        data = view_json(dataDir + 'busesInfo.json')

        for obj in data:
            if DepartureTown == ArrivalTown:
                messagebox.showwarning("Error", "Departure Town can not be same as Arrival Town", parent=treeframe)
                show_all_data(my_tree)
                break
            elif (obj.get('departure_date') == Date) and (obj.get('departure_town') == DepartureTown) and (obj.get('arrival town') == ArrivalTown):
                available_seats(obj['bus_id'])
                fare_per_seat = ("{:.2f}".format(obj['fare per seat']))
                my_tree.insert(parent='', index='end', text="", values=(
                    obj['bus_id'], 
                    obj['departure_date'], 
                    obj['departure_time'], 
                    obj['departure_town'],
                    obj['arrival town'], 
                    str(SeatsAvailable) + "/" +str(obj['total_seats']),
                    fare_per_seat
                    )
                )


    ## Show all data first by default
    show_all_data(my_tree)

    ### Proceed to selected Bus
    def select_bus():
        ## Check if user selected a bus to enter. if not reject enter seat selection interface
        isSelected = False

        ## Get Item Selected from Treeview
        busid = my_tree.focus()
        buses = my_tree.item(busid, 'values')
        
        if busid != '':
            isSelected = True
        else:
            messagebox.showwarning("Error", "Please select a bus you want to proceed")


        ## Read
        if isSelected:
            busID = buses[0]
            total_seats = (buses[5].split('/'))[1]

            fare_per_seat = buses[6]
            if total_seats == '20':
                seatSelection.seat_layout_20(root, busID, fare_per_seat, buses)
            elif total_seats == '30':
                seatSelection.seat_layout_30(root, busID, fare_per_seat, buses)
            elif total_seats == '40':
                seatSelection.seat_layout_40(root, busID, fare_per_seat, buses)

            
    ####### WIDGETS #######
    ### Texts
    title_Label = Label(root, text= 'Bus Selection', font="Helvetica 15 bold", bg="#f3e0ca").pack(anchor='n', pady=(10,0), padx=(0, 140))
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

    PB_Button = Button(functionframe, text="Select Bus",fg="black", bg="#c5bab0", justify=CENTER, width=13, activebackground="#5e514d", activeforeground="white", command=lambda:select_bus())
    PB_Button.pack(pady=(25, 0))

    TS_Button = Button(functionframe, text="Ticket History", width=20, command=lambda:ticketHistory.th_interface())
    TS_Button.pack(pady=(50, 0))

    AS_Button = Button(functionframe, width=20, text="Account Settings",command=lambda:acc_settings())
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
    setting_Top.title("Account Settings")
    setting_Top.iconbitmap("./images/bus_icon.ico")
    setting_Top.configure(bg="#e9d3bf")
    WIDTH = '400'
    HEIGHT = '320'
    setting_Top.geometry(WIDTH + 'x' + HEIGHT)

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