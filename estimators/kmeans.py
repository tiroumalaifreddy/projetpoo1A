from estimators.estimators import Estimators
from Data.Jeu_de_donnees import Jeu_de_donnees
from estimators.moyenne import Moyenne
from estimators.ecart_type import Ecart_type


class Kmeans(Estimators):
    def fit(self, Table, k, nstart):
        X <- Table.rows
        n = len(X)
        c = len(Table.column_names)
        moyenne = []
        ecarttype = []
        for index_variable in range(len(Table.column_names)):
            moyenne.append(Moyenne().fit(Table, index_variable))
            ecarttype.append(Ecart_type().fit(Table, index_variable))



