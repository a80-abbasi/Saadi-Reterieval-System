import numpy as np
from PreProcess import sent_pre_process
from Utils import boostan_data, beit_based_all, poem_based_boostan, poem_based_all
from sklearn.feature_extraction.text import CountVectorizer


class Boolean:
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

        self.tf = CountVectorizer(analyzer=self._analyzer)
        bool_data = self.tf.fit_transform(self.data['poem'])
        self.bool_data = bool_data.toarray().astype(bool)

    def _analyzer(self, x):
        return sent_pre_process(x, remove_stopwords=True)

    def get_vectors(self):
        return self.bool_data

    def search(self, query, k=10):
        query_bool = self.tf.transform([query]).toarray()[0]#.astype(bool)
        scores = np.dot(self.bool_data, query_bool)  # their inner products
        args = np.argsort(scores)[::-1]
        k_args = args[:k]
        return self.data.poem.to_numpy()[k_args]