from gensim.models import Word2Vec
from Utils import all_data
from Utils import boostan_data
from PreProcess import pre_process, sent_pre_process
import numpy as np
import pandas as pd
from Utils import get_cosine
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


def get_all_words(document):
    all_words = {}
    for line in pre_process(document['poem'], remove_stopwords=True):
        for w in line:
            if w not in all_words:
                all_words[w] = 0
            all_words[w] += 1
    return all_words


class my_word2vec:
    def __init__(self, Golestan=False):
        if Golestan:
            self.data = all_data
        else:
            self.data = boostan_data['poem']

        self.tf = CountVectorizer(analyzer=self._analyzer)
        self.tf_data = self.tf.fit_transform(self.data)
        self.tf_data = self.tf_data.toarray().astype(bool)
        self.idf = TfidfTransformer(smooth_idf=True, use_idf=True)
        self.idf.fit(self.tf_data);
        self.idf_data = self.idf.idf_
        self.idf_dataframe = pd.Series(self.idf_data, index=self.tf.get_feature_names())
        self.idf_dataframe.head()
        x = pre_process(self.data, remove_stopwords=True)
        self.model = Word2Vec(x)

    def _analyzer(self, x):
        return sent_pre_process(x, remove_stopwords=True)

    def get_most_similar_word_to_word(self, word):
        return self.model.wv.most_similar(word)

    def get_similarity(self, query, line):
        pre_processed_query = sent_pre_process(query, remove_stopwords=True)
        pre_processed_line = sent_pre_process(line, remove_stopwords=True)
        query_vector = self.word_summation(pre_processed_query)
        line_vector = self.word_summation(pre_processed_line)
        return get_cosine(query_vector, line_vector)

    def word_summation(self, sent):
        vector = np.zeros(self.model.wv.vector_size, dtype=np.float64)
        weight_sum = 0
        for word in sent:
            try:
                weight = self.idf_dataframe[word]
                vector += self.model.wv[word] * weight
                weight_sum += weight
            except:
                pass
        if weight_sum != 0:
            vector /= weight_sum
        return vector

    def search(self, query, k=10):
        tops = list()
        for line in self.data:
            similarity = self.get_similarity(query, line)
            if not np.isnan(similarity):
                tops.append([similarity, line])
        tops = np.array(tops)
        args = np.argsort(tops[:, 0])[::-1]
        return list(tops[args[:k], 1])

    def get_vec(self, doc):
        return self.model.infer_vector(pre_process(doc)[0])
