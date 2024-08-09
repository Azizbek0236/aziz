from os import system
from json import dumps
system("cls")

users=[]

names=open("languages.txt","r")
malumot =names.read().split("\n")

for odam in malumot:
    odam=odam.split(",")

    user={
    'side': odam[0],
    'number': int(odam[1]),
    'language': odam[2],
    }
    if user['number']>=1000000:
     users.append(user)

users.sort(key=lambda user: user['number'])

print(dumps(users, indent=4))
print(users[0])

names.close()