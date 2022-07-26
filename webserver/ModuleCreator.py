import os.path
import pickle

from webserver.Boolean import Boolean
from webserver.TFIDF import TFIDF

resources_path = '../resources/'


def get_boolean(Golestan=False, poem_based=False):
    name = 'boolean'
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
