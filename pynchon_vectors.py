import logging
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO

import codecs # for dealing with unicode

import nltk

import itertools
import numpy as np

import gensim
from gensim.utils import smart_open, simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

import util

class Pynchon(object):
    def __init__(self, filename):
        with open(filename) as file:
            self.file = file
            self.tokens = []
            for line in file:
                self.tokens.append(util.tokenize(line))

    def tokens(self):
        return self.tokens

tokenized_corpus = Pynchon('gravitys_rainbow.txt')
tokens = tokenized_corpus.tokens
# print tokens
# print list(tokenized_corpus)
# #
dictionary = gensim.corpora.Dictionary(tokens)
dictionary.filter_extremes(no_below=5)
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(once_ids) # remove stop words and words that appear only once
dictionary.compactify() # remove gaps in id sequence after words that were removed
# print dictionary
bow = [dictionary.doc2bow(doc) for doc in tokens]
# print bow
dictionary.save('/tmp/pynchon_dict.dict')
gensim.corpora.MmCorpus.serialize('/tmp/pynchon_vectors.mm', bow)
