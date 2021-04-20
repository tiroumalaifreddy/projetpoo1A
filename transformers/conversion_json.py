import json
import transformers

class Conversion_json():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename

    def conversion_en_json(self):
        with open(self.folder + self.filename) as json_file :
            data = json.load(json_file)
        return data


