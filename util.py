import io
import re
import fileinput
import os
# to read each line from each file in a dir
# for line in fileinput.input(file):

import logging
import itertools
import codecs # for dealing with unicode

from textblob import TextBlob

from nltk.corpus import stopwords

import gensim
from gensim.utils import smart_open, simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

names = ['jim','angelo','hamilton','hugh','polly','harris','sawyer','julia','bee','morris',
'marie','michael','edith','joe','wilson','alice','pearl','duncan','frederick','lucy',
'eliza','sam','jonah','edgar','allen','poe','mark','twain',
'herman','melville', 'dickinson','benjamin','franklin','elizabeth','edwards','edward','hugo',
'dudley','sarah','augustine','betty']
further_stopwords = ['en','ain','yer','ugh','dat','dey','gwine']
further_stopwords += names
stops = set(stopwords.words('english'))
for n in further_stopwords:
    stops.add(n)

# def read_dir:

def iter_corpus(directory):
    texts = os.listdir(directory)
    processed = []
    for work in texts:
        if not directory.endswith('/'):
            directory += '/'
        full_path = directory + work
        print full_path
        processed.append(preprocess_text(full_path))
    return processed


def preprocess_text(file):
    start_re = re.compile(r'\*\*\*.+\*\*\*')
    end_re = re.compile(r'End.+Gutenberg\sEBook', re.IGNORECASE)
    blocks = []
    go = False
    finput = fileinput.FileInput(file)
    for line in finput:
        if end_re.search(line):
            content = u'\n\n'.join(blocks[1:])
            return content
        if go:
            if line and not re.match('Produce', line):
                stripped = gensim.utils.to_unicode(line, 'latin1').strip()
                blocks += stripped.split(u'\n\n')
        if start_re.search(line):
            go = True


def write_text(stripped_text, filename):
    writeable = codecs.open(filename + ".txt","w", "utf-8")
    out = stripped_text
    writeable.write(out)
    writeable.close()
        # # writeable.write(stripped_text.encode('utf-8').strip())

def lemmatize(text):
    """Break text into a list of lemmatized words."""
    return gensim.utils.lemmatize(text)

def tokenize(text):
    return [token for token in simple_preprocess(text) if token not in stops]
