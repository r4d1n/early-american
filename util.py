import io
import re
import fileinput
# to read each line from each file in a dir
# for line in fileinput.input(file):

import codecs # for dealing with unicode

import gensim
from gensim.utils import smart_open, simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

# def read_dir:


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


def tokenize(text):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]
