from Data.Jeu_de_donnees import Jeu_de_donnees
from transformers.transformers import Transformers
from transformers.jointure_vertical import Jointure_vertical

class Moyenne_glissante(Transformers):
    def __init__(self, n, liste_variable):
        self.n = n
        self.liste_variable = liste_variable

    def transform(self,Table):
        liste_moyenne = []
        variable = self.liste_variable[0]
        indice_variable = Table.column_names.index(variable)
        for i in range(len(Table.rows)):
            liste = Table.rows[i:self.n + i]
            if len(liste) == self.n:
                somme = 0
                for j in liste:
                    somme += float(j[indice_variable])
                liste_moyenne += [[round(somme / self.n, 2)]]
        new_column = [["M_glissante n{} de {}".format(self.n, variable)]] + liste_moyenne
        new_Table = Jeu_de_donnees(new_column)
        if len(self.liste_variable) > 1:
            for variable in self.liste_variable[1:]:
                liste_moyenne = []
                indice_variable = Table.column_names.index(variable)
                for i in range(len(Table.rows)):
                    liste = Table.rows[i:self.n + i]
                    if len(liste) == self.n:
                        somme = 0
                        for j in liste:
                            somme += float(j[indice_variable])
                        liste_moyenne += [[round(somme / self.n, 2)]]
                new_column = [["M_glissante n{} de {}".format(self.n, variable)]] + liste_moyenne
                new_Table = Jointure_vertical(Jeu_de_donnees(new_column)).transform(new_Table)
        return Jointure_vertical(new_Table).transform(Table)
