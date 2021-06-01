#####################
#                   #
# PSP0201 - Group 4 #
#                   #
#####################

### IMPORT MODULES
from modules import auth
from systems import system, stor_init, pip_init

## Import root from system.py 
root = system.root

### Init Functions

## Python Module Initiation
pip_init.pip_init()

## Storage Initiation
stor_init.storageInit()

## Authentication
auth.userAuth()



### Tkinter Loop
root.mainloop()
