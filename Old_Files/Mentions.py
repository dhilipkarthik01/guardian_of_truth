import tweepy
import json
from TweepyAuthentication import TweepyAuthentication


class ReferencedMentions:
    def __init__(self, client, user):
        self.client = client
        self.user = user
    
    def getMentions(self, user_id):
        response = self.client.get_users_mentions(
            id=self.user.data.id,
            tweet_fields='referenced_tweets',
            user_auth=True
        )
    
        print(response)

if __name__ == "__main__":
    tweepy_auth = TweepyAuthentication(
        keys_file="Keys.json"
    )

    client = tweepy_auth.getClient()
    user = client.get_user(
        username="got_truth101",
        user_auth=True
    )
    print(user.data.id)
    res = client.get_users_mentions(
            id=user.data.id,
            tweet_fields='referenced_tweets',
            user_auth=True
        )
    print(res)
    for i in res.data:
        print(i.referenced_tweets)
    #mentions = ReferencedMentions(client)
    #mentions.getMentions(USER_ID)

    


    