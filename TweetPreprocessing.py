import re
class TweetPreprocessing:
    def __init__(self):
        pass
    
    def process(self, tweet):
        self.tweet = tweet
        self.removeHashtagsMentions()
        self.removeEmojis()
        self.removeLinks()
        self.removeWhitespaceCharacters()
        self.removeSpecialCharacters()
        return self

    def removeEmojis(self):
        regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
        self.tweet = regrex_pattern.sub(r'', self.tweet)
    
    def removeLinks(self):
        regex_pattern = re.compile(pattern=r"http\S+|www.\S+", flags=re.UNICODE)
        self.tweet = regex_pattern.sub(r'', self.tweet)
    
    def removeHashtagsMentions(self):
        regex_pattern = re.compile(pattern=r"@[A-Za-z0-9_]+|#[A-Za-z0-9_]+", flags=re.UNICODE)
        self.tweet = regex_pattern.sub(r'', self.tweet)
    
    def removeWhitespaceCharacters(self):
        regex_pattern = re.compile(pattern=r"\s", flags=re.UNICODE)
        self.tweet = regex_pattern.sub(r' ', self.tweet)
        regex_pattern = re.compile(pattern=r"\s{2,}", flags=re.UNICODE)
        self.tweet = regex_pattern.sub(r' ', self.tweet)

    def removeSpecialCharacters(self):
        regex_pattern = re.compile(pattern=r"[^\w., '\-]", flags=re.UNICODE)
        self.tweet = regex_pattern.sub(r'', self.tweet)

    def getProcessedTweet(self):
        return self.tweet


    