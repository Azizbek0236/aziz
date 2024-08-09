import os
os.system("cls")

with open("booking_data.txt", "r") as file:
    malumotlar = [line.strip().split(",") for line in file]

pul = float(input("Summani kiriting: "))

natijalar = []
for malumot in malumotlar[1:]:
    narx = float(malumot[5][1:])
    if pul - 50 < narx < pul + 100:
        natijalar.append({
            "Name": malumot[0],
            "Location": malumot[1],
            "Date": malumot[2],
            "Room Type": malumot[3],
            "Nights": malumot[4],
            "Price": narx
        })

for natija in natijalar:
    print(f"Name: {natija['Name']}, Location: {natija['Location']}, Date: {natija['Date']}, "
          f"Room Type: {natija['Room Type']}, Nights: {natija['Nights']}, Price: ${natija['Price']:.2f}")
