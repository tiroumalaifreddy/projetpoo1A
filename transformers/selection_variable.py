from transformers.transformers import Transformers
from Data.Jeu_de_donnees import Jeu_de_donnees

class Selection_variable(Transformers):

    # def select_une_var(self, variable):
    #     return [[row[self.data[0].index(variable)]] for row in self.data]

    def transform(self, Table, liste_variable):
        new_rows = [[row[Table.column_names.index(liste_variable[0])]] for row in Table.rows]
        for variable in liste_variable[1:]:
            for i in range(len(new_rows)):
                new_rows[i] = new_rows[i]+ [[row[Table.column_names.index(variable)]] for row in Table.rows][i]

        data = [liste_variable] + new_rows
        new_jeu = Jeu_de_donnees(data)
        return new_jeu


