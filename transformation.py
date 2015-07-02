import logging
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

dictionary = corpora.Dictionary.load('/tmp/am_lit_dict.dict')
corpus = corpora.MmCorpus('/tmp/am_lit_corpus.mm')
print(corpus)

pynchon_vectors = corpora.MmCorpus('/tmp/pynchon_vectors.mm')

tfidf = models.TfidfModel(corpus) # initialize transformation w/ training corpus

corpus_tfidf = tfidf[corpus]
pynchon_tfidf = tfidf[pynchon_vectors] # step 2 -- use the model to transform vectors

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10) # initialize an LSI transformation
# corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi


lda = models.LdaModel(corpus, id2word=dictionary, num_topics=100, passes=10)
lda.save('/tmp/early_am_model.lda')
lda.print_topics()
# lsi.print_topics(3)
lsi.save('/tmp/early_am_model.lsi')
# pynchon_lsi.save('/tmp/pynchon_model.lsi')
