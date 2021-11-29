# Author: Caden Kroonenberg
# Date: 11-29-21

from pandas import read_csv
import keys
import tweepy

# Init twitter user
CONSUMER_KEY = keys.CONSUMER_KEY
CONSUMER_SECRET = keys.CONSUMER_SECRET
ACCESS_KEY = keys.ACCESS_KEY
ACCESS_SECRET = keys.ACCESS_SECRET
BEARER_TOKEN = keys.BEARER_TOKEN

# Your username
username = 'og_ron_c_'

# CSV file where actions are stored (see sample_actions.csv)
actions_url = "actions.csv"

# Thing you're quitting
addiction_str = 'nicotine'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
client = tweepy.Client(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

user = client.get_user(username=username)[0]

id = user.id

# get date
day_file = open(r"day.txt", "r+")
day = int(day_file.read()) + 1

# load actions
names = ['action']
dataset = read_csv(actions_url, names=names)
actions = dataset.values[:,0]
action = str(actions[day])

# Create tweet string
to_tweet = "Day " + str(day) + " no " + addiction_str + ": " + action

# Tweet day and action
print("Tweeting \"" + to_tweet + "\"")
client.create_tweet(text=to_tweet)
print("Tweet sent!")

# Overwrite date in day file
day_file.seek(0)
day_file.write(str(day))
day_file.truncate()
day_file.close()