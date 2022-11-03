from TweepyAuthentication import TweepyAuthentication
import json
import datetime

class ReferencedMentions:

    def __init__(self, client, user, time_file="MentionedTimestamp.json"):
        self.client = client
        self.user = user
        self._time_file = time_file

    def getResponse(self):
        last_retrieved_time = self.getLastRetrievedTime()
        response = self.client.get_users_mentions(
            id=self.user.data.id,
            tweet_fields=['referenced_tweets', 'created_at'],
            user_auth=True,
            start_time=last_retrieved_time
        )
        return response
    
    def extract(self, response):
        mention_list = []
        last_time = self.getLastRetrievedTime()
        if response.data is None:
            return None
        for res in response.data:
            tweet_id = res.id
            tweet_created_time = res.created_at
            if res.referenced_tweets is not None and res.referenced_tweets[0].type == "replied_to":
                referenced_tweet_id = res.referenced_tweets[0].id
                referenced_tweet_content = self.getTweetContent(referenced_tweet_id)
                mention_list.append((tweet_id, referenced_tweet_content))

            if tweet_created_time > last_time:
                last_time = tweet_created_time
            
        
        self.updateLastRetrievedTime(last_time)
        return mention_list

    def getMentions(self):
        response = self.getResponse()
        mention_list = self.extract(response)
        return mention_list


    def getTweetContent(self, tweet_id):
        tweet = self.client.get_tweet(tweet_id, user_auth=True)
        tweet_content = tweet.data.text
        return tweet_content

    def getLastRetrievedTime(self):
        times = json.load(open(self._time_file))
        last_retrieved_time = datetime.datetime.fromisoformat(times['last_retrived_time'])
        return last_retrieved_time

    def updateLastRetrievedTime(self, last_time):
        read_fp = open(self._time_file, mode="r")
        times = json.load(read_fp)
        write_fp = open(self._time_file, mode="w")
        
        one_second = datetime.timedelta(seconds=1)
        times['last_retrived_time'] = str(last_time+one_second)
        json.dump(times, write_fp, indent="")

if __name__ == "__main__":
    client_v2 = TweepyAuthentication(keys_file="Keys.json").getClient()
    user = client_v2.get_user(username="got_truth101", user_auth=True)
    referenced_mention = ReferencedMentions(client_v2, user).getMentions()
    print(referenced_mention)