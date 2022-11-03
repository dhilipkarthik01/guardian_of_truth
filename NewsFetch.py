class NewsFetch:

    def __init__(self, client, no_of_results = 10):
        self.no_of_results = no_of_results
        self.client = client
        

    def fetchNews(self, query):

        response = self.client.get_everything(
            q=query,
            page_size=self.no_of_results,
            sort_by='relevancy',
            language='en'
        )
        if len(response['articles']) == 0:
            return None
        else:
            return response['articles'][0]['url']
