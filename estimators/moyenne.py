from estimators.estimators import Estimators
from Data.Jeu_de_donnees import Jeu_de_donnees

class Moyenne(Estimators):
    def fit(self, Jeu_de_donnees, index_variable):
        somme = 0
        for liste in Jeu_de_donnees.rows:
            somme += float(liste[index_variable])
        return somme/len(Jeu_de_donnees.rows)

