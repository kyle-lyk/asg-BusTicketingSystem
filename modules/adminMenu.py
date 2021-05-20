######################
# Admin Bus Creation #
######################

from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from tkinter import ttk
import json

from systems import system
from modules import auth

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

#######################################################   Admin Section   #################################################################
def admin_interface():
    clear_frame(root)

    bus_frame = Frame(root)

    global bus_list

    bus_list = ttk.Treeview(bus_frame, show='headings', selectmode='browse')

    bus_list['columns'] = ("Bus ID", "Departure Date", "Departure Time", "Departure Town", "Arrival Town",  "Seats Available", "Total Fare")
    bus_list.column("Bus ID", anchor=CENTER, width = 45)
    bus_list.column("Departure Date", anchor=CENTER, width = 88)
    bus_list.column("Departure Time", anchor=CENTER, width = 88)
    bus_list.column("Departure Town", anchor=CENTER, width = 90)
    bus_list.column("Arrival Town", anchor=CENTER, width = 90)
    bus_list.column("Seats Available", anchor=CENTER, width = 83)
    bus_list.column("Total Fare", anchor=CENTER, width = 40)

    bus_list.heading('Bus ID', text= 'Bus ID')
    bus_list.heading('Departure Date', text='Departure Date')
    bus_list.heading('Departure Time', text='Departure Time')
    bus_list.heading('Departure Town', text='Departure Town')
    bus_list.heading('Arrival Town', text='Arrival Town')
    bus_list.heading('Seats Available', text='Seats Available')
    bus_list.heading('Total Fare', text='Fare')

    data = view_json(dataDir + 'busesInfo.json')

    ##Append data to Treeview from Database
    i = 0
    for record in data:
        bus_list.insert(parent='', index='end', iid=i, text="", values=(
            data[i]['bus_id'], 
            data[i]['departure_date'], 
            data[i]['departure_time'], 
            data[i]['departure_town'], 
            data[i]['arrival town'], 
            data[i]['total_seats'],
            data[i]['fare per seat']
            )
            )
        i += 1

    bus_list.pack(expand=True, fill=BOTH)
    bus_frame.pack(anchor=N, side=LEFT, pady=(5, 10), padx=10, expand=True, fill=BOTH)
    functionframe = Frame(root)
    functionframe.pack(anchor=N, side=RIGHT, pady=20, padx=10)

    Label(root, text="List of Buses", font="Helvetica 15 bold").pack(anchor = W, padx=20)
    
    create_btn = Button(functionframe, text="Create Bus", command=create_bus, width=20)
    edit_btn = Button(functionframe, text="Edit Bus", command=edit_bus, width=20)
    delete_btn = Button(functionframe, text="Delete Bus", command=delete_bus, width=20)
    logout_btn = Button(functionframe, text="Log Out", command=log_out, width=20)

    create_btn.pack(pady=(30, 20))
    edit_btn.pack(pady=(0,10))
    delete_btn.pack(pady=10)
    logout_btn.pack(pady=80)

def create_bus():
    add_Top = Toplevel(root)
    add_Top.title("Create New Bus")
    HEIGHT = '510'
    WIDTH = '680'
    add_Top.geometry(WIDTH + 'x' + HEIGHT)

    ## Function for minutes decrement
    def up_or_down(direction):
        if direction == 'down':
            after_pressed_minutes = int(minutes.get())
            if after_pressed_minutes == 59:
                min_update.set(after_pressed_minutes - 9)
            
    is_up_or_down = root.register(up_or_down)
    
    ## Confirm Bus Creation
    def createBusConfirm(date, departure_town, hour, minute, arrival_town, total_seats, fare):
        
        ## Generate Bus ID
        data = view_json(dataDir+'busesInfo.json')
        if not data:
            char = 'A'
            digit = 1
            newbusID = char + f"{digit:05n}"
        else:
            lastbusID = data[-1].get('bus_id')
            splitID = lastbusID.split('A')

            char = 'A'
            digit = int(splitID[1]) + 1
            newbusID = char + f"{digit:05n}"

        ## Append Data to Database
        if station1.get() == station2.get():
            messagebox.showwarning("Error", "Departure Town can not be same as Arrival Town", parent=add_Top)
        elif station1.get() != station2.get() and fare.get() == "" :
            messagebox.showwarning("Error", "Please enter the fare!", parent=add_Top)
        elif fare.get() != "" and station1.get() != station2.get():
            try:
                float(fare.get())
                busID = newbusID
                departure_date = date.get()
                start_town = departure_town.get()
                departure_hour = hour.get()
                departure_minute = minute.get()
                end_town = arrival_town.get()
                seats = total_seats.get()
                fee = fare.get()
                data = (view_json(dataDir+'busesInfo.json'))                   
                data = {
                    'bus_id': busID,
                    'departure_date': departure_date,
                    'departure_time': str(departure_hour) + ':' + str(departure_minute),
                    'departure_town': start_town,
                    'arrival town': end_town,
                    'total_seats': seats,
                    'fare per seat': fee
                    }
                add_json(data, dataDir+'busesInfo.json')  
                messagebox.showinfo("Successful!", "Bus created!", parent=add_Top)
                add_Top.destroy()
                admin_interface()
            
            ## Show warning if user input string
            except ValueError:
                messagebox.showwarning("Error", "Please enter number value only", parent=add_Top)
    
    ##Stations List
    stations = ["Ketereh,KLT", "Cyberjaya,SLG", "Ipoh,PRK", "Skudai,JHR", "Jawi,PNG"]

    station1 = StringVar()
    station1.set(stations[0])

    station2= StringVar()
    station2.set(stations[1])

    seats = IntVar()
    seats.set(30)

    time = StringVar()

    Label(add_Top, text="Select Departure Date", font="Helvetica 10").pack(pady=(20, 0))
    date = DateEntry(add_Top, date_pattern = 'dd/mm/yy')
    date.pack()

    Label(add_Top, text="Select Departure Town", font="Helvetica 10").pack(pady=(20, 0))
    departure_town = OptionMenu(add_Top, station1, *stations)
    departure_town.pack()

    Label(add_Top, text="Select Departure Time", font="Helvetica 10").pack(pady=(20, 0))
    time = Frame(add_Top, width=100, height=100)
    min_update = StringVar()
    hours = Spinbox(time, from_=0, to=23, wrap=True, state="readonly",width=2,format="%02.0f")
    minutes = Spinbox(time, from_=0, to=59, wrap=True, state="readonly",width=2, format="%02.0f", increment=10, textvariable=min_update, command=(is_up_or_down,'%d'))
    time.pack()
    hours.pack(side=LEFT)
    minutes.pack(side=LEFT)

    Label(add_Top, text="Select Arrival Town", font="Helvetica 10").pack(pady=(20, 0))
    arrival_town = OptionMenu(add_Top, station2, *stations)
    arrival_town.pack()

    Label(add_Top, text="Total Seats Available", font="Helvetica 10").pack(pady=(20,0))
    total_seats = OptionMenu(add_Top, seats, 20, 30, 40)
    total_seats.pack()

    Label(add_Top, text="Fare per Seat (RM)", font="Helvetica 10").pack(pady=(20,0))
    fare = Entry(add_Top, font="Helvetica 10")
    fare.pack()

    add_btn = Button(add_Top, text="Create", font="Helvetica 10", bg="#000000", fg="#ffffff", padx=30, command=lambda:createBusConfirm(date, station1, hours, minutes, station2, seats, fare))
    add_btn.pack(pady=(20,0))

    cancel_btn = Button(add_Top, text="Cancel", font="Helvetica 10", bg="#000000", fg="#ffffff", padx=30, command=admin_interface)
    cancel_btn.pack(pady=10)

def edit_bus():
    ## Check if admin selected a bus to edit. if not reject enter edit interface
    isEdit = False

    ## Get Item Selected from Treeview
    busid = bus_list.focus()
    if busid != '':
        buses = bus_list.item(busid, 'values')
        isEdit = True
    else:
        messagebox.showwarning("Error", "Please select a bus you want to edit")
    
    ## Function for minutes decrement
    def up_or_down(direction):
        if direction == 'down':
            after_pressed_minutes = int(minutes.get())
            if after_pressed_minutes == 59:
                min_update.set(after_pressed_minutes - 9)
            
    is_up_or_down = root.register(up_or_down)
    
    ## Confirm to Edit Bus
    def editBusConfirm(date, departure_town, hour, minute, arrival_town, total_seats, fare):
        if station1.get() == station2.get():
            messagebox.showwarning("Error", "Departure Town can not be same as Arrival Town")
        elif station1.get() != station2.get() and fare.get() == "" :
            messagebox.showwarning("Error", "Please enter the fare!")
        elif fare.get() != "" and station1.get() != station2.get():

            try:
                float(fare.get())
                departure_date = date.get()
                start_town = departure_town.get()
                departure_hour = hour.get()
                departure_minute = minute.get()
                end_town = arrival_town.get()
                seats = total_seats.get()
                fee = fare.get()

                data = (view_json(dataDir+'busesInfo.json'))                   
                
                ##Update New Bus Info
                for i in data:    
                    if i.get('bus_id') == buses[0]:
                        i['departure_date'] = departure_date
                        i['departure_time'] = str(departure_hour) + ':' + str(departure_minute)
                        i['departure_town'] = start_town
                        i['arrival town'] = end_town
                        i['total_seats'] = seats
                        i['fare per seat'] = fee
                    
                update_json(data, dataDir+'busesInfo.json')  
                messagebox.showinfo("Successful!", "Bus edited!")
                
                admin_interface()
            
            ## Show warning if user input string
            except ValueError:
                messagebox.showwarning("Error", "Please enter number value only")

    data = view_json(dataDir+'busesInfo.json')

    ##Get Bus Details
    if isEdit:
        clear_frame(root)
        for i in data:
            if i.get('bus_id') == buses[0]:

                Label(root, text="Edit Bus", font="Helvetica 15 bold").pack(pady=(10,0))

                stations = ["Ketereh,KLT", "Cyberjaya,SLG", "Ipoh,PRK", "Skudai,JHR", "Jawi,PNG"]

                station1 = StringVar()
                station1.set(i.get('departure_town'))

                station2= StringVar()
                station2.set(i.get('arrival town'))

                seats = IntVar()
                seats.set(i.get('total_seats'))

                time_before = i.get('departure_time')
                time_split = time_before.split(":")

                Label(root, text="Select Departure Date", font="Helvetica 10").pack(pady=(10, 0))
                date = DateEntry(root, date_pattern = 'dd/mm/yy')
                date.set_date(i.get('departure_date'))
                date.pack()

                Label(root, text="Select Departure Town", font="Helvetica 10").pack(pady=(20, 0))
                departure_town = OptionMenu(root, station1, *stations)
                departure_town.pack()

                Label(root, text="Select Departure Time", font="Helvetica 10").pack(pady=(20, 0))
                time = Frame(root, width=100, height=100)

                min_update = StringVar()
                hour = StringVar(time)
                
                hour.set(time_split[0])
                min_update.set(time_split[1])

                hours = Spinbox(time, from_=0, to=23, wrap=True, textvariable=hour, state="readonly", width=2, format="%02.0f")
                minutes = Spinbox(time, from_=0, to=59, wrap=True, state="readonly", width=2, format="%02.0f", increment=10, textvariable=min_update, command=(is_up_or_down,'%d'))
                time.pack()
                hours.pack(side=LEFT)
                minutes.pack(side=LEFT)

                Label(root, text="Select Arrival Town", font="Helvetica 10").pack(pady=(20, 0))
                arrival_town = OptionMenu(root, station2, *stations)
                arrival_town.pack()

                Label(root, text="Total Seats Available", font="Helvetica 10").pack(pady=(20,0))
                total_seats = OptionMenu(root, seats, 20, 30, 40)
                total_seats.pack()

                Label(root, text="Fare per Seat (RM)", font="Helvetica 10").pack(pady=(20,0))
                fare = Entry(root, font="Helvetica 10")
                fare.insert(0, str(i.get('fare per seat')))
                fare.pack()

                ConfirmEdit = Button(root, text="Edit", font="Helvetica 10", bg="#000000", fg="#ffffff", width=15, command=lambda:editBusConfirm(date, station1, hours, minutes, station2, seats, fare))
                ConfirmEdit.pack(pady=(20,0))

                cancel_btn = Button(root, text="Cancel", font="Helvetica 10", bg="#000000", fg="#ffffff", width=15, command=admin_interface)
                cancel_btn.pack(pady=10)

def delete_bus():
    ## Check if admin selected a bus to edit. if not reject enter edit interface
    isDelete = False

    ## Get Item Selected from Treeview
    bus_del = bus_list.selection()
    
    if bus_del != ():
        isDelete = True
    else:
        messagebox.showwarning("Error", "Please select a bus you want to delete")
    ##Get Item Selected in Treeview
    bus = bus_list.focus()
    buses = bus_list.item(bus, 'values')

    if isDelete:
        confirmDelete = messagebox.askquestion ('Delete Confirmation','Are you sure you want to delete the bus?',icon = 'warning')
        if confirmDelete == 'yes':
            ##Delete selection on Treeview
            data = view_json(dataDir + 'busesInfo.json')
            for info in bus_del:
                bus_list.delete(info)

            ##Delete object in database
            i = 0
            while i < len(data):
                if (data[i].get('bus_id')) == buses[0]:
                    data.pop(i)
                    update_json(data, dataDir+'busesInfo.json')
                    continue
                i += 1
                
            admin_interface()

def log_out():
    confirmLogout = messagebox.askquestion ('Logout Confirmation','Are you sure you want to log out from your account?',icon = 'warning')
    if confirmLogout == 'yes':
       auth.userAuth()