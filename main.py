#####################
#
# PSP0201 - Group 4
#
#####################

### IMPORT MODULES
import tkinter
from tkinter import *
import json

from modules import auth, init


### Tkinter Root Settings
root = Tk()
root.title("Bus Ticketing System")
## Geometry
WIDTH = '720'
HEIGHT = '510'
root.geometry(WIDTH + 'x' + HEIGHT)


### Calling out functions
## Authentication
auth.userAuth(root)
init.storageInit()



### Tkinter Loop
root.mainloop()