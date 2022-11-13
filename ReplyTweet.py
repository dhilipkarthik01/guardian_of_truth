class ReplyTweet:
    def __init__(self, client):
        self.client = client

    def post_tweet(self, tweet_id, news_url, similarity=0): #tid = tweet_id | news_url = news article's URL
        reply_tweet = "Similarity: " + str(round(similarity * 100)) + "%\n" + news_url 
        self.status = self.client.update_status(status=reply_tweet, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
