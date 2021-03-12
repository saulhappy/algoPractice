"""
Not to be updated: start 
"""
import random
NUMBER_TWEETS_LAST_24_HOURS = 1000
class TwitterIterator:
    """
    Given a hashtag, this iterator will return all tweets,
    occurring over the last 24 hours which include the hashtag
    """

    def __init__(self, hashtag: str):
        """
        hashtag here is ignored, but we can imagine if this were
        a real implementation there would be an underlying Twitter Client
        """
        pass

    def __iter__(self):
        for i in range(0, NUMBER_TWEETS_LAST_24_HOURS):
            yield str(i)
"""
Not to be updated: end 
"""


## Implement this function ##
def random_tweet(hashtag):
    """
    Given all the tweets from the TwitterIterator pick one tweet
    at random to return
    """
    # return f"{random.randint(0, NUMBER_TWEETS_LAST_24_HOURS)} {hashtag}" 
    
    iterator = TwitterIterator(hashtag)
    tweet = ""
    # return random.randint(0, iterator.__sizeof__())iterator.hashtag

    for i in iterator:
        rand_num = random.randint(0, 1)
        if rand_num < 0.5:
            tweet = i
    
    return tweet

    # rand_num = random.randint(0, len(tweets))
    # return tweets[rand_num]


if __name__ == "__main__":
    print(random_tweet('test'))

