from Data.Jeu_de_donnees import Jeu_de_donnees
from transformers.transformers import Transformers

class Jointure_vertical(Transformers):

    def transform(self, Table1, Table2):
        #if len(Table1.rows) == len(Table2.rows):
        if 0 == 0:
            data_fusion = [Table1.column_names + Table2.column_names]
            for i in range(min(len(Table1.rows), len(Table2.rows))):
                data_fusion.append(Table1.rows[i] + Table2.rows[i])
        return Jeu_de_donnees(data_fusion)