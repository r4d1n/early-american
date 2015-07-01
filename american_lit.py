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

class LitCorpus(object):
    def __init__(self, fname):
        self.fname = fname

    def __iter__(self):
        for text in util.iter_corpus(self.fname):
            # tokenize each message; simply lowercase & match alphabetic chars, for now
            yield self.tokenize(text)
            # yield self.lemmatize(text)

    def lemmatize(self, text):
        """Break text into a list of lemmatized words."""
        return gensim.utils.lemmatize(text)

    def tokenize(self, text):
        return [token for token in simple_preprocess(text) if token not in STOPWORDS]


tokenized_corpus = LitCorpus('./corpus')
print(list(itertools.islice(tokenized_corpus, 2)))
