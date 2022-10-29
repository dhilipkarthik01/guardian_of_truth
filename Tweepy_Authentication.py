import tweepy
import json
class TweepyAuthentication:
    """
    Used to obtain the correct type of tweepy Client object based on the purpose.
    """

    def __init__(self, api_key=None, api_key_secret=None,
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

        self.client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_key_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

    def getClient(self):
        """
        Obtain the client represented by this object.
        
        Return
        -------
        tweepy.Client
        """
        return self.client

