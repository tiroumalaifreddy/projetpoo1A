import csv
import json


class Conversion():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename

    def convert(self, choix="Calendrier"):
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
            liste = []
            a = data[choix]
            for i in range(len(a)):
                cle = []
                valeur = []
                for key, value in a[i].items():
                    valeur.append(value)
                    if not key in cle:
                        cle.append(key)
                liste += [valeur]
            liste.insert(0, cle)
            return liste
        else:
            return "Erreur : Seuls les fichiers .csv et .json sont acceptés"
