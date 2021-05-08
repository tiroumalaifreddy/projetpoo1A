import copy
import random

from estimators.estimators import Estimators
from Data.Jeu_de_donnees import Jeu_de_donnees
from estimators.moyenne import Moyenne
from estimators.ecart_type import Ecart_type
import numpy as np


class Kmeans(Estimators):
    def fit(self, Table, k, nstart):
        X = np.array(Table.rows)
        liste_index_random = random.sample(range(0, len(X)), k)
        centers = []
        for index in liste_index_random:
            centers.append(X[index])
        centers = np.array(centers)
        euc_dist = np.zeros((len(X), k))
        for i in range(k):
            euc_dist[:, i] = np.linalg.norm(X - centers[i], axis=1)
        clusters = np.argmin(euc_dist, axis=1)
        for indice in range(nstart):
            centers = []
            for i in range(k):
                liste_temp = X[clusters==i]
                liste_mean = []
                for c in range(liste_temp.shape[1]):
                    column = liste_temp[:,c]
                    somme = 0
                    for elt in column:
                        somme += elt
                    liste_mean.append(somme/len(liste_temp))
                centers.append(liste_mean)
            centers = np.array(centers)
            euc_dist = np.zeros((len(X), k))
            for i in range(k):
                euc_dist[:, i] = np.linalg.norm(X - centers[i], axis=1)
            clusters = np.argmin(euc_dist, axis=1)
        return clusters


































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






