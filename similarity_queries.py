from gensim import corpora, models, similarities

dictionary = corpora.Dictionary.load('/tmp/am_lit_dict.dict')
corpus = corpora.MmCorpus('/tmp/am_lit_corpus.mm')
# print(corpus)

lsi = models.LsiModel.load('/tmp/early_am_model.lsi')
print(lsi)

pynch_bow = corpora.MmCorpus('/tmp/pynchon_vectors.mm')
pynch_lsi = lsi[pynch_bow] # convert the query to LSI space
print(pynch_lsi)

index = similarities.MatrixSimilarity(lsi[corpus]) # transform corpus to LSI space and index it
print(index)
index.save('/tmp/early_am.index')

sims = index[pynch_lsi] # perform a similarity query against the corpus
sims = sorted(enumerate(sims))
print(sims) # print (document_number, document_similarity) 2-tuples
