from gensim.models import Word2Vec
import itertools

def get_all_words(document):
    all_words = {}
    for line in pre_process(document['poem'], remove_stopwords=True):
        for w in line:
            if w not in all_words:
                all_words[w] = 0
            all_words[w] += 1
    return all_words

