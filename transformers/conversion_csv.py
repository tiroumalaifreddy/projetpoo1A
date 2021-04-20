import csv
import transformers

class Conversion_CSV(transformers):
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename

    def conversion_en_csv(self):
        data = []
        with open(folder + filename, encoding='ISO-8859-1') as csvfile :
            covidreader = csv.reader(csvfile, delimiter='')
            for row in covidreader :
                data.append(row)
        return data

