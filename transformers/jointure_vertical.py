from Data.Jeu_de_donnees import Jeu_de_donnees
from transformers.transformers import Transformers

class Jointure_vertical(Transformers):
    def __init__(self, Table2):
        self.Table2 = Table2

    def transform(self, Table1):
        data_fusion = [Table1.column_names + self.Table2.column_names]
        for i in range(min(len(Table1.rows), len(self.Table2.rows))):
            data_fusion.append(Table1.rows[i] + self.Table2.rows[i])
        return Jeu_de_donnees(data_fusion)