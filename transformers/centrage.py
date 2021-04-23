from estimators.moyenne import Moyenne
from transformers.transformers import Transformers
from Data.Jeu_de_donnees import Jeu_de_donnees

M=Moyenne()

class Centrage(Transformers):
    def transform(self, Table):
        new_data = [Table.column_names]
        for liste in Table.rows:
            l = []
            for i in range(len(liste)):
                l.append(float(liste[i])- M.fit(Table, Table.column_names[i]))
            new_data.append(l)
        return Jeu_de_donnees(new_data)
