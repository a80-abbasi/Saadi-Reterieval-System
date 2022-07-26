from webserver.PreProcess import sent_pre_process
from Utils.Utils import boostan_data, beit_based_all, poem_based_boostan, poem_based_all

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


class TFIDF:
    def __init__(self, Golestan=False, poem_based=False):
        if poem_based:
            if Golestan:
                self.data = poem_based_all
            else:
                self.data = poem_based_boostan
        else:
            if Golestan:
                self.data = beit_based_all
            else:
                self.data = boostan_data

        self.tfidf = TfidfVectorizer(analyzer=lambda x: sent_pre_process(x, remove_stopwords=True))
        tfidf_data = self.tfidf.fit_transform(self.data['poem'])
        self.tfidf_data = tfidf_data.toarray()

    def get_vectors(self):
        return self.tfidf_data

    def search(self, query, k=10):
        query_tfidf = self.tfidf.transform([query]).toarray()[0]
        scores = np.dot(self.tfidf_data, query_tfidf)  # their inner products
        args = np.argsort(scores)[::-1]
        k_args = args[:k]
        return self.data.poem.to_numpy()[k_args]