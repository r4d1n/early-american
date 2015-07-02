import logging
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

import codecs # for dealing with unicode

import nltk
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures

from textblob import TextBlob

import itertools
import numpy as np

import gensim
from gensim.utils import smart_open, simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

import util

class LitCorpus(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for text in util.iter_corpus(self.dirname):
            # tokenize each work
            yield util.tokenize(text)



tokenized_corpus = LitCorpus('./corpus')
# tokens = list(itertools.islice(tokenized_corpus, 10, None))
tokens = tokenized_corpus
print tokenized_corpus
# print list(tokenized_corpus)
#
dictionary = gensim.corpora.Dictionary(tokens)
dictionary.filter_extremes(no_below=5)
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(once_ids) # remove stop words and words that appear only once
dictionary.compactify() # remove gaps in id sequence after words that were removed
print dictionary
bow = [dictionary.doc2bow(doc) for doc in tokens]
dictionary.save('/tmp/am_lit_dict.dict')
gensim.corpora.MmCorpus.serialize('/tmp/am_lit_corpus.mm', bow)
# # print bow
