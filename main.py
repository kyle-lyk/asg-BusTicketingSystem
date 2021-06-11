#####################
#     MAIN FILE     #
#####################


### System Initiation
from systems import system, stor_init, pip_valid
## Import root from systems initiation
root = system.root
## Python Module Initiation
pip_valid.pip_validation()
## Storage Initiation
stor_init.storageInit()


### Calling modules
from modules import auth
## Authentication Page
auth.userAuth()


### Tkinter Loop
root.mainloop()
