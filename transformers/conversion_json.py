import json
import transformers

class Conversion_json(transformers):
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename

    def conversion_en_json(self):
        with open(folder + filename) as json_file :
            data = json.load(json_file)
        return data


