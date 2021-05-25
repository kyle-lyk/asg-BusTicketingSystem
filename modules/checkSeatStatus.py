from tkinter import *
import json

root = Tk()
root.title("Seat Layout")
db_filepath = "./data/seatInfo.json"

top = Frame(root)
top.pack()
bottom = Frame(root)
bottom.pack(side=BOTTOM)

def view_json(filename):
    with open (filename,'r') as f:
        data = json.load(f)
    return data

def update_json(data, filename=db_filepath):
    with open(filename,'w') as file:
        json.dump(data, file, indent=4)

def click_button(btn):
    def select_button():
        if btn["bg"] == "SystemButtonFace":
            btn.config(bg="green", relief=SUNKEN)
        else:
            btn.config(bg="SystemButtonFace", relief=RAISED)
    return select_button


def occupied_seat(letter_id, button_list):

    with open(db_filepath) as db:
        data = json.load(db)   

    n = 0
    iter_letter = iter(letter_id)
    letter = next(iter_letter)
    id_list = []

    for i in data:
        busID = i["bus_id"]
        id_list.append(busID)

    while True:
        get_id = input("Enter bus ID: ").upper()
        if get_id in id_list:
            id_index = id_list.index(get_id)
            print("Seat layout has been successfully updated!")
            break
        else:
            print("The bus ID entered does not exist!")
            continue
    
    if get_id in id_list and data[id_index]["bus_id"] == get_id:
        for i in button_list:
            list_length = len(data[id_index][letter])
            if n < list_length:
                if data[id_index][letter][n] == False:
                    i.config(bg="#8A8A8A")
                else:
                    i["command"] = click_button(i)
            elif n == list_length:
                n = 0
                letter = next(iter_letter)
                if data[id_index][letter][n] == False:
                    i.config(bg="#8A8A8A")
                else:
                    i["command"] = click_button(i)
            n += 1


def seat_database_20(id=""):

    layout = {
        "bus_id": id,
        "A": [True, True, True, True],
        "B": [True, True, True, True],
        "C": [True, True, True, True],
        "D": [True, True, True, True],
        "E": [True, True, True, True]
    }

    with open(db_filepath) as db:
        data = json.load(db)    
        data.append(layout)
        
    update_json(data)

# def edit_seat_database_20(id):
#     data = view_json(db_filepath)
#     for i in data:
#         if i.get('bus_id') == id:
#             i.clear()
#             i["bus_id"] = id,
#             i["A"] = [True, True, True, True]
#             i["B"] = [True, True, True, True]
#             i["C"] = [True, True, True, True]
#             i["D"] = [True, True, True, True]
#             i["E"] = [True, True, True, True]
#             print(i)
        
#     update_json(data, db_filepath)

def seat_database_30(id=""):

    layout = {
        "bus_id": id,
        "A": [True, True, True, True],
        "B": [True, True, True, True],
        "C": [True, True, True, True],
        "D": [True, True, True, True],
        "E": [True, True, True, True],
        "F": [True, True, True, True],
        "G": [True, True, True, True, True, True]
    }

    with open(db_filepath) as db:
        data = json.load(db)    
        data.append(layout)
        
    update_json(data)


def seat_database_40(id=""):
    
    layout = {
        "bus_id": id,
        "A": [True, True, True, True],
        "B": [True, True, True, True],
        "C": [True, True, True, True],
        "D": [True, True, True, True],
        "E": [True, True, True, True],
        "F": [True, True, True, True],
        "G": [True, True, True, True],
        "H": [True, True, True, True],
        "I": [True, True, True, True],
        "J": [True, True, True, True],
        "K": [True, True, True, True]
    }

    with open(db_filepath) as db:
        data = json.load(db)    
        data.append(layout)
        
    update_json(data)

def seat_layout_20():
    entrance_label = Label(top, text="Entrance", borderwidth=2, relief="groove")
    entrance_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=10, pady=10)
    driver_label = Label(top, text="Driver's Seat", borderwidth=2, relief="groove")
    driver_label.grid(row=0, column=2, columnspan=2, pady=10)
    a1 = Button(top, text="A1", width=4)
    a1.grid(row=1, column=0)
    a2 = Button(top, text="A2", width=4)
    a2.grid(row=1, column=1, padx=(0, 30))
    a3 = Button(top, text="A3", width=4)
    a3.grid(row=1, column=2)
    a4 = Button(top, text="A4", width=4)
    a4.grid(row=1, column=3)
    b1 = Button(top, text="B1", width=4)
    b1.grid(row=2, column=0)
    b2 = Button(top, text="B2", width=4)
    b2.grid(row=2, column=1, padx=(0, 30))
    b3 = Button(top, text="B3", width=4)
    b3.grid(row=2, column=2)
    b4 = Button(top, text="B4", width=4)
    b4.grid(row=2, column=3)
    c1 = Button(top, text="C1", width=4)
    c1.grid(row=3, column=0)
    c2 = Button(top, text="C2", width=4)
    c2.grid(row=3, column=1, padx=(0, 30))
    c3 = Button(top, text="C3", width=4)
    c3.grid(row=3, column=2)
    c4 = Button(top, text="C4", width=4)
    c4.grid(row=3, column=3)
    exit_label = Label(top, text="Exit", borderwidth=2, relief="groove")
    exit_label.grid(row=4, column=0, columnspan=2, sticky=W, padx=10, pady=10)
    d1 = Button(top, text="D1", width=4)
    d1.grid(row=5, column=0)
    d2 = Button(top, text="D2", width=4)
    d2.grid(row=5, column=1, padx=(0, 30))
    d3 = Button(top, text="D3", width=4)
    d3.grid(row=5, column=2)
    d4 = Button(top, text="D4", width=4)
    d4.grid(row=5, column=3)
    e1 = Button(top, text="E1", width=4)
    e1.grid(row=6, column=0)
    e2 = Button(top, text="E2", width=4)
    e2.grid(row=6, column=1, padx=(0, 30))
    e3 = Button(top, text="E3", width=4)
    e3.grid(row=6, column=2)
    e4 = Button(top, text="E4", width=4)
    e4.grid(row=6, column=3)

    letter_id = ["A", "B", "C", "D", "E"]
    button_list = [a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4, e1, e2, e3, e4]

    occupied_seat(letter_id, button_list)



def seat_layout_30():
    entrance_label = Label(top, text="Entrance", borderwidth=2, relief="groove")
    entrance_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=10, pady=10)
    driver_label = Label(top, text="Driver's Seat", borderwidth=2, relief="groove")
    driver_label.grid(row=0, column=2, columnspan=2, pady=10)
    a1 = Button(top, text="A1", width=4)
    a1.grid(row=1, column=0)
    a2 = Button(top, text="A2", width=4)
    a2.grid(row=1, column=1, padx=(0, 30))
    a3 = Button(top, text="A3", width=4)
    a3.grid(row=1, column=2)
    a4 = Button(top, text="A4", width=4)
    a4.grid(row=1, column=3)
    b1 = Button(top, text="B1", width=4)
    b1.grid(row=2, column=0)
    b2 = Button(top, text="B2", width=4)
    b2.grid(row=2, column=1, padx=(0, 30))
    b3 = Button(top, text="B3", width=4)
    b3.grid(row=2, column=2)
    b4 = Button(top, text="B4", width=4)
    b4.grid(row=2, column=3)
    c1 = Button(top, text="C1", width=4)
    c1.grid(row=3, column=0)
    c2 = Button(top, text="C2", width=4)
    c2.grid(row=3, column=1, padx=(0, 30))
    c3 = Button(top, text="C3", width=4)
    c3.grid(row=3, column=2)
    c4 = Button(top, text="C4", width=4)
    c4.grid(row=3, column=3)
    d1 = Button(top, text="D1", width=4)
    d1.grid(row=4, column=0)
    d2 = Button(top, text="D2", width=4)
    d2.grid(row=4, column=1, padx=(0, 30))
    d3 = Button(top, text="D3", width=4)
    d3.grid(row=4, column=2)
    d4 = Button(top, text="D4", width=4)
    d4.grid(row=4, column=3)
    e1 = Button(top, text="E1", width=4)
    e1.grid(row=5, column=0)
    e2 = Button(top, text="E2", width=4)
    e2.grid(row=5, column=1, padx=(0, 30))
    e3 = Button(top, text="E3", width=4)
    e3.grid(row=5, column=2)
    e4 = Button(top, text="E4", width=4)
    e4.grid(row=5, column=3)
    exit_label = Label(top, text="Exit", borderwidth=2, relief="groove")
    exit_label.grid(row=6, column=0, columnspan=2, sticky=W, padx=10, pady=10)
    f1 = Button(top, text="F1", width=4)
    f1.grid(row=7, column=0)
    f2 = Button(top, text="F2", width=4)
    f2.grid(row=7, column=1, padx=(0, 30))
    f3 = Button(top, text="F3", width=4)
    f3.grid(row=7, column=2)
    f4 = Button(top, text="F4", width=4)
    f4.grid(row=7, column=3)
    g1 = Button(bottom, text="G1", width=3)
    g1.grid(row=8, column=0)
    g2 = Button(bottom, text="G2", width=3)
    g2.grid(row=8, column=1)
    g3 = Button(bottom, text="G3", width=3)
    g3.grid(row=8, column=2)
    g4 = Button(bottom, text="G4", width=3)
    g4.grid(row=8, column=3)
    g5 = Button(bottom, text="G5", width=3)
    g5.grid(row=8, column=4)
    g6 = Button(bottom, text="G6", width=3)
    g6.grid(row=8, column=5)

    letter_id = ["A", "B", "C", "D", "E", "F", "G"]
    button_list = [a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4, e1, e2, e3, e4, f1,
    f2, f3, f4, g1, g2, g3, g4, g5, g6]

    occupied_seat(letter_id, button_list)


def seat_layout_40():
    entrance_label = Label(top, text="Entrance", borderwidth=2, relief="groove")
    entrance_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=10, pady=10)
    driver_label = Label(top, text="Driver's Seat", borderwidth=2, relief="groove")
    driver_label.grid(row=0, column=2, columnspan=2, pady=10)
    a1 = Button(top, text="A1", width=4)
    a1.grid(row=1, column=0)
    a2 = Button(top, text="A2", width=4)
    a2.grid(row=1, column=1, padx=(0, 30))
    a3 = Button(top, text="A3", width=4)
    a3.grid(row=1, column=2)
    a4 = Button(top, text="A4", width=4)
    a4.grid(row=1, column=3)
    b1 = Button(top, text="B1", width=4)
    b1.grid(row=2, column=0)
    b2 = Button(top, text="B2", width=4)
    b2.grid(row=2, column=1, padx=(0, 30))
    b3 = Button(top, text="B3", width=4)
    b3.grid(row=2, column=2)
    b4 = Button(top, text="B4", width=4)
    b4.grid(row=2, column=3)
    c1 = Button(top, text="C1", width=4)
    c1.grid(row=3, column=0)
    c2 = Button(top, text="C2", width=4)
    c2.grid(row=3, column=1, padx=(0, 30))
    c3 = Button(top, text="C3", width=4)
    c3.grid(row=3, column=2)
    c4 = Button(top, text="C4", width=4)
    c4.grid(row=3, column=3)
    d1 = Button(top, text="D1", width=4)
    d1.grid(row=4, column=0)
    d2 = Button(top, text="D2", width=4)
    d2.grid(row=4, column=1, padx=(0, 30))
    d3 = Button(top, text="D3", width=4)
    d3.grid(row=4, column=2)
    d4 = Button(top, text="D4", width=4)
    d4.grid(row=4, column=3)
    e1 = Button(top, text="E1", width=4)
    e1.grid(row=5, column=0)
    e2 = Button(top, text="E2", width=4)
    e2.grid(row=5, column=1, padx=(0, 30))
    e3 = Button(top, text="E3", width=4)
    e3.grid(row=5, column=2)
    e4 = Button(top, text="E4", width=4)
    e4.grid(row=5, column=3)
    f1 = Button(top, text="F1", width=4)
    f1.grid(row=6, column=0)
    f2 = Button(top, text="F2", width=4)
    f2.grid(row=6, column=1, padx=(0, 30))
    f3 = Button(top, text="F3", width=4)
    f3.grid(row=6, column=2)
    f4 = Button(top, text="F4", width=4)
    f4.grid(row=6, column=3)
    g1 = Button(top, text="G1", width=4)
    g1.grid(row=7, column=0)
    g2 = Button(top, text="G2", width=4)
    g2.grid(row=7, column=1, padx=(0, 30))
    g3 = Button(top, text="G3", width=4)
    g3.grid(row=7, column=2)
    g4 = Button(top, text="G4", width=4)
    g4.grid(row=7, column=3)
    h1 = Button(top, text="H1", width=4)
    h1.grid(row=8, column=0)
    h2 = Button(top, text="H2", width=4)
    h2.grid(row=8, column=1, padx=(0, 30))
    h3 = Button(top, text="H3", width=4)
    h3.grid(row=8, column=2)
    h4 = Button(top, text="H4", width=4)
    h4.grid(row=8, column=3)
    exit_label = Label(top, text="Exit", borderwidth=2, relief="groove")
    exit_label.grid(row=9, column=0, columnspan=2, sticky=W, padx=10, pady=10)
    i1 = Button(top, text="I1", width=4)
    i1.grid(row=10, column=0)
    i2 = Button(top, text="I2", width=4)
    i2.grid(row=10, column=1, padx=(0, 30))
    i3 = Button(top, text="I3", width=4)
    i3.grid(row=10, column=2)
    i4 = Button(top, text="I4", width=4)
    i4.grid(row=10, column=3)
    j1 = Button(top, text="J1", width=4)
    j1.grid(row=11, column=0)
    j2 = Button(top, text="J2", width=4)
    j2.grid(row=11, column=1, padx=(0, 30))
    j3 = Button(top, text="J3", width=4)
    j3.grid(row=11, column=2)
    j4 = Button(top, text="J4", width=4)
    j4.grid(row=11, column=3)

    letter_id = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    button_list = [a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4, e1, e2, e3, e4, f1,
    f2, f3, f4, g1, g2, g3, g4, h1, h2, h3, h4, i1, i2, i3, i4, j1, j2, j3, j4]

    occupied_seat(letter_id, button_list)


# seat_database_20("insert_id") - test appending default layout to database
# seat_layout_20() - see available seats, enter bus id to check available seats



