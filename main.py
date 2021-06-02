#####################
#                   #
# PSP0201 - Group 4 #
#                   #
#####################


### System Initiation
from systems import system, stor_init, pip_init
## Import root from systems initiation
root = system.root
## Python Module Initiation
pip_init.pip_init()
## Storage Initiation
stor_init.storageInit()


### Calling modules
from modules import auth
## Authentication Page
auth.userAuth()


### Tkinter Loop
root.mainloop()
