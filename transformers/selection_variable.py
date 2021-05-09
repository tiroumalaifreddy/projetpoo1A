from transformers.transformers import Transformers
from Data.Jeu_de_donnees import Jeu_de_donnees

class Selection_variable(Transformers):
    def __init__(self, liste_variable):
        self.liste_variable = liste_variable


    def transform(self, Table):
        new_rows = [[row[Table.column_names.index(self.liste_variable[0])]] for row in Table.rows]
        for variable in self.liste_variable[1:]:
            for i in range(len(new_rows)):
                new_rows[i] = new_rows[i]+ [[row[Table.column_names.index(variable)]] for row in Table.rows][i]
        data = [self.liste_variable] + new_rows
        new_jeu = Jeu_de_donnees(data)
        return new_jeu


