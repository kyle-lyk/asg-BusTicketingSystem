#####################
#                   #
# PSP0201 - Group 4 #
#                   #
#####################


### System Initiation
## Import root from systems initiation
from systems import system, stor_init, pip_init
root = system.root

## Python Module Initiation
pip_init.pip_init()

## Storage Initiation
stor_init.storageInit()

### Authentication
from modules import auth
auth.userAuth()



### Tkinter Loop
root.mainloop()
