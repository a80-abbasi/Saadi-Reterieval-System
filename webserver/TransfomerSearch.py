import sentence_transformers as st
from Utils import all_data
from Utils import boostan_data
import numpy as np
from PreProcess import pre_process, sent_pre_process
import itertools


class my_transformer:
    def __init__(self, Golestan=False):
        if Golestan:
            self.data = all_data
        else:
            self.data = boostan_data['poem']
        self.x = st.models.Transformer('HooshvareLab/bert-fa-zwnj-base')
        self.model = st.SentenceTransformer(modules=[self.x, st.models.Pooling(self.x.get_word_embedding_dimension())])
        self.processed_data = pre_process(self.data, remove_stopwords=True, put_index=True, MIN_COUNT=0)
        self.processed_data_index = [(' '.join(x[0]), x[1]) for x in self.processed_data]
        self.processed_data = [' '.join(x[0]) for x in self.processed_data]
        self.vectors = self.model.encode(self.processed_data)

    def search(self, query, k=10):
        pre_processed_query = sent_pre_process(query, remove_stopwords=True)
        joint_processed_query = ' '.join(pre_processed_query)
        query_encode = self.model.encode(joint_processed_query)
        sims = st.util.cos_sim(query_encode, self.vectors).numpy()[0]
        indexes = np.argsort(sims)[::-1][:k]
        tops = list()
        for ind in indexes:
            # tops.append((sims[ind], self.data[self.processed_data_index[ind][1]]))
            tops.append(self.data[self.processed_data_index[ind][1]])
        return tops
