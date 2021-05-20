from estimators.estimators import Estimators
from Data.Jeu_de_donnees import Jeu_de_donnees

class Moyenne(Estimators):
    def __init__(self, index_variable):
        self.index_variable = index_variable

    def fit(self, Table):
        somme = 0
        for liste in Table.rows:
            somme += float(liste[self.index_variable])
        return somme/len(Table.rows)

