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

# read each line from each file in a dir
import fileinput
    # for line in fileinput.input(file):


def preprocess_text(file):
    start_re = re.compile(r'\*\*\*.+\*\*\*')
    end_re = re.compile()
    blocks = []
    start = false
    for line in fileinput.input(file):
        if start:
            if !re.match('produce', line):
                text = gensim.utils.to_unicode(line, 'latin1').strip()
                blocks += text.split(u'\n\n')
            print text
        if start_re.search(line):
            start = true
        if end_re.search(line):
    return blocks

def write_text(stripped_text, filename):
    writeable = codecs.open(filename + ".txt","w", "utf-8")
    writeable.write(str(stripped_text))
    writeable.close()

# def process_message(message):
#     """
#     Preprocess a single 20newsgroups message, returning the result as
#     a unicode string.
#
#     """
#     # skip email headers (first block) and footer (last block)
#     content = u'\n\n'.join(blocks[1:])
#     return content
#
# print process_message(message)

preprocess_text('./corpus/crane-red-badge.txt')

def tokenize(text):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]
