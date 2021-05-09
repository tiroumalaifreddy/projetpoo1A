from Data.Jeu_de_donnees import Jeu_de_donnees
from estimators.estimators import Estimators
from estimators.moyenne import Moyenne



class Ecart_type(Estimators):


    def __init__(self, index_variable):
        self.index_variable = index_variable

    def fit(self, Jeu_de_donnees):
        et = 0
        for liste in Jeu_de_donnees.rows:
            et += (float(liste[self.index_variable]) - Moyenne(self.index_variable).fit(Jeu_de_donnees))**2
        return (et/(len(Jeu_de_donnees.rows)-1))**(0.5)



