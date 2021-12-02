# Author: Caden Kroonenberg
# Date: 11-29-21

import csv
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

qrt_file = open(r"qrt.txt", "r+")
to_quote_id = qrt_file.read()

# reading csv file
with open(actions_url, 'r') as csvfile:
    actions = []
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
  
    # extracting each data row one by one
    for row in csvreader:
        actions.append(row[0])
  
    # get total number of actions
    if csvreader.line_num < day:
        print("Need new content!")

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

most_recent_tweet = client.get_users_tweets(id, max_results=1)[0][0]
most_recent_id = most_recent_tweet.id

# Overwrite qrt ID in qrt file
qrt_file.seek(0)
qrt_file.write(str(most_recent_id)) # TODO: Update ID
qrt_file.truncate()
qrt_file.close()