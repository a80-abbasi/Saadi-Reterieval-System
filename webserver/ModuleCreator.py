import os.path
import pickle

from webserver.Boolean import Boolean
from webserver.Clustering import Clustering
from webserver.LinkAnalysis import LinkAnalysis
from webserver.TFIDF import TFIDF

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

