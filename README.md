# Guardian Of Truth

## Objective:
Our motive is to combat misinformation and disinformation on twitter. We want to help people by providing easy access to factual data related to the tweets they are reading on twitter. We aim to create a twitter bot that identifies trending content and the tweets containing facts related to that trending topic. After identifying the tweets, we look for news articles from multiple sources that deal with the same topic. We then rank the news articles based on an algorithm and the select the best one that is related to that tweet. We'll also use a prediction mechanism that gives a score for each tweet indicating the fakeness in a tweet. Finally, we will retweet along with the related news article and predicted score.

## Modules Description:
We have 2 main modules in the project along with 3 submodules for each module
1. Bot
- Fetching Tweets: Scraping data periodically using an API to access
trending tweets
- Fetching (related) Articles: Searching articles with high relatedness and
similarity of the fetched tweet using an API
- Post Tweets: Publish the truth score of the tweet
2. Algorithms
- Preprocessing: Bringing the tweet information to a form which can be
manipulated easily using stop word removal, tokenization etc.
- Comparison: Comparing related and similar factual articles along with
the tweet in hand to generate a truth score.
- Ranking: When searching for articles rank them based on most
similarity and relatedness

