from os import system
from json import dumps
system("cls")

users=[]

names=open("names.txt","r")
malumot =names.read().split("\n")

for odam in malumot:
    odam=odam.split(",")

    user={
    'name': odam[0],
    'surname': odam[1],
    'gender': odam[2],
    'age': int(odam[3]),
    'place': odam[4]
    }
    if user['gender']=='Male':
     users.append(user)

users.sort(key=lambda user: user['gender'])

print(dumps(users, indent=4))
print(users[0])

names.close()