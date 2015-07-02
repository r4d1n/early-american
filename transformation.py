import logging
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO

from gensim import corpora, models, similarities

dictionary = corpora.Dictionary.load('/tmp/am_lit_dict.dict')
corpus = corpora.MmCorpus('/tmp/am_lit_corpus.mm')
print(corpus)


# lda_model = gensim.models.LdaModel(bow, num_topics=20, id2word=dictionary, passes=20)
# _ = lda_model.print_topics(-1)  # print a few most important words for each LDA topic
# gensim.corpora.MmCorpus.serialize('./corpus_lda.mm', lda_model[bow])

# vector_bow = gensim.corpora.Mmcorpus.load('./corpus_lda.mm')

# pynch_file = open('../pynchon_gr.txt')
# pynch_text = pynch_file.read()
# pynch_tokens = util.tokenize(pynch_text)
# pynch_bow = dictionary.doc2bow(util.tokenize(pynch_text))
# print([(dictionary[id], count) for id, count in bow])
# transform into LDA space
# lda_vector = lda_model[bow]
# print lda_model.show_topics()

# vec_bow = dictionary.doc2bow(pynch_tokens)
# vec_lsi = lsi[vec_bow] # convert the query to LSI space
# print(vec_lsi)

 #construct the tf-idf model
# corpus_tfidf = tfidf_model[bow]   # first transform each raw bow vector in the corpus to the tfidf model's vector space
# index = gensim.similarities.MatrixSimilarity(corpus_tfidf)  # construct the term-document index
# sims = index[bow]
# print(list(enumerate(sims)))

# print similarityModel
