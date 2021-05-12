Data = [
    {
        "username": "123",
        "password": "abc"
    },
    {
        "username": "321",
        "password": "cba"
    },
]

x = input('username')

for i in Data:

    if x == (i.get('username')):
        print('username already exists')