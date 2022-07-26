import random
import numpy as np
from TFIDF import TFIDF
from scipy.spatial.distance import cdist  # used to get distance matrix


def get_distance_matrix(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return cdist(x, y, 'euclidean') ** 2


class K_means:

    def __init__(self, data: np.ndarray, number_of_clusters):
        self.data: np.ndarray = data
        self.number_of_clusters = number_of_clusters
        self.n, self.d = data.shape  # number of data points and feature size
        self.centers: np.ndarray = None  # set when fit is called
        self.predictions: np.ndarray = None  # set when fit is called

    def kmeans_plus_plus(self):
        centers = np.zeros((self.number_of_clusters, self.d))
        centers[0] = random.choice(self.data)
        for i in range(1, self.number_of_clusters):
            centers[i] = \
            random.choices(self.data, weights=np.amin(get_distance_matrix(centers[:i], self.data), axis=0))[0]
        return centers

    def fit(self, max_number_of_iteration):
        predictions = None
        centers = self.kmeans_plus_plus()
        for i in range(max_number_of_iteration):
            predictions = get_distance_matrix(centers, self.data).argmin(axis=0)
            prev_centers = centers.copy()
            for j in range(self.number_of_clusters):
                cluster_j = self.data[predictions == j]
                if len(cluster_j) > 0:
                    centers[j] = cluster_j.mean(axis=0)

            if (prev_centers == centers).all():
                break

        self.centers = centers
        self.predictions = predictions
        return self.centers, self.predictions

    def get_distortion(self):  # aka: RSS
        return np.amin(get_distance_matrix(self.centers, self.data), axis=0).sum()

    def get_purity(self, labels):
        assert self.n == len(labels), "Number of labels must be equal to number of data"
        intersection = 0
        for j in range(self.number_of_clusters):
            j_labels = labels[self.predictions == j]
            values, counts = np.unique(j_labels, return_counts=True)
            intersection += np.max(counts)
        return intersection / self.n

    def predict(self, query):
        return get_distance_matrix(self.centers, np.array([query]))[:, 0].argmin()


class Clustering:

    def __init__(self, poem_based=False):
        self.tfidf = TFIDF(False, poem_based)

        number_of_clusters = 11
        self.kmeans = K_means(self.tfidf.tfidf_data, number_of_clusters)
        self.kmeans.fit(10000)

        data = self.tfidf.data.copy()
        data['cluster'] = self.kmeans.predictions
        self.clusters = data.groupby('cluster').apply(lambda x: x['poem'].to_numpy())

    def predict_cluster(self, query):
        query_tfidf = self.tfidf.tfidf.transform([query]).toarray()[0]
        i = self.kmeans.predict(query_tfidf)
        return i, self.clusters[i]

    def get_clusters(self):
        return list(self.clusters)