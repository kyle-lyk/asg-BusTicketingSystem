###################
# TICKET HISTORY #
##################

### IMPORT MODULES
from tkinter import *
from tkinter import ttk
from tkcalendar import *

## Import root from system.py 
root = Tk()
root.title('Ticket History')
root.geometry('720x510')


### Frame Layout
treeframe = Frame(root)
functionframe = Frame(root)

### Treeview List 
properties = ['Bus ID','Departure Town','Arrival Town','Departure Time','Selected Seat','Total Fare']
my_tree = ttk.Treeview(treeframe, show='headings')
my_tree['columns']= properties


## Define Columns
my_tree.column('Bus ID',width=80)
my_tree.column('Departure Town',width=80)
my_tree.column('Arrival Town',width=80)
my_tree.column('Departure Time',width=80)
my_tree.column('Selected Seat',width=80)
my_tree.column('Total Fare',width=80)


## Define Headings  
my_tree.heading('Bus ID', text= 'Bus ID')
my_tree.heading('Departure Town', text='Departure\nTown')
my_tree.heading('Arrival Town', text='Arrival\nTown')
my_tree.heading('Departure Time', text='Departure\nTime')
my_tree.heading('Selected Seat', text='Selected\nSeat')
my_tree.heading('Total Fare', text='Total\nFare')


####### WIDGETS #######
### Dates
date = Label(functionframe, text='Select Departure Date').pack(pady=(20, 0))
dateEntry = DateEntry(functionframe, width = 10).pack()

### Location
stations = ["Tamarind Square, Cyberjaya", "Sunway, Kuala Lumpur", "Alor Gajah, Malacca", "Skudai, Johor", "Butterworth, Penang"]

DepatureTown = StringVar()
DepatureTown.set("All") 

ArrivalTown = StringVar()
ArrivalTown.set("All") 


DT_Label = Label(functionframe, text='Select Depature Town').pack(pady=(20, 0))
DT_OptionMenu = OptionMenu(functionframe, DepatureTown, *stations)
DT_OptionMenu.pack()

AT_Label = Label(functionframe, text='Select Arrival Town').pack(pady=(20, 0))
AT_OptionMenu = OptionMenu(functionframe, ArrivalTown, *stations)
AT_OptionMenu.pack()

SB_Button = Button(functionframe, text="Search",fg="white", bg="black",justify=CENTER,width=10)
SB_Button.pack(pady=(20, 0))

CB_Button = Button(functionframe, text='Cancel',fg="white", bg="black",justify=CENTER,width=10)
CB_Button.pack(pady=(10, 0))

BS_Button = Button(functionframe, width=20, text="Return to Bus Selection")
BS_Button.pack(pady=(50, 0))
AS_Button = Button(functionframe, width=20, text="Account Settings")
AS_Button.pack(pady=(80, 0))


### Frame Packing
my_tree.pack(expand=True, fill=BOTH)
treeframe.pack(anchor=N, side=LEFT, pady=20, padx=20, expand=True, fill=BOTH)
functionframe.pack(anchor=N, side=RIGHT, pady=20, padx=20)



#######################
### Disable resizing tree column
def handle_click(event):
    if my_tree.identify_region(event.x, event.y) == "separator":
        return "break"


my_tree.bind('<Button-1>', handle_click)


root.mainloop()