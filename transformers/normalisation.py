from estimators.moyenne import Moyenne
from estimators.ecart_type import Ecart_type
from transformers.transformers import Transformers
from Data.Jeu_de_donnees import Jeu_de_donnees
import numpy as np

class Normalisation(Transformers):
    def transform(self, Table):
        new_data = []
        X = np.array(Table.rows)
        mean = []
        ect = []
        for i in range(len(Table.column_names)):
            mean.append(Moyenne(i).fit(Table))
            ect.append(Ecart_type(i).fit(Table))
        mean = np.array(mean)
        ect = np.array(ect)
        new_data = X - (mean/ect)
        data = [Table.column_names] + new_data.tolist()
        J = Jeu_de_donnees(data)
        return J