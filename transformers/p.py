import csv


data = []
with open("C:/Users/Freddy/projetpoo1A/departments_regions_france_2016.csv", encoding='ISO-8859-1') as csvfile:
    covidreader = csv.reader(csvfile, delimiter=',')
    for row in covidreader:
        data.append(row[0::2])

