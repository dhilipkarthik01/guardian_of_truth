import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
class NewsFetch:

    def __init__(self, client, no_of_results = 10):
        self.no_of_results = no_of_results
        self.client = client
        

    def fetchNews(self, query, model, tweet):

        articles = self.getArticles(query)
        if articles is None:
            return None
        url_max_similar = self.compareArticles(model, tweet, articles)
        return url_max_similar

    def compareArticles(self, model, tweet, articles):
        descriptions = []
        for article in articles:
            descriptions.append(article['description'])
        #print(descriptions)
        embeddings = model.encode(tweet, descriptions)
        #print(embeddings.shape)
        similarities = cosine_similarity([embeddings[0]], embeddings[1:])[0]
        idx = np.argmax(similarities)
        #print(similarities)
        #print(idx)
        url = articles[idx]['url']
        max_similar = similarities[idx]
        return (url, max_similar)

    def getArticles(self, query):
        response = self.client.get_everything(
            q=query,
            page_size=self.no_of_results,
            sort_by='relevancy',
            language='en'
        )
        if len(response['articles']) == 0:
            return None
        else:
            return response['articles']