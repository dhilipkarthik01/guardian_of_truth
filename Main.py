from FormNewsAPIQuery import FormNewsAPIQuery
from KeywordExtraction import KeywordExtraction
from TweepyAuthentication import TweepyAuthentication
from NewsAPIAuthentication import NewsAPIAuthentication
from ReferencedMentions import ReferencedMentions
from NewsFetch import NewsFetch
from ReplyTweet import ReplyTweet
from TweetPreprocessing import TweetPreprocessing

if __name__ == "__main__":
    client_v1 = TweepyAuthentication(version_2=False, keys_file="Keys.json").getClient()
    client_v2 = TweepyAuthentication(keys_file="Keys.json").getClient()
    client_news_api = NewsAPIAuthentication(keys_file="Keys.json").getClient()
    user = client_v2.get_user(username="got_truth101", user_auth=True)
    mentions = ReferencedMentions(client_v2, user).getMentions()
    news_fetch = NewsFetch(client_news_api, 1)
    reply_tweet = ReplyTweet(client_v1)

    if mentions is not None:    
        for mention in mentions:
            tweet = mention[1]
            print(tweet)
            processed_tweet = TweetPreprocessing().process(tweet=tweet).getProcessedTweet()
            print(processed_tweet)
            keywords = KeywordExtraction().extractKeywords(processed_text=processed_tweet).getKeywords()
            print(keywords)
            query = FormNewsAPIQuery().process(keywords=keywords).getQuery()
            print(query)
            if query is not None:                 
                news_url = news_fetch.fetchNews(query)
                if news_url is not None:
                    reply_tweet.post_tweet(mention[0], news_url)
                print((mention[0], news_url, tweet))
