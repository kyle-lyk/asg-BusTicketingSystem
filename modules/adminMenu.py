######################
# Admin Bus Creation #
######################

from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from tkinter import ttk
import json

from systems import system
from modules import auth, seatSelection

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
## Function to check if any seat is taken in the selected bus
def seat_info(): 
    busid = bus_list.focus()   ## Refer to the item selected in treeview
    buses = bus_list.item(busid, 'values')  ## Refer to the values in the item selected ('A00001', 'Cyberjaya' .... etc.)
    data = (view_json(dataDir+'busesInfo.json'))

    for i in data:
        if (i.get('bus_id')) == buses[0]:  ## Check the bus id
            letter_id = []
            if i['total_seats']== 20:
                letter_id = ["A", "B", "C", "D", "E"]  ## Seats layout according to the seats amount
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
    iter_letter = iter(letter_id) ## Iter through the element in the list
    letter = next(iter_letter)  ## Next iter item in the list

    id_list = []
    global TakenSeat
    TakenSeat = 0  ## Count how many seats are taken

    for i in data2:
        busID = i["bus_id"]
        id_list.append(busID)    ## Append the existing bus id into the list

    get_id = buses[0]
    if get_id in id_list:
        id_index = id_list.index(get_id)  ## Get the bus id when selected

    n = 0
        
    for i in button_list:
        if data2[id_index]["bus_id"] == buses[0]:
            if n < ((len(data2[id_index][letter]))): 
                if(data2[id_index][letter][n]) == False:
                    TakenSeat += 1   

            elif n == ((len(data2[id_index][letter]))): 
                n = 0
                letter = next(iter_letter)
                if(data2[id_index][letter][n]) == False:
                    TakenSeat += 1
                
            n += 1

## Function to create new bus
def create_bus():
    add_Top = Toplevel(root)  ## New window
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

    ##Call out the function
    is_up_or_down = root.register(up_or_down)  
    
    ## Confirm Bus Creation after user press Create Button
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
                float(fare.get()) ## Check if the value entered is float number
                busID = newbusID
                departure_date = date.get()
                start_town = departure_town.get()
                departure_hour = hour.get()
                departure_minute = minute.get()
                end_town = arrival_town.get()
                seats = total_seats.get()
                fee = fare.get()

                ## Append data to database
                data = (view_json(dataDir+'busesInfo.json'))                   
                data = {
                    'bus_id': busID,
                    'departure_date': departure_date,
                    'departure_time': str(departure_hour) + ':' + str(departure_minute),
                    'departure_town': start_town,
                    'arrival town': end_town,
                    'total_seats': seats,
                    'fare per seat': float(fee)
                    }
                add_json(data, dataDir+'busesInfo.json')  
                
                ## Append seat layout to database
                if seats == 20:
                    seatSelection.seat_database_20(busID)

                elif seats == 30:
                    seatSelection.seat_database_30(busID)

                elif seats == 40:
                    seatSelection.seat_database_40(busID)

                messagebox.showinfo("Successful!", "Bus created!", parent=add_Top)

                add_Top.destroy()
                admin_interface()
            
            ## Show warning if user input string or other value
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

    ## Options for bus details
    ## Date
    Label(add_Top, text="Select Departure Date", font="Helvetica 10").pack(pady=(20, 0))
    date = DateEntry(add_Top, date_pattern = 'dd/mm/yy')
    date.pack()

    ## Departure Town
    Label(add_Top, text="Select Departure Town", font="Helvetica 10").pack(pady=(20, 0))
    departure_town = OptionMenu(add_Top, station1, *stations)
    departure_town.pack()

    ## Departure Time
    Label(add_Top, text="Select Departure Time", font="Helvetica 10").pack(pady=(20, 0))
    time = Frame(add_Top, width=100, height=100)
    min_update = StringVar()
    hours = Spinbox(time, from_=0, to=23, wrap=True, state="readonly",width=2,format="%02.0f")
    minutes = Spinbox(time, from_=0, to=59, wrap=True, state="readonly",width=2, format="%02.0f", increment=10, textvariable=min_update, command=(is_up_or_down,'%d'))
    time.pack()
    hours.pack(side=LEFT)
    minutes.pack(side=LEFT)

    ## Arrival Town
    Label(add_Top, text="Select Arrival Town", font="Helvetica 10").pack(pady=(20, 0))
    arrival_town = OptionMenu(add_Top, station2, *stations)
    arrival_town.pack()
    
    ## Seats Amount
    Label(add_Top, text="Total Seats Available", font="Helvetica 10").pack(pady=(20,0))
    total_seats = OptionMenu(add_Top, seats, 20, 30, 40)
    total_seats.pack()

    ## Fare per Seat
    Label(add_Top, text="Fare per Seat (RM)", font="Helvetica 10").pack(pady=(20,0))
    fare = Entry(add_Top, font="Helvetica 10")
    fare.pack()

    add_btn = Button(add_Top, text="Create", font="Helvetica 10", bg="#000000", fg="#ffffff", padx=30, command=lambda:createBusConfirm(date, station1, hours, minutes, station2, seats, fare))
    add_btn.pack(pady=(20,0))

    cancel_btn = Button(add_Top, text="Cancel", font="Helvetica 10", bg="#000000", fg="#ffffff", padx=30, command=admin_interface)
    cancel_btn.pack(pady=10)
    
## Function to edit existing empty bus
def edit_bus():
    ## Check if admin selected a bus to edit. if not reject enter edit interface
    isEdit = False
    ## Get Item Selected from Treeview
    busid = bus_list.focus()
    buses = bus_list.item(busid, 'values')

    ## Check if there is item selected from treeview
    if busid != '':
        seat_info()
        if TakenSeat == 0:  ## Check if the bus seats are not taken
            isEdit = True
        else:
            messagebox.showwarning("Error", "This bus cannot be edit!") ## User cannot edit the non-empty bus
        
    else:
        messagebox.showwarning("Error", "Please select a bus you want to edit")

    ## Function for minutes decrement
    def up_or_down(direction):
        if direction == 'down':
            after_pressed_minutes = int(minutes.get())
            if after_pressed_minutes == 59:
                min_update.set(after_pressed_minutes - 9)
            
    is_up_or_down = root.register(up_or_down)
    
    ## Confirm to Edit Bus when user press edit button
    def editBusConfirm(date, departure_town, hour, minute, arrival_town, total_seats, fare):
        if station1.get() == station2.get():
            messagebox.showwarning("Error", "Departure Town can not be same as Arrival Town")
        elif station1.get() != station2.get() and fare.get() == "" :
            messagebox.showwarning("Error", "Please enter the fare!")
        elif fare.get() != "" and station1.get() != station2.get():
            try:
                ## Check if user enter float value
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
                        old_seats = i['total_seats']
                        i['departure_date'] = departure_date
                        i['departure_time'] = str(departure_hour) + ':' + str(departure_minute)
                        i['departure_town'] = start_town
                        i['arrival town'] = end_town
                        i['total_seats'] = seats
                        i['fare per seat'] = float(fee)
                    
                update_json(data, dataDir+'busesInfo.json') 

                data2 = (view_json(dataDir+'seatInfo.json'))

                ##Update seats layout to database
                if seats != old_seats:
                    for i in data2:
                        if i.get('bus_id') == buses[0]:
                            i.clear()
                            if seats == 20:
                                #seatSelection.edit_seat_database_20(buses[0])
                                i['bus_id'] = buses[0]
                                i['A'] = [True, True, True, True]
                                i['B'] = [True, True, True, True]
                                i['C'] = [True, True, True, True]
                                i['D'] = [True, True, True, True]
                                i['E'] = [True, True, True, True]
                            elif seats == 30:
                                i['bus_id'] = buses[0]
                                i['A'] = [True, True, True, True]
                                i['B'] = [True, True, True, True]
                                i['C'] = [True, True, True, True]
                                i['D'] = [True, True, True, True]
                                i['E'] = [True, True, True, True]
                                i['F'] = [True, True, True, True]
                                i['G'] = [True, True, True, True, True, True]
                                
                            elif seats == 40:
                                i['bus_id'] = buses[0]
                                i['A'] = [True, True, True, True]
                                i['B'] = [True, True, True, True]
                                i['C'] = [True, True, True, True]
                                i['D'] = [True, True, True, True]
                                i['E'] = [True, True, True, True]
                                i['F'] = [True, True, True, True]
                                i['G'] = [True, True, True, True]
                                i['H'] = [True, True, True, True]
                                i['I'] = [True, True, True, True]
                                i['J'] = [True, True, True, True]

                update_json(data2, dataDir+'seatInfo.json') 

                messagebox.showinfo("Successful!", "Bus edited!")
                
                admin_interface()
                
            ## Show warning if user input string
            except ValueError:
                messagebox.showwarning("Error", "Please enter number value only")

    ##Get Bus Details
    data = view_json(dataDir+'busesInfo.json')
    
    ## User can edit the bus if they select and it is empty
    if isEdit:
        clear_frame(root)

        ## Get the existing bus detail from database
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

## Function to delete bus
def delete_bus():
    ## Check if admin selected a bus to edit. if not reject enter edit interface
    isDelete = False

    ## Get Item Selected from Treeview
    bus_del = bus_list.selection()
    busid = bus_list.focus()
    buses = bus_list.item(busid, 'values')
    
    if bus_del != ():
        seat_info()
        if TakenSeat == 0:
            isDelete = True
        else:
            messagebox.showwarning("Error", "This bus cannot be delete!")
        
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

            data2 = view_json(dataDir + 'seatInfo.json')
            n = 0
            while n < len(data2):
                if (data2[n].get("bus_id")) == buses[0]:
                    data2.pop(n)
                    update_json(data2, dataDir+'seatInfo.json')
                    continue
                n += 1

            admin_interface()

## Log out funtion
def log_out():
    confirmLogout = messagebox.askquestion ('Logout Confirmation','Are you sure you want to log out from your account?',icon = 'warning')
    if confirmLogout == 'yes':
       auth.userAuth()

## Main interface
def admin_interface():
    clear_frame(root)

    bus_frame = Frame(root)
    global bus_list
    bus_list = ttk.Treeview(bus_frame, show='headings', selectmode='browse')

    bus_list['columns'] = ("Bus ID", "Departure Date", "Departure Time", "Departure Town", "Arrival Town",  "Seats Available", "Total Fare")
    bus_list.column("Bus ID", anchor=CENTER, width =50)
    bus_list.column("Departure Date", anchor=CENTER, width = 92)
    bus_list.column("Departure Time", anchor=CENTER, width = 93)
    bus_list.column("Departure Town", anchor=CENTER, width = 93)
    bus_list.column("Arrival Town", anchor=CENTER, width = 92)
    bus_list.column("Seats Available", anchor=CENTER, width = 82)
    bus_list.column("Total Fare", anchor=CENTER, width = 60)

    bus_list.heading('Bus ID', text= 'Bus ID')
    bus_list.heading('Departure Date', text='Departure Date')
    bus_list.heading('Departure Time', text='Departure Time')
    bus_list.heading('Departure Town', text='Departure Town')
    bus_list.heading('Arrival Town', text='Arrival Town')
    bus_list.heading('Seats Available', text='Seats Available')
    bus_list.heading('Total Fare', text='Fare(RM)')  

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
    data = view_json(dataDir + 'busesInfo.json')

    ##Append data to Treeview from Database
    for record in data:
        available_seats(record['bus_id'])
        fare_per_seat = ("{:.2f}".format(record['fare per seat']))
        bus_list.insert(parent='', index='end', text="", values=(
            record['bus_id'], 
            record['departure_date'], 
            record['departure_time'], 
            record['departure_town'], 
            record['arrival town'], 
            str(SeatsAvailable) + "/" +str(record['total_seats']),
            fare_per_seat
            )
        )
    
    Label(root, text="List of Buses", font="Helvetica 15 bold").pack(anchor='n', pady=(10,0), padx=(0, 150))
    
    bus_list.pack(expand=True, fill=BOTH)
    bus_frame.pack(anchor=N, side=LEFT, pady=(0, 15), padx=15, expand=True, fill=BOTH)
    
    functionframe = Frame(root)
    functionframe.pack(anchor=N, side=RIGHT, pady=10, padx=15)
    
    create_btn = Button(functionframe, text="Create Bus", command=create_bus, width=20)
    edit_btn = Button(functionframe, text="Edit Bus", command=edit_bus, width=20)
    delete_btn = Button(functionframe, text="Delete Bus", command=delete_bus, width=20)
    logout_btn = Button(functionframe, text="Log Out", command=log_out, width=20)

    create_btn.pack(pady=(30, 20))
    edit_btn.pack(pady=(0,10))
    delete_btn.pack(pady=10)
    logout_btn.pack(pady=80)