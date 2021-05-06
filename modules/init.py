#######################
# STORAGE INITITATION #
#######################

import os
import json

def storageInit():
    path = './data/'

    datalist = ['userAcc.json','adminAcc.json','busesInfo.json','seatInfo.json','ticketHistory.json']

    ### Check if data folder exists

    is_Dir = os.path.isdir(path)
    if not is_Dir:
        os.mkdir(path)
    else:
        print("Data folder found! Loading data from it")

    ### Check if data file exists
    for data in datalist:
        try:
            open(path + data)
        except IOError: 
            ## Canf find json
            print(f"Generating {data}")
            file = open(path + data, "w")
            data =[]
            json.dump(data, file)
        else:
            print(f"{data} found! Loading data from file")

