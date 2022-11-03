from newsapi import NewsApiClient
import json

class NewsAPIAuthentication:
    def __init__(self, secret_key=None, keys_file=None):
        if secret_key is None and keys_file is not None:
            keys = json.load(open(keys_file))
            secret_key = keys["NEWS_API_SECRET"]
        
        self.client = NewsApiClient(api_key=secret_key)

    def getClient(self):
        return self.client