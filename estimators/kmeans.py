from estimators.estimators import Estimators
from Data.Jeu_de_donnees import Jeu_de_donnees
from sklearn.cluster import KMeans

class Kmeans(Estimators):
    def fit(self, Table, k):
        kmeans = KMeans(n_clusters = k, random_state=0).fit(Table.rows)
        return kmeans