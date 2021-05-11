######################
# Admin Bus Creation #
######################

from tkinter import *
from tkcalendar import *
from tkinter import messagebox

import system
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

    def time_picker():
        time = Frame(add_Top, width=100, height=100)
        hours = Spinbox(time, from_=0, to=23, wrap=True, state="readonly",width=2,format="%02.0f")
        minutes = Spinbox(time, from_=0, to=59, wrap=True, state="readonly",width=2, format="%02.0f", increment=10)
        time.pack()
        hours.pack(side=LEFT)
        minutes.pack(side=LEFT)
    
    def createBusConfirm():
        if station1.get() == station2.get():
            messagebox.showwarning("Error", "Departure Town can not be same as Arrival Town", parent=add_Top)
        if station1.get() != station2.get() and fare.get() == "" :
            messagebox.showwarning("Error", "Please enter the fare!", parent=add_Top)
        if fare.get() != "":
            if fare.get().isdigit():
                messagebox.showinfo("Successful!", "Bus created!", parent=add_Top)
            
            else:
                messagebox.showwarning("Error", "Please enter number value only", parent=add_Top)
    
    stations = ["Tamarind Square, Cyberjaya", "Sunway, Kuala Lumpur", "Alor Gajah, Malacca", "Skudai, Johor", "Butterworth, Penang"]

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
    time_picker()

    Label(add_Top, text="Select Arrival Town", font="Helvetica 10").pack(pady=(20, 0))
    arrival_town = OptionMenu(add_Top, station2, *stations)
    arrival_town.pack()

    Label(add_Top, text="Total Seats Available", font="Helvetica 10").pack(pady=(20,0))
    total_seats = OptionMenu(add_Top, seats, 20, 30, 40)
    total_seats.pack()

    Label(add_Top, text="Fare per Seat (RM)", font="Helvetica 10").pack(pady=(20,0))
    fare = Entry(add_Top, font="Helvetica 10")
    fare.pack()

    add_btn = Button(add_Top, text="Create", font="Helvetica 10", bg="#000000", fg="#ffffff", padx=30, command=createBusConfirm)
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
    Label(root).pack(pady=55)
    bus_list = Frame(root)
    bus_list.place(x=30, y=110)
    Label(bus_list, text="List of Buses", font="Helvetica 15 bold").pack()

    create_btn = Button(root, text="Create New Bus", command=create_bus, padx=50).pack(anchor=E, pady=10)
    edit_btn = Button(root, text="Edit Bus", command=edit_bus, padx=70).pack(anchor=E)
    delete_btn = Button(root, text="Delete Bus", command=delete_bus, padx=63).pack(anchor=E, pady=10)
    logout_btn = Button(root, text="Log Out", command=lambda:log_out(), padx=70).pack(anchor=E, pady=80)
