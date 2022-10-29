import tweepy

class Retweet:
    def post_tweet(self, auth, tid, news_url): #tid = tweet_id | news_url = news article's URL
        self.api = tweepy.API(auth)
        self.status = self.api.update_status(status=news_url, in_reply_to_status_id=tid, auto_populate_reply_metadata=True)

if __name__ == "__main__":
    # do something
