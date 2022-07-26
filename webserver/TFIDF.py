import pickle
import os.path
import numpy as np
from PreProcess import sent_pre_process
from sklearn.feature_extraction.text import TfidfVectorizer
from Utils import boostan_data, beit_based_all, poem_based_boostan, poem_based_all

resources_path = '../resources/'


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

        self.tfidf = TfidfVectorizer(analyzer=self._analyzer)
        tfidf_data = self.tfidf.fit_transform(self.data['poem'])
        self.tfidf_data = tfidf_data.toarray()

    def _analyzer(self, x):
        return sent_pre_process(x, remove_stopwords=True)

    def get_vectors(self):
        return self.tfidf_data

    def search(self, query, k=10):
        query_tfidf = self.tfidf.transform([query]).toarray()[0]
        scores = np.dot(self.tfidf_data, query_tfidf)  # their inner products
        args = np.argsort(scores)[::-1]
        k_args = args[:k]
        return self.data.poem.to_numpy()[k_args]


def get_tfidf(Golestan=False, poem_based=False):
    name = 'tfidf'
    if Golestan:
        name += '_Golestan'
    if poem_based:
        name += '_poem_based'
    name += '.pickle'
    path = resources_path + name
    if os.path.isfile(path):
        pickle_in = open(path, "rb")
        return pickle.load(pickle_in)
    else:
        tfidf = TFIDF(Golestan, poem_based)
        pickle_out = open(path, "wb")
        pickle.dump(tfidf, pickle_out)
        return tfidf
