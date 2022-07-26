import os.path
import pickle

from Boolean import Boolean
from TFIDF import TFIDF
from Embedding import my_word2vec
from TransfomerSearch import my_transformer
from Clustering import Clustering
from LinkAnalysis import LinkAnalysis
from QueryExpansion import QueryExpansion
from Classification import Classification

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
        return boolean


def get_clustering(poem_based=False):
    name = 'clustring'
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
    name = 'query_expansion'
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


def get_classification():
    name = 'classification.pickle'
    path = resources_path + name
    if os.path.isfile(path):
        pickle_in = open(path, 'rb')
        return pickle.load(pickle_in)
    else:
        classification = Classification()
        pickle_out = open(path, 'wb')
        pickle.dump(classification, pickle_out)
        return classification
