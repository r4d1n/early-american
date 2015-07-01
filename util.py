import io
import re
import fileinput
# to read each line from each file in a dir
# for line in fileinput.input(file):

import codecs # for dealing with unicode
import gensim

# def read_dir:


def preprocess_text(path_prefix, file):
    path = path_prefix + file
    start_re = re.compile(r'\*\*\*.+\*\*\*')
    end_re = re.compile(r'End\sof\sProject\sGutenberg', re.IGNORECASE)
    blocks = []
    go = False
    finput = fileinput.FileInput(path)
    for line in finput:
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
    out = stripped_text
    writeable.write(out)
    writeable.close()
        # # writeable.write(stripped_text.encode('utf-8').strip())

def make_tokens(file_list):
    def tokenize(text):
        return [token for token in simple_preprocess(text) if token not in STOPWORDS]
    tokens = []
    for path in file_list:
        graphs = preprocess_text(path)
        for n in graphs:
            tokens.append(tokenize(n))
    return tokens
