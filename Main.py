from BertTransformer import BertTransformer
from FormNewsAPIQuery import FormNewsAPIQuery
from KeywordExtraction import KeywordExtraction
from TweepyAuthentication import TweepyAuthentication
from NewsAPIAuthentication import NewsAPIAuthentication
from ReferencedMentions import ReferencedMentions
from NewsFetch import NewsFetch
from ReplyTweet import ReplyTweet
from TweetPreprocessing import TweetPreprocessing
from sklearn.metrics.pairwise import cosine_similarity

if __name__ == "__main__":
    client_v1 = TweepyAuthentication(version_2=False, keys_file="Keys.json").getClient()
    client_v2 = TweepyAuthentication(keys_file="Keys.json").getClient()
    client_news_api = NewsAPIAuthentication(keys_file="Keys.json").getClient()
    user = client_v2.get_user(username="got_truth101", user_auth=True)
    mentions = ReferencedMentions(client_v2, user).getMentions()
    news_fetch = NewsFetch(client_news_api, 10)
    reply_tweet = ReplyTweet(client_v1)
    bert_model = BertTransformer()

    if mentions is not None:    
        for mention in mentions:
            tweet = mention[1]
            #print(tweet)
            processed_tweet = TweetPreprocessing().process(tweet=tweet).getProcessedTweet()
            #print(processed_tweet)
            keywords = KeywordExtraction().extractKeywords(processed_text=processed_tweet).getKeywords()
            #print(keywords)
            query = FormNewsAPIQuery().process(keywords=keywords).getQuery()
            #print(query)
            if query is not None:                 
                fetched_url_similarity = news_fetch.fetchNews(query, bert_model, processed_tweet)
                if fetched_url_similarity is not None:
                    (news_url, max_similar) = fetched_url_similarity
                    #term_freq = Term_Freq().find_term_freq(processed_tweet, description)
                    #sentence_embeddings = bert_model.encode(processed_tweet, news_description)
                    #imilarity = cosine_similarity([sentence_embeddings[0]], [sentence_embeddings[1]])[0][0]
                    if news_url is not None:
                        reply_tweet.post_tweet(mention[0], news_url, max_similar)
                    print((mention[0], news_url, tweet, max_similar))
