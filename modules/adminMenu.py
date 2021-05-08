######################
# Admin Bus Creation #
######################

from tkinter import *
from tkcalendar import *
root = Tk()
root.title("Admin Interface")

HEIGHT = '510'
WIDTH = '720'
root.geometry(WIDTH + 'x' + HEIGHT)

def clear_frame(root):
    for widget in root.winfo_children():
        widget.destroy()

def view_bus(root):
    return

def create_bus():
    add_Top = Toplevel(root)
    add_Top.title("Create New Bus")
    HEIGHT = '510'
    WIDTH = '680'
    add_Top.geometry(WIDTH + 'x' + HEIGHT)

    def time_picker():
        time = Frame(add_Top, width=100, height=100)
        hours = StringVar()
        ap = StringVar()

        hours = Spinbox(time, from_=0, to=23, wrap=True, state="readonly",width= 2, format="%02.0f")
        minutes = Spinbox(time, from_=0, to=59, wrap=True, state="readonly",width= 2, format="%02.0f", increment=10)
        day_night = Label(time, textvariable=ap, width=3)
        hours.pack(side=LEFT)
        minutes.pack(side=LEFT)
        day_night.pack(side=LEFT)
        if hours.get() == "12":
            ap.set("PM") 
        else:
            ap.set("AM")
        time.pack()
    
    stations = ["Tamarind Square, Cyberjaya", "Sunway, Kuala Lumpur", "Alor Gajah, Malacca", "Skudai, Johor", "Butterworth, Penang"]

    station1 = StringVar()
    station1.set(stations[0])

    station2= StringVar()
    station2.set(stations[0])

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

    Label(add_Top, text="Fare per Seat", font="Helvetica 10").pack(pady=(20,0))
    fare = Entry(add_Top, text="RM", font="Helvetica 10")
    fare.pack()

    add_btn = Button(add_Top, text="Create", font="Helvetica 10", bg="#000000", fg="#ffffff", padx=30)
    add_btn.pack(pady=(20,0))

    cancel_btn = Button(add_Top, text="Cancel", font="Helvetica 10", bg="#000000", fg="#ffffff", padx=30, command=admin_interface)
    cancel_btn.pack(pady=10)


def edit_bus():
    clear_frame(root)
    Label(root, text="Edit Buses", font="Helvetica 15 bold").pack(pady=30)
    bus = Button(root, text="A001", font="Helvetica 10", padx=50).pack(pady=(0,20))
    bus = Button(root, text="A002", font="Helvetica 10", padx=50).pack()
    bus = Button(root, text="A003", font="Helvetica 10", padx=50).pack()
    bus = Button(root, text="A004", font="Helvetica 10", padx=50).pack()
    bus = Button(root, text="A005", font="Helvetica 10", padx=50).pack()

    cancel_btn = Button(root, text="Cancel", font="Helvetica 10", bg="#000000", fg="#ffffff", padx=30, command=admin_interface)
    cancel_btn.pack(pady=10)

def delete_bus(root):
    return

def log_out(root):
    return

def admin_interface():
    clear_frame(root)
    Label(root).pack(pady=55)
    bus_list = Frame(root)
    bus_list.place(x=30, y=110)
    Label(bus_list, text="List of Buses", font="Helvetica 15 bold").pack()
    bus = Button(bus_list, text="A001", font="Helvetica 10", padx=50).pack()
    bus = Button(bus_list, text="A002", font="Helvetica 10", padx=50).pack()
    bus = Button(bus_list, text="A003", font="Helvetica 10", padx=50).pack()
    bus = Button(bus_list, text="A004", font="Helvetica 10", padx=50).pack()
    bus = Button(bus_list, text="A005", font="Helvetica 10", padx=50).pack()

    create_btn = Button(root, text="Create New Bus", command=create_bus, padx=50).pack(anchor=E, pady=10)
    edit_btn = Button(root, text="Edit Bus", command=edit_bus, padx=70).pack(anchor=E)
    delete_btn = Button(root, text="Delete Bus", command=delete_bus, padx=63).pack(anchor=E, pady=10)
    logout_btn = Button(root, text="Log Out", command=log_out, padx=70).pack(anchor=E, pady=80)

    
admin_interface()

root.mainloop()