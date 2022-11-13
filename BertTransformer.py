from sentence_transformers import SentenceTransformer

class BertTransformer:
    
    def __init__(self):
        self.model = SentenceTransformer('bert-base-nli-mean-tokens')

    def getModel(self):
        return self.model

    def encode(self, tweet, articles):
        li = []
        li.append(tweet)
        sentense_embeddings = self.model.encode(li + articles)
        return sentense_embeddings