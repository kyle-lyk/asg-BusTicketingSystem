###########################
# TKINTER SYSTEM SETTINGS #
###########################

### IMPORT MODULES
from tkinter import *
from tkinter import ttk

### Tkinter Root Settings
root = Tk()
root.title("TriBus Ticketing System")
root.iconbitmap("./img/bus_icon.ico")
root.resizable(False, False)

## Treeview Style
style = ttk.Style()
style.theme_use("default")

## Geometry
WIDTH = '740'
HEIGHT = '550'
root.geometry(WIDTH + 'x' + HEIGHT)