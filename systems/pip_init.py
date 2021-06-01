##########################
# PIP MODULE INITITATION #
##########################

import pip

package = ['tkcalendar']

def pip_init():
    for i in package:
        try:
            __import__(i)
            print(f"Module {i} found!")

        except ImportError:
            print(f"Module {i} not found. Module has been installed.")
            pip.main(['install', i])