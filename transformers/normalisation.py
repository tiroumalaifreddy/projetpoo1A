from estimators.moyenne import Moyenne as M
from estimators.ecart_type import Ecart_type as E


class Normalisation():
    def normalisation(self,data):
        new_data = []
        for liste in data[1:]:
            l = []
            for i in range(len(liste)):
                l.append((float(liste[i]) - M().moyenne(data, data[0][i]))/E().ecart_type_corr(data, data[0][i]))
            new_data.append(l)
        return new_data