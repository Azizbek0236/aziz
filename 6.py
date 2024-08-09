import os
os.system("cls")

with open("booking_data.txt", "r") as file:
    malumotlar = [line.strip().split(",") for line in file]

natijalar = []
for malumot in malumotlar[1:]:  
    davlat = malumot[3]
    vaqt = int(malumot[4].split(":")[0])
    
    if davlat == "US" and vaqt < 20:
        natijalar.append({
            "Name": malumot[0],
            "Location": malumot[1],
            "Date": malumot[2],
            "Country": davlat,
            "Time": malumot[4],
            "Additional Info": malumot[5:]
        })

for natija in natijalar:
    print(f"Name: {natija['Name']}, Location: {natija['Location']}, Date: {natija['Date']}, "
          f"Country: {natija['Country']}, Time: {natija['Time']}, Additional Info: {natija['Additional Info']}")
