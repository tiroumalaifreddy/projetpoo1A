# Importing required modules

import numpy as np
from scipy.spatial.distance import cdist
from estimators.estimators import Estimators
from Data.Jeu_de_donnees import Jeu_de_donnees

class Kmean(Estimators):


# Function to implement steps given in previous section
    def fit(self, X, k, no_of_iterations):
        idx = np.random.choice(len(X), k, replace=False)
        # Randomly choosing Centroids
        centroids = X[idx, :]  # Step 1

        # finding the distance between centroids and all the data points
        distances = cdist(X, centroids, 'euclidean')  # Step 2

        # Centroid with the minimum Distance
        points = np.array([np.argmin(i) for i in distances])  # Step 3

        # Repeating the above steps for a defined number of iterations
        # Step 4
        for _ in range(no_of_iterations):
            centroids = []
            for idx in range(k):
                # Updating Centroids by taking mean of Cluster it belongs to
                temp_cent = X[points == idx].mean(axis=0)
                centroids.append(temp_cent)

            centroids = np.array(centroids)  # Updated Centroids

            distances = cdist(X, centroids, 'euclidean')
            points = np.array([np.argmin(i) for i in distances])

        return points


