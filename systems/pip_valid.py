'''
** ** ** ** **
Code Filename: main.py
Course: PSP0201 Mini IT Project 
Trimester: 2030
Lecture Section: TC1V
Tutorial Section: TT2V

Student Name as per MMU 1: Chua Hui Yi
Student ID 1: 1201100840
Email 1: 1201100840@student.mmu.edu.my
Phone 1: 010-7843168

Student Name as per MMU 2: Edwin Lim Cheng Yin
Student ID 2: 1201100287
Email 2: 1201100287@student.mmu.edu.my
Phone 2: 016-2152148

Student Name as per MMU 3: Lim Yuen Khai
Student ID 3: 1201100842
Email 3: 1201100842@student.mmu.edu.my
Phone 3: 011-60977732

Student Name as per MMU 4: Muhammad Haikal bin Lokman
Student ID 4: 1201100844 
Email 4: 1201100844@student.mmu.edu.my
Phone 4: 019-2580817
** ** ** ** **
'''


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