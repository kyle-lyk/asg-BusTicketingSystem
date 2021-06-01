##########################
# PIP MODULE INITITATION #
##########################

import pip

package = ['tkcalendar']

def pip_init():
    for i in package:
        try:
            import i 
            print(f"Module {i} found!")

        except ModuleNotFoundError:
            print(f"Module {i} not found. Module has been installed.")
            pip.main(['install', i])
