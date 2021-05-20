from Data.Jeu_de_donnees import Jeu_de_donnees
from estimators.estimators import Estimators
from estimators.moyenne import Moyenne



class Ecart_type(Estimators):


    def __init__(self, index_variable):
        self.index_variable = index_variable

    def fit(self, Table):
        et = 0
        for liste in Table.rows:
            et += (float(liste[self.index_variable]) - Moyenne(self.index_variable).fit(Table))**2
        return (et/(len(Table.rows)-1))**(0.5)



