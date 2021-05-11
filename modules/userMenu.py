from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkcalendar import *

root = Tk()
root.title("Bus Selection")
root.geometry('350x400')

frame = Frame(root)
frame.pack()

########### BUS LIST ############

def create_bus():
    add_Top = Toplevel(root)
    add_Top.title("Bus Lists")
    HEIGHT = '600'
    WIDTH = '600'
    add_Top.geometry(WIDTH + 'x' + HEIGHT)
    
    buslist = ttk.Treeview(add_Top)

    selection = Label(add_Top,text="Bus Selection").pack(pady=20)

    buslist["columns"] = ('Bus ID', 'Seat Availible', 'Depature Time')
    
    buslist.column("Bus ID")
    buslist.column("Seat Availible")
    buslist.column("Depature Time")

    buslist.heading("Bus ID", Text="Bus ID")
    buslist.heading("Seat Availible", Text="Seat Availible")
    buslist.heading("Depature Time", Text="Depature Time")

    buslist.insert(parent="",index='end',iid=0,Text="Test", value=("1201100287", 30, "00:20"))

    buslist.pack()

    
    

####### DATE ENTRY ########
date = Label(root, text='Select Departure Date').pack(pady=20)
cal = DateEntry(root, width = 10).pack()


####### LOCATION ENTRY ########

DepatureTown = StringVar(root)
DepatureTown.set("NONE") 

ArrivalTown = StringVar(root)
ArrivalTown.set("NONE") 

SDT = Label(root, text='Select Depature Town').pack(pady=20)
DT = OptionMenu(root, DepatureTown, "KL", "US", "UK").pack()

SAT = Label(root, text='Select Arrival Town').pack(pady=20)
AT = OptionMenu(root, ArrivalTown, "AUS", "NE", "TW").pack()

SB = Button(root, text="Search",fg="white", bg="black",justify=CENTER,width=10,command=create_bus)
SB.pack(pady=20)

CB = Button(root, text='Cancel',fg="white", bg="black",justify=CENTER,width=10)
CB.pack()

########### ############




root.mainloop()