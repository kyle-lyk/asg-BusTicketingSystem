##########################
# PIP MODULE VALIDATION #
##########################

import pip

package = ['tkcalendar']

## Function to check if your python has needed external module in this program, if not then auto install.
def pip_validation():
    for i in package:
        try:
            __import__(i)
            print(f"Module {i} found!")

        except ImportError:
            print(f"Module {i} not found. Module has been installed.")
            pip.main(['install', i])