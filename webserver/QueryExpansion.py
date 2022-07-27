import numpy as np
from PreProcess import pre_process, sent_pre_process
from PreProcess import bi_sent_pre_process
from Utils import all_data
from parsivar import SpellCheck
from sklearn.feature_extraction.text import CountVectorizer


class QueryExpansion:
    def __init__(self):
        self.processed_data = pre_process(all_data)
        self.processed_data = [' '.join(x) for x in self.processed_data]
        self.vectorizer = CountVectorizer(analyzer=self._analyzer, ngram_range=(2, 2))
        x = self.vectorizer.fit_transform(self.processed_data)
        self.bi_counter = x.toarray()
        self.bi_counter = np.sum(self.bi_counter, axis=0)
        self.my_checker = SpellCheck()
        ind = np.unravel_index(np.argmax(self.bi_counter, axis=None), self.bi_counter.shape)
        self.vectorizer.get_feature_names()

    def _analyzer(self, x):
        return bi_sent_pre_process(x, remove_stopwords=True)

    def suggest(self, query):
        query = sent_pre_process(query)
        bi_words = self.vectorizer.get_feature_names()
        max_count = 0
        best_word = ''
        for i in range(len(bi_words)):
            if bi_words[i].split()[0] == query[-1]:
                if self.bi_counter[i] > max_count:
                    best_word = bi_words[i].split()[1]
                    max_count = self.bi_counter[i]
        return best_word

    def correct_spell_error(self, query):
        return self.my_checker.spell_corrector(query)
