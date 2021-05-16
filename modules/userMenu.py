###################
# BUS SELECTION #
##################

### IMPORT MODULES
from tkinter import *
from tkinter import ttk
from tkcalendar import *

## Import root from system.py 
root = Tk()
root.title('Bus Selection')
root.geometry('740x550')

### Frame Layout
treeframe = Frame(root)
functionframe = Frame(root)

### Function
def show_selected():
    for child in my_tree.get_children():
        print(my_tree.item(child)["values"])

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



## Define Headings  
my_tree.heading('Bus ID', text= 'Bus ID')
my_tree.heading('Departure Date', text='Departure Date')
my_tree.heading('Departure Time', text='Departure Time')
my_tree.heading('Departure Town', text='Departure Town')
my_tree.heading('Arrival Town', text='Arrival Town')
my_tree.heading('Total Seat', text='Seat Available')
my_tree.heading('Fare/Seat', text='Fare/Seat')


## Define Rows
my_tree.insert(parent="", index="end", iid=0, text="", values=("A0001","27/2/2020","0020","TestTown", "TestTown", 30, "2" ))

####### WIDGETS #######
### Dates
date = Label(functionframe, text= 'Departure Date').pack(pady=(20, 0))
dateEntry = DateEntry(functionframe, width = 10).pack()

### Location
stations = ["Ketereh,KLT", "Cyberjaya,SLG", "Ipoh,PRK", "Skudai,JHR", "Jawi,PNG"]

DepatureTown = StringVar()
DepatureTown.set(stations[0]) 

ArrivalTown = StringVar()
ArrivalTown.set(stations[1])

DT_Label = Label(functionframe, text='Depature Town').pack(pady=(20, 0))
DT_OptionMenu = OptionMenu(functionframe, DepatureTown, *stations)
DT_OptionMenu.pack()

AT_Label = Label(functionframe, text='Arrival Town').pack(pady=(20, 0))
AT_OptionMenu = OptionMenu(functionframe, ArrivalTown, *stations)
AT_OptionMenu.pack()

SB_Button = Button(functionframe, text="Search",fg="white", bg="black",justify=CENTER,width=20)
SB_Button.pack(pady=(20, 0))

PB_Button = Button(functionframe, text="Proceed",fg="white", bg="black",justify=CENTER,width=20, command=show_selected)
PB_Button.pack(pady=(20, 0))

TS_Button = Button(functionframe, width=20, text="Ticket History")
TS_Button.pack(pady=(60, 0))

AS_Button = Button(functionframe, width=20, text="Account Settings")
AS_Button.pack(pady=(40, 0))


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