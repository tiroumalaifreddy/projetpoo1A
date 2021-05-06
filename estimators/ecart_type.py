from Data.Jeu_de_donnees import Jeu_de_donnees
from estimators.estimators import Estimators
from estimators.moyenne import Moyenne as M



class Ecart_type(Estimators):
    def fit(self, Jeu_de_donnees, index_variable):
        et = 0
        for liste in Jeu_de_donnees.rows:
            et += (float(liste[index_variable]) - M().fit(Jeu_de_donnees, index_variable))**2
        return (et/(len(Jeu_de_donnees.rows)-1))**(0.5)



