from estimators.moyenne import Moyenne
from estimators.ecart_type import Ecart_type
M=Moyenne()
E=Ecart_type()
class Normalisation():
    def normalisation(self,data):
        new_data = []
        for liste in data[1:]:
            l = []
            for i in range(len(liste)):
                l.append(float(((liste[i]) - M.moyenne(data, data[0][i]))/E.ecart_type(data)))
            new_data.append(l)
        return new_data