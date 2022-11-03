class ReplyTweet:
    def __init__(self, client):
        self.client = client

    def post_tweet(self, tweet_id, news_url): #tid = tweet_id | news_url = news article's URL
        self.status = self.client.update_status(status=news_url, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
