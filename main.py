#####################
#                   #
# PSP0201 - Group 4 #
#                   #
#####################

### IMPORT MODULES
from modules import auth
from systems import system, init

## Import root from system.py 
root = system.root

### Init Functions
## Authentication
auth.userAuth()

## Storage Initiation
init.storageInit()


### Tkinter Loop
root.mainloop()
