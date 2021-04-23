from estimators.moyenne import Moyenne as M
from estimators.ecart_type import Ecart_type as E
from transformers.transformers import Transformers
from Data.Jeu_de_donnees import Jeu_de_donnees


class Normalisation(Transformers):
    def transform(self, Table):
        new_data = []
        for liste in Table.rows:
            l = []
            for i in range(len(liste)):
                l.append(round(((float(liste[i]) - M().fit(Table, Table.column_names[i]))/E().fit(Table, Table.column_names[i])),2))
            new_data.append(l)
        data = [Table.column_names] + new_data
        J = Jeu_de_donnees(data)
        return J