# %%
import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
import gensim
import numpy as np

class Term_Freq:
    def find_term_freq(self,query,news_art):
        file_docs = []
        flag = 0
        f = news_art
        tokens = sent_tokenize(f)
        for line in tokens:
            file_docs.append(line)
        if len(file_docs)<2:
            file_docs.append("abc")
            flag = 1
        # print("Number of documents:",len(file_docs))

        # %%
        gen_docs = [[w.lower() for w in word_tokenize(text)] 
                    for text in file_docs]

        # %%
        dictionary = gensim.corpora.Dictionary(gen_docs)
        # print(dictionary.token2id)

        # %%
        corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]

        # %%
        tf_idf = gensim.models.TfidfModel(corpus)
        # for doc in tf_idf[corpus]:
            # print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])

        # %%
        # building the index
        sims = gensim.similarities.Similarity(r'C:\Users\Rizwan Local User\Documents\Guardian_Of_Truth\GuardianOfTruth_CommandLine',tf_idf[corpus],
                                                num_features=len(dictionary))

        # %%
        file2_docs = []

        f = query
        tokens = sent_tokenize(f)
        for line in tokens:
            file2_docs.append(line)

        # print("Number of documents:",len(file2_docs))  
        for line in file2_docs:
            query_doc = [w.lower() for w in word_tokenize(line)]
            query_doc_bow = dictionary.doc2bow(query_doc) #update an existing dictionary and create bag of words
        # # print(query_doc_bow)

        # %%
        # perform a similarity query against the corpus
        query_doc_tf_idf = tf_idf[query_doc_bow]
        # # print(document_number, document_similarity)
        result = sims[query_doc_tf_idf]
        # print('Comparing Result:', result) 

        # %%
        if flag==1:
            score = result[0]
        else:
            score = np.average(result)
        score = int(np.round(score*100))
        return score




