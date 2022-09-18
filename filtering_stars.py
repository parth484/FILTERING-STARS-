import csv
import pandas as pd

rows=[]
with open('Final.csv', 'r') as f:
    csv_r = csv.reader(f)
    for star in csv_r:
        rows.append(star)
headers = rows[0]
star_data = rows[1:]

names = []
distance = []
mass = []
radius = []
gravity = []
final_list = []

for star in star_data:
    if float(star[2]) < 100:
        if float(star[5]) > 150 and float(star[5]) < 350:
            final_list.append(star)
for i in final_list:
    names.append(i[1])
    distance.append(i[2])
    mass.append(i[3])
    radius.append(i[4])
    gravity.append(i[5])
df = pd.DataFrame(
    list(zip(names, distance, mass, radius, gravity)),
    columns=["Star Name", "Distance", "Mass", "Radius", "Gravity"],
)
print(df)

df.to_csv('Final.csv')
