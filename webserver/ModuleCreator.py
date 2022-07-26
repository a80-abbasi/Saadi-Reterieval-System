import os.path
import pickle

from Boolean import Boolean
from TFIDF import TFIDF
from Embedding import my_word2vec
from TransfomerSearch import my_transformer
from Clustering import Clustering
from LinkAnalysis import LinkAnalysis
from QueryExpansion import QueryExpansion

resources_path = '../resources/'


def get_boolean(Golestan=False, poem_based=False):
    name = 'boolean'
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
        boolean = Boolean(Golestan, poem_based)
        pickle_out = open(path, "wb")
        pickle.dump(boolean, pickle_out)


def get_tfidf(Golestan=False, poem_based=False):
    name = 'tfidf'
    if Golestan:
        name += '_Golestan'
    if poem_based:
        name += '_poem_based'
    name += '.npy'
    path = resources_path + name
    if os.path.isfile(path):
        pickle_in = open(path, "rb")
        return pickle.load(pickle_in)
    else:
        tfidf = TFIDF(Golestan, poem_based)
        pickle_out = open(path, "wb")
        pickle.dump(tfidf, pickle_out)
        return tfidf


def get_clustering(poem_based=False):
    name = 'tfidf'
    if poem_based:
        name += '_poem_based'
    name += '.pickle'
    path = resources_path + name
    if os.path.isfile(path):
        pickle_in = open(path, "rb")
        return pickle.load(pickle_in)
    else:
        clustering = Clustering(poem_based)
        pickle_out = open(path, "wb")
        pickle.dump(clustering, pickle_out)
        return clustering


def get_link_analysis():
    name = 'link_analysis.pickle'
    path = resources_path + name
    if os.path.isfile(path):
        pickle_in = open(path, "rb")
        return pickle.load(pickle_in)
    else:
        linkanalyser = LinkAnalysis()
        pickle_out = open(path, "wb")
        pickle.dump(linkanalyser, pickle_out)
        return linkanalyser


def get_embedding(Golestan=False):
    name = 'word2vec'
    if Golestan:
        name += '_Golestan'
    name += '.pickle'
    path = resources_path + name
    if os.path.isfile(path):
        pickle_in = open(path, "rb")
        return pickle.load(pickle_in)
    else:
        word2vec = my_word2vec(Golestan)
        pickle_out = open(path, "wb")
        pickle.dump(word2vec, pickle_out)
        return word2vec


def get_transformer(Golestan=False):
    name = 'transformer'
    if Golestan:
        name += '_Golestan'
    name += '.pickle'
    path = resources_path + name
    if os.path.isfile(path):
        pickle_in = open(path, 'rb')
        return pickle.load(pickle_in)
    else:
        transformer = my_transformer(Golestan)
        pickle_out = open(path, 'wb')
        pickle.dump(transformer, pickle_out)
        return transformer


def get_query_expansion():
    name = 'transformer'
    name += '.pickle'
    path = resources_path + name
    if os.path.isfile(path):
        pickle_in = open(path, 'rb')
        return pickle.load(pickle_in)
    else:
        query_extender = QueryExpansion()
        pickle_out = open(path, 'wb')
        pickle.dump(query_extender, pickle_out)
        return query_extender

print(get_transformer(True).search('به نام خداوند جان و خرد'))