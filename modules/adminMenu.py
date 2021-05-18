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

#######################################################   Admin Section   #################################################################

def view_bus():
    return

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
            if fare.get().isdigit():
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
            
            else:
                messagebox.showwarning("Error", "Please enter number value only", parent=add_Top)
    
    stations = ["Ketereh,KLT", "Cyberjaya,SLG", "Ipoh,PRK", "Skudai,JHR", "Jawi,PNG"]

    station1 = StringVar()
    station1.set(stations[0])

    station2= StringVar()
    station2.set(stations[1])

    seats = IntVar()
    seats.set(30)

    time = StringVar()

    Label(add_Top, text="Select Departure Date", font="Helvetica 10").pack(pady=(20, 0))
    date = DateEntry(add_Top)
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
    clear_frame(root)
    Label(root, text="Edit Buses", font="Helvetica 15 bold").pack(pady=30)
    
    cancel_btn = Button(root, text="Cancel", font="Helvetica 10", bg="#000000", fg="#ffffff", padx=30, command=admin_interface)
    cancel_btn.pack(pady=10)

def delete_bus():
    return

def log_out():
    confirmLogout = messagebox.askquestion ('Logout Confirmation','Are you sure you want to log out from your account?',icon = 'warning')
    if confirmLogout == 'yes':
       auth.userAuth()


def admin_interface():
    clear_frame(root)

    bus_frame = Frame(root)

    bus_list = ttk.Treeview(bus_frame, show='headings', selectmode="browse")

    bus_list['columns'] = ("Bus ID", "Departure Date", "Departure Time", "Departure Town", "Arrival Town",  "Seats Available", "Total Fare")
    bus_list.column("Bus ID", anchor=CENTER, width = 60)
    bus_list.column("Departure Date", anchor=CENTER, width = 100)
    bus_list.column("Departure Time", anchor=CENTER, width = 100)
    bus_list.column("Departure Town", anchor=CENTER, width = 100)
    bus_list.column("Arrival Town", anchor=CENTER, width = 90)
    bus_list.column("Seats Available", anchor=CENTER, width = 90)
    bus_list.column("Total Fare", anchor=CENTER, width = 70)

    bus_list.heading('Bus ID', text= 'Bus ID')
    bus_list.heading('Departure Date', text='Departure Date')
    bus_list.heading('Departure Time', text='Departure Time')
    bus_list.heading('Departure Town', text='Departure Town')
    bus_list.heading('Arrival Town', text='Arrival Town')
    bus_list.heading('Seats Available', text='Seats Available')
    bus_list.heading('Total Fare', text='Fare')

    data = view_json(dataDir + 'busesInfo.json')

    ##Append data to Treeview from Database
    global i 
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
    functionframe = Frame(root)
    
    create_btn = Button(functionframe, text="Create Bus", command=create_bus, width=20).pack(pady=(30, 20))
    edit_btn = Button(functionframe, text="Edit Bus", command=edit_bus, width=20).pack(pady=(0,10))
    delete_btn = Button(functionframe, text="Delete Bus", command=delete_bus, width=20).pack(pady=10)
    logout_btn = Button(functionframe, text="Log Out", command=log_out, width=20).pack(pady=80)
    
    Label(root, text="List of Buses", font="Helvetica 15 bold").pack(anchor = W, padx=20)

    bus_list.pack(expand=True, fill=BOTH)
    bus_frame.pack(anchor=N, side=LEFT, pady=(5, 10), padx=10, expand=True, fill=BOTH)
    functionframe.pack(anchor=N, side=RIGHT, pady=20, padx=10)