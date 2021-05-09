from estimators.moyenne import Moyenne
from estimators.ecart_type import Ecart_type
from transformers.transformers import Transformers
from Data.Jeu_de_donnees import Jeu_de_donnees


class Normalisation(Transformers):
    def transform(self, Table):
        new_data = []
        for liste in Table.rows:
            l = []
            for i in range(len(liste)):
                l.append(round(((float(liste[i]) - Moyenne(i).fit(Table))/(Ecart_type(i).fit(Table))),2))
            new_data.append(l)
        data = [Table.column_names] + new_data
        J = Jeu_de_donnees(data)
        return J