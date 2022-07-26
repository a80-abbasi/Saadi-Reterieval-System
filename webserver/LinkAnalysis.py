import numpy as np
import networkx as nx
from TFIDF import TFIDF


class LinkAnalysis:
    def __init__(self):
        self.tfidf = TFIDF(False, False)

        similarity_matrix = np.matmul(self.tfidf.tfidf_data, self.tfidf.tfidf_data.T)
        threshold = 0.3
        adj_matrix = (similarity_matrix > threshold).astype(int)
        adj_matrix -= np.eye(len(adj_matrix), dtype=int)
        adj_graph = nx.from_numpy_array(adj_matrix)

        probabilities = nx.pagerank(adj_graph)
        self.page_rank_max_idx = sorted(probabilities, key=probabilities.get, reverse=True)

        hubs, authority = nx.hits(adj_graph)
        self.hubs_max_idx = list(sorted(authority, key=authority.get, reverse=True))

    def get_pagerank_results(self, k=10):
        return list(self.tfidf.data.poem[self.page_rank_max_idx[:k]])

    def get_authority_hubs_results(self, k=10):
        return list(self.tfidf.data.poem[self.hubs_max_idx[:k]])
