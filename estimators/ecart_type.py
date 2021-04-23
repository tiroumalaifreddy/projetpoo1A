from Data.Jeu_de_donnees import Jeu_de_donnees

from estimators.moyenne import Moyenne as M



class Ecart_type():
    def fit(self, Jeu_de_donnees, variable):
        et = 0
        index_variable = Jeu_de_donnees.column_names.index(variable)
        for liste in Jeu_de_donnees.rows:
            et += (float(liste[index_variable]) - M().fit(Jeu_de_donnees, variable))**2
        return round((et/(len(Jeu_de_donnees.rows)-1))**(0.5), 2)



