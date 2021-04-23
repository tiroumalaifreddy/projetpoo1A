from estimators.estimators import Estimators
from Data.Jeu_de_donnees import Jeu_de_donnees

class Moyenne(Estimators):
    def fit(self, Jeu_de_donnees, variable):
        somme = 0
        index_variable = Jeu_de_donnees.column_names.index(variable)
        for liste in Jeu_de_donnees.rows:
            somme += float(liste[index_variable])
        return round(somme/len(Jeu_de_donnees.rows),2)

