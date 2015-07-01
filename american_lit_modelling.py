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

import itertools
import numpy as np

import gensim
from gensim.utils import smart_open, simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

import fileinput

import util

# util.write_text(util.preprocess_text('./corpus/crane-red-badge.txt'), 'write')
corpus = os.listdir('./corpus')
for work in corpus:
    prepped = util.preprocess_text('./corpus/', work)
    if prepped:
        print prepped
        util.write_text(prepped, 'prepped')
# tokens = util.make_tokens(['./corpus/crane-red-badge.txt'])
# print tokens
