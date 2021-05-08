import copy

from estimators.estimators import Estimators
from Data.Jeu_de_donnees import Jeu_de_donnees
from estimators.moyenne import Moyenne
from estimators.ecart_type import Ecart_type
import numpy as np


class Kmeans(Estimators):
    def fit(self, Table, k, nstart):
        X = Table.rows
        X = np.array(X)
        n = len(X)
        c = len(Table.column_names)
        idx = np.random.choice(len(X), k, replace=False)
        centers = X[idx, :]
        # mean = []
        # ecarttype = []
        # for index_variable in range(len(Table.column_names)):
        #     mean.append(Moyenne().fit(Table, index_variable))
        #     ecarttype.append(Ecart_type().fit(Table, index_variable))
        # centers = []
        # for i in range(k):
        #     l_temp = []
        #     for j in range(c):
        #         l_temp.append(X[j])
        #     centers.append(l_temp)
        clusters = np.zeros(n)
        euc_dist = np.zeros((n, k))
        for indice in range(nstart):
            for i in range(k):
                euc_dist[:, i] =np.linalg.norm(X - centers[i], axis = 1)
            clusters = np.argmin(euc_dist, axis = 1)
            for i in range(k):
                for j in range(c):
                    if clusters[j] == i:
                        centers[i][j] = Moyenne().fit(Table, j)
        return clusters
        # while condition != 0:
        #     for i in range(k):
        #         euc_dist[:, i] =np.linalg.norm(X_np - centers[i], axis = 1)
        #     clusters = np.argmin(euc_dist, axis = 1)
        #     centers_old = copy.deepcopy(centers)
        #     for i in range(k):
        #         for j in range(c):
        #             if clusters[j] == i:
        #                 centers[i][j] = Moyenne().fit(Table, j)
        #     condition = np.linalg.norm(centers - centers_old)
        # return clusters































        # clusters = {}
        # centers = {}
        # for i in range(k):
        #     clusters[i] = []
        #     centers[i] = X[i]
        # condition = 1
        # while condition != 0:
        #     for liste in X:
        #         distances = []
        #         for i in range(k):
        #             distances.append(np.linalg.norm(liste - centers[i]))
        #         clusters[distances.index(min(distances))].append(liste)
        #     centers_old = copy.deepcopy(centers)
        #     for j in range(k):
        #         centers[j] = np.mean(clusters[j], axis = 0)
        #     condition = np.linalg.norm(centers - centers_old)
        # return clusters






