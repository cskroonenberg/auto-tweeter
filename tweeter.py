# Author: Caden Kroonenberg
# Date: 11-29-21

import csv
import data.info as info
import tweepy
import os
import playsound

def fetch_val(file_name):
    if not os.path.isfile(file_name):
        raise FileNotFoundError
    # get date
    file = open(file_name, "r+")
    val = file.read()
    file.close()
    return val

def overwrite(file_name, val):
    if not os.path.isfile(file_name):
        raise FileNotFoundError
    # Overwrite
    file = open(file_name, "r+")
    file.seek(0)
    file.write(str(val))
    file.truncate()
    file.close()
    return val

if __name__ == "__main__":
    # Init twitter user
    CONSUMER_KEY = info.CONSUMER_KEY
    CONSUMER_SECRET = info.CONSUMER_SECRET
    ACCESS_KEY = info.ACCESS_KEY
    ACCESS_SECRET = info.ACCESS_SECRET
    BEARER_TOKEN = info.BEARER_TOKEN

    # Your username
    username = info.USERNAME

    # CSV file where actions are stored (see sample_actions.csv)
    actions_url = "tweets.csv"

    # Thing you're quitting
    addiction_str = info.ADDICTION

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    client = tweepy.Client(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

    user = client.get_user(username=username)[0]
    id = user.id

    # Fetch day and QRT values
    day = int(fetch_val("data/day.txt")) + 1
    qrt_id = int(fetch_val("data/qrt.txt"))

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

    # Send tweet
    print("Tweeting \"" + to_tweet + "\"")
    if qrt_id == 0: # Root tweet
        client.create_tweet(text=to_tweet)
    else: # Quote RT
        client.create_tweet(text=to_tweet, quote_tweet_id=qrt_id)

    # Play tweet sound
    if info.TWEET_SOUNDS:
        playsound.playsound("assets/twit_notif.mp3")
    
    print("Tweet sent!")

    # Store ID of last tweet to use for Quote RTing next time.
    most_recent_tweet = client.get_users_tweets(id, max_results=5)[0][0]
    most_recent_id = most_recent_tweet.id

    # Set day and QRT values for next script execution
    overwrite("data/qrt.txt", most_recent_id)
    overwrite("data/day.txt", day)