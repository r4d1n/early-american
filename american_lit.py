import logging
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO
import os
import sys
import re

import codecs # for dealing with unicode

import nltk
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures

import tarfile
import itertools
import numpy as np

import gensim
from gensim.utils import smart_open, simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

import fileinput

import util

# util.write_text(util.preprocess_text('./corpus/crane-red-badge.txt'), 'write')

def iter_corpus(directory):
    corpus = os.listdir(directory)
    for work in corpus:
        if not directory.endswith('/'):
            directory += '/'
        full_path = directory + work
        yield util.preprocess_text(full_path)

class LitCorpus(object):
    def __init__(self, fname):
        self.fname = fname

    def __iter__(self):
        for text in iter_corpus(self.fname):
            # tokenize each message; simply lowercase & match alphabetic chars, for now
            # yield list(gensim.utils.tokenize(text, lower=True))
            yield self.tokenize(text)

    def tokenize(self, text):
        """Break text into a list of lemmatized words."""
        return gensim.utils.lemmatize(text)

tokenized_corpus = LitCorpus('./corpus')
print(list(itertools.islice(tokenized_corpus, 2)))
