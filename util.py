import os
import sys
import re
import fileinput
# to read each line from each file in a dir
# for line in fileinput.input(file):

import codecs # for dealing with unicode
import gensim

def preprocess_text(file):
    start_re = re.compile(r'\*\*\*.+\*\*\*')
    end_re = re.compile(r'End\sof\sProject\sGutenberg', re.IGNORECASE)
    blocks = []
    go = False
    for line in fileinput.input(file):
        if end_re.search(line):
            content = u'\n\n'.join(blocks[1:])
            return content
        if go:
            if not re.match('Produce', line):
                stripped = gensim.utils.to_unicode(line, 'latin1').strip()
                blocks += stripped.split(u'\n\n')
        if start_re.search(line):
            go = True


def write_text(stripped_text, filename):
    writeable = codecs.open(filename + ".txt","w", "utf-8")
    writeable.write(str(stripped_text))
    writeable.close()

def tokenize(text):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]
