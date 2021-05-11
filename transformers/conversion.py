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
            liste_data = []
            a = data[choix]
            list_keys = []
            for key in a[0].keys():
                list_keys.append(key)
            liste_data.append(list_keys)
            list_values = []
            for i in range(len(a)):
                valeur = []
                for value in a[i].values():
                    valeur.append(value)
                list_values.append(valeur)
            liste_data += list_values
            return liste_data
        else:
            return "Erreur : Seuls les fichiers .csv et .json sont acceptés"