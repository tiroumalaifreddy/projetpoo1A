import csv


class Conversion_CSV():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename

    def conversion_en_csv(self):
        data = []
        with open(self.folder + self.filename, encoding='ISO-8859-1') as csvfile:
            covidreader = csv.reader(csvfile, delimiter=';')
            for row in covidreader:
                data.append(row)
        return data

