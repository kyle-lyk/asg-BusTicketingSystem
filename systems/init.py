#######################
# STORAGE INITITATION #
#######################

import os
import json

def storageInit():
    path = './data/'

    datalist = ['userAcc.json','adminAcc.json','busesInfo.json','seatInfo.json','ticketHistory.json']

    ### Check if data folder exists, if not create one
    is_Dir = os.path.isdir(path)
    if not is_Dir:
        os.mkdir(path)
        print("Data folder not found! Data folder has been generated.")
    else:
        print("Data folder loaded successfully.")

    ### Check if data file exists, if not create one
    for data in datalist:
        try:
            open(path + data)
        except IOError: 
            print(f"'{data}' not found! Data file has been generated.")
            file = open(path + data, "w")

            ### Init default data for all databases for easier debugging

            if data == 'userAcc.json':
                data = [
                            {
                                "username": "user1",
                                "password": "user1"
                            }
                        ]

            elif data == 'adminAcc.json': 
                data = [
                            {
                                "username": "admin1",
                                "password": "admin1"
                            },
                            {
                                "username": "admin2",
                                "password": "admin2"
                            },    
                            {
                                "username": "admin3",
                                "password": "admin3"
                            }
                        ]
            elif data == 'busesInfo.json':
                data = [
                            {
                                "bus_id": "A00001",
                                "departure_date": "30/12/21",
                                "departure_time": "00:00",
                                "departure_town": "Ketereh,KLT",
                                "arrival town": "Cyberjaya,SLG",
                                "total_seats": 20,
                                "fare per seat": 5
                            }
                        ]
            elif data == 'seatInfo.json':
                data = [
                            {
                                "bus_id": "A00001",
                                "A": [False, True, True, True],
                                "B": [True, True, True, True],
                                "C": [True, True, True, True],
                                "D": [True, True, True, True],
                                "E": [True, True, True, True]
                            }
                        ]
            elif data == 'ticketHistory.json':
                data = [
                            {
                                "user_id": "user1",
                                "bus_id": "A00001",
                                "departure_date": "30/12/21",
                                "departure_time": "00:00",
                                "departure_town": "Ketereh,KLT",
                                "arrival town": "Cyberjaya,SLG",
                                "selected_seat": "A1",
                                "total_fare": 5
                            }
                        ]




            json.dump(data, file, indent=4)
        else:
            print(f"'{data}' data file loaded successfully.")


