import json

def add_json(new_data,filename):
    with open (filename,"r") as f:
        temp = json.load(f)
        temp.append(new_data)
    with open (filename,"w") as f:
        json.dump(temp, f, indent = 4)

def view_json():
    with open (filename,"r") as f:
        temp = json.load(f)

dataDir = './data/'

def register():
    username = input('username:')
    password = input('password:')
    data = {
        'username': username,
        'password': password
        }
    add_json(data, dataDir+'userAcc.json')    



