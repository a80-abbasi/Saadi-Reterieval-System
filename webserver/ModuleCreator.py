import os.path
import numpy as np

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
        return np.load(path)
    else:
        return Boolean(Golestan, poem_based)


def get_tfidf(Golestan=False, poem_based=False):
    name = 'tfidf'
    if Golestan:
        name += '_Golestan'
    if poem_based:
        name += '_poem_based'
    name += '.npy'
    path = resources_path + name
    if os.path.isfile(path):
        return np.load(path)
    else:
        return TFIDF(Golestan, poem_based)


def get_clustering(poem_based=False):
    name = 'tfidf'
    if poem_based:
        name += '_poem_based'
    name += '.npy'
    path = resources_path + name
    if os.path.isfile(path):
        return np.load(path)
    else:
        return TFIDF(Golestan, poem_based)
