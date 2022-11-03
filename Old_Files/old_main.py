import tweepy
import json
from newsapi import NewsApiClient
import re
class TweepyAuthentication:
    """
    Used to obtain the correct type of tweepy Client object based on the purpose.
    """

    def __init__(self, version_2=True, api_key=None, api_key_secret=None,
        access_token=None, access_token_secret=None, keys_file=None):
        """
        Params
        -------
        api_key : string
            Think of this as the user name that represents your Twitter developer app.
            It is given during creation of developer account.
        
        api_key_secret : string
            Think of this as the password that represents your Twitter developer app.
            It is given during creation of developer account.

        access_token : string
            It specifies the Twitter account the request is made on behalf of.
            It is generated from developer portal.

        access_token_secret : secret
            It specifies the Twitter account the request is made on behalf of.
            It is generated from developer portal.
        """
        if keys_file is not None:
            keys = json.load(open(keys_file))
            if api_key is None:
                api_key = keys["API_KEY"]
            if api_key_secret is None:
                api_key_secret = keys["API_KEY_SECRET"]
            if access_token is None:
                access_token = keys["ACCESS_TOKEN"]
            if access_token_secret is None:
                access_token_secret = keys["ACCESS_TOKEN_SECRET"]

        if version_2:
            self.client = tweepy.Client(
                consumer_key=api_key,
                consumer_secret=api_key_secret,
                access_token=access_token,
                access_token_secret=access_token_secret
            )
        else:
            auth = tweepy.OAuth1UserHandler(
                consumer_key=api_key,
                consumer_secret=api_key_secret,
                access_token=access_token,
                access_token_secret=access_token_secret
            )
            self.client = tweepy.API(auth)

    def getClient(self):
        """
        Obtain the client represented by this object.
        
        Return
        -------
        tweepy.Client
        """
        return self.client


class ReferencedMentions:

    def __init__(self, client, user):
        self.client = client
        self.user = user

    def getResponse(self):
        response = self.client.get_users_mentions(
            id=self.user.data.id,
            tweet_fields='referenced_tweets',
            user_auth=True
        )
        return response
    
    def extract(self, response):
        mention_list = []
        for res in response.data:
            tweet_id = res.id
            if res.referenced_tweets is not None and res.referenced_tweets[0].type == "replied_to":
                referenced_tweet_id = res.referenced_tweets[0].id
                referenced_tweet_content = self.getTweetContent(referenced_tweet_id)
                mention_list.append((tweet_id, referenced_tweet_content))

        return mention_list

    def getMentions(self):
        response = self.getResponse()
        mention_list = self.extract(response)
        return mention_list


    def getTweetContent(self, tweet_id):
        tweet = self.client.get_tweet(tweet_id, user_auth=True)
        tweet_content = tweet.data.text
        return tweet_content


class NewsAPIAuthentication:
    def __init__(self, secret_key=None, keys_file=None):
        if secret_key is None and keys_file is not None:
            keys = json.load(open(keys_file))
            secret_key = keys["NEWS_API_SECRET"]
        
        self.client = NewsApiClient(api_key=secret_key)

    def getClient(self):
        return self.client

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

class ReplyTweet:
    def __init__(self, client):
        self.client = client

    def post_tweet(self, tweet_id, news_url): #tid = tweet_id | news_url = news article's URL
        self.status = self.client.update_status(status=news_url, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)


if __name__ == "__main__":
    client_v1 = TweepyAuthentication(version_2=False, keys_file="Keys.json").getClient()
    client_v2 = TweepyAuthentication(keys_file="Keys.json").getClient()
    client_news_api = NewsAPIAuthentication(keys_file="Keys.json").getClient()

    user = client_v2.get_user(username="got_truth101", user_auth=True)
    mentions = ReferencedMentions(client_v2, user).getMentions()
    
    news_fetch = NewsFetch(client_news_api, 1)

    reply_tweet = ReplyTweet(client_v1)

    process_tweet = ProcessTweet()

    for mention in mentions:
        tweet = mention[1]
        tweet = process_tweet.process(tweet)
        news_url = news_fetch.fetchNews(tweet)
        if news_url is not None:
            reply_tweet.post_tweet(mention[0], news_url)
        print((mention[0], news_url, tweet))
