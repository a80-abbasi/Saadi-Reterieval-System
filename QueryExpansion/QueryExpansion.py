from PreProcess.PreProcess import pre_process
from PreProcess.PreProcess import bi_sent_pre_process
from Utils.Utils import all_data
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from parsivar import SpellCheck


class QueryExpansion:
    def __init__(self):
        self.processed_data = pre_process(all_data)
        self.processed_data = [' '.join(x) for x in self.processed_data]
        self.vectorizer = CountVectorizer(analyzer=lambda x: bi_sent_pre_process(x, remove_stopwords=True),
                                          ngram_range=(2, 2))
        x = self.vectorizer.fit_transform(self.processed_data)
        self.bi_counter = x.toarray()
        self.bi_counter = np.sum(self.bi_counter, axis=0)
        ind = np.unravel_index(np.argmax(self.bi_counter, axis=None), self.bi_counter.shape)
        self.vectorizer.get_feature_names()

    def suggest(self, query):
        bi_words = self.vectorizer.get_feature_names()
        max_count = 0
        best_word = ''
        for i in range(len(bi_words)):
            if bi_words[i].split()[0] == query:
                if self.bi_counter[i] > max_count:
                    best_word = bi_words[i].split()[1]
                    max_count = self.bi_counter[i]
        return best_word

    def correct_spell_error(self, query):
        my_checker = SpellCheck()
        return my_checker.spell_corrector(query)