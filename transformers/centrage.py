from estimators.moyenne import Moyenne

M=Moyenne()

class Centrage():
    def centrage(self, data):
        new_data = []
        for liste in data[1:]:
            l = []
            for i in range(len(liste)):
                l.append(float(liste[i])- M.moyenne(data, data[0][i]))
            new_data.append(l)
        return new_data
