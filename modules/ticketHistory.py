###################
# TICKET HISTORY #
##################

### IMPORT MODULES
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox


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


#######################################################   Interface   #################################################################

def th_interface():
    clear_frame(root)
    ### Frame Layout
    treeframe = Frame(root)
    functionframe = Frame(root)

    ### Treeview List 
    properties = ['Bus ID','Departure Date','Departure Time','Departure Town','Arrival Town','Selected Seat','Total Fare']
    my_tree = ttk.Treeview(treeframe, show='headings')
    my_tree['columns']= properties


    ## Define Columns
    my_tree.column('Bus ID',width=50)
    my_tree.column('Departure Date',width=92)
    my_tree.column('Departure Time',width=92)
    my_tree.column('Departure Town',width=92)
    my_tree.column('Arrival Town',width=92)
    my_tree.column('Selected Seat',width=80)
    my_tree.column('Total Fare',width=60)


    ## Define Headings  
    my_tree.heading('Bus ID', text= 'Bus ID')
    my_tree.heading('Departure Date', text='Departure Date')
    my_tree.heading('Departure Time', text='Departure Time')
    my_tree.heading('Departure Town', text='Departure Town')
    my_tree.heading('Arrival Town', text='Arrival Town')
    my_tree.heading('Selected Seat', text='Selected Seat')
    my_tree.heading('Total Fare', text='Total Fare')


    ####### WIDGETS #######
    ### Dates
    date = Label(functionframe, text='Departure Date').pack(pady=(20, 0))
    dateEntry = DateEntry(functionframe, width = 10).pack()

    ### Location
    stations = ["Tamarind Square, Cyberjaya", "Sunway, Kuala Lumpur", "Alor Gajah, Malacca", "Skudai, Johor", "Butterworth, Penang"]

    DepatureTown = StringVar()
    DepatureTown.set("All") 

    ArrivalTown = StringVar()
    ArrivalTown.set("All") 


    DT_Label = Label(functionframe, text='Depature Town').pack(pady=(20, 0))
    DT_OptionMenu = OptionMenu(functionframe, DepatureTown, *stations)
    DT_OptionMenu.pack()

    AT_Label = Label(functionframe, text='Arrival Town').pack(pady=(20, 0))
    AT_OptionMenu = OptionMenu(functionframe, ArrivalTown, *stations)
    AT_OptionMenu.pack()

    SB_Button = Button(functionframe, text="Search",fg="white", bg="black",justify=CENTER,width=10)
    SB_Button.pack(pady=(20, 0))


    BS_Button = Button(functionframe, width=20, text="Bus Selection", command=lambda:userMenu.user_interface())
    BS_Button.pack(pady=(80, 0))
    AS_Button = Button(functionframe, width=20, text="Account Settings")
    AS_Button.pack(pady=(80, 0))


    ### Frame Packing
    my_tree.pack(expand=True, fill=BOTH)
    treeframe.pack(anchor=N, side=LEFT, pady=20, padx=20, expand=True, fill=BOTH)
    functionframe.pack(anchor=N, side=RIGHT, pady=20, padx=20)

    ### Disable resizing tree column
    my_tree.bind('<Button-1>', handle_click)


#######################
### Disable resizing tree column
def handle_click(event):
    if my_tree.identify_region(event.x, event.y) == "separator":
        return "break"

