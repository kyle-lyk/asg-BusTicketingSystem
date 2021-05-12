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
    else:
        print("Data folder found! Loading data from it")

    ### Check if data file exists, if not create one
    for data in datalist:
        try:
            open(path + data)
        except IOError: 
            print(f"Generating {data}")
            file = open(path + data, "w")

            if data == 'adminAcc.json': ## Init 3 default admin accounts
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
            else:
                data =[]
            json.dump(data, file, indent=4)
        else:
            print(f"{data} found! Loading data from file")


