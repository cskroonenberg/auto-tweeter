# Author: Caden Kroonenberg
# Date: 11-29-21

import csv
import data.info as info
import tweepy

# Init twitter user
CONSUMER_KEY = info.CONSUMER_KEY
CONSUMER_SECRET = info.CONSUMER_SECRET
ACCESS_KEY = info.ACCESS_KEY
ACCESS_SECRET = info.ACCESS_SECRET
BEARER_TOKEN = info.BEARER_TOKEN

# Your username
username = info.USERNAME

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
client = tweepy.Client(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

user = client.get_user(username=username)[0]

id = user.id

my_tweets = client.get_users_tweets(id, max_results=25)[0]

for tweet in my_tweets:
    print(str(tweet.id) + '\t' + str(tweet.text))
