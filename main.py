#####################
#
# PSP0201 - Group 4
#
#####################

### IMPORT MODULES
import tkinter
from tkinter import *
import json

import auth


### Tkinter Root Settings
root = Tk()
root.title("Bus Ticketing System")
## Geometry
HEIGHT = '510'
WIDTH = '720'
root.geometry(WIDTH + 'x' + HEIGHT)


### Authentication
auth.authentication(root)


### Tkinter Loop
root.mainloop()