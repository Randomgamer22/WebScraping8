import pandas as pd
import csv

df = pd.read_csv('main.csv', encoding = 'UTF8')

headers = df.columns.tolist()
all_star_data = df.values.tolist()

def filter_distance():
    for index, star_data in enumerate(all_star_data):
        if star_data[2] > 100:
            del all_star_data[index]
def filter_gravity():
    for index, star_data in enumerate(all_star_data):
        if star_data[5] < 1.5 and star_data[5] > 3.5:
            del all_star_data[index]

filter_distance()
filter_gravity()

with open('main1.csv', 'a+', encoding = 'UTF8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(all_star_data)
 
