import tweepy
from Tweepy_Authentication import TweepyAuthentication

class ReferencedMentions:
    def __init__(self, client):
        self.client = client
    
    def getMentions(self, user_id):
        self.user_id = user_id
        
        response = self.client.get_users_mentions(
            id=self.user_id,
            expansions='referenced_tweets.id'
        )

        print(response)


API_KEY = "Ecq8C2SIYzXNXT6QM2zFJoXqf"
API_KEY_SECRET = "MqFZRV8Vykpo6EaKpjoFUPGcTS0UEP5i90lOWP3RnghjdsGopQ"
ACCESS_TOKEN = "1561265656020242434-p6bAYeAAqNQORlZRufbYt4d399gFrY"
ACCESS_TOKEN_SECRET = "q0YGuwwAVpRObIGUguNARKOLukpXODtsF1kB9KSbWWoig"
USERNAME = "got_truth101"
if __name__ == "__main__":
    tweepy_auth = TweepyAuthentication(
        api_key=API_KEY,
        api_key_secret=API_KEY_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    client = tweepy_auth.getClient()
    user = client.get_user(
        username=USERNAME,
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

    


    