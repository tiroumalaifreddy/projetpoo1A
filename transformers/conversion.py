import csv
import json


class Conversion():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename

    def convert(self):
        if self.filename[-4:] == ".csv":
            data = []
            with open(self.folder + self.filename, encoding='ISO-8859-1') as csvfile:
                covidreader = csv.reader(csvfile, delimiter=';')
                for row in covidreader:
                    data.append(row)
            return data
        if self.filename[-5:] == ".json":
            with open(self.folder + self.filename) as json_file:
                data = json.load(json_file)
            return data
        else:
            return "Erreur : Seuls les fichiers .csv et .json sont acceptés"

