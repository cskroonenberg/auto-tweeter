# Author: Caden Kroonenberg
# Date: 11-29-21

import csv
import data.info as info
import tweepy
import os
import playsound
import time
import json
from datetime import datetime
import text_client

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

# function to add to JSON
def log(new_data, filename='data/log.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data['tweets'].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def fetch_qrt():
    with open("data/log.json",'r+') as file:
        # Load tweet log:
        file_data = json.load(file)
        if len(file_data) == 0: # If no tweets have been tweeted yet:
            return 0
        # Return ID of last tweet and close file
        id = file_data['tweets'][-1]['id']
        file.close()
        return id

# Remove a line from a file
def remove_line(fileName,lineToSkip):
    with open(fileName,'r') as read_file:
        lines = read_file.readlines()

    currentLine = 1
    with open(fileName,'w') as write_file:
        for line in lines:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)
	
            currentLine += 1

def tweet():
    # Init twitter user
    CONSUMER_KEY = info.CONSUMER_KEY
    CONSUMER_SECRET = info.CONSUMER_SECRET
    ACCESS_KEY = info.ACCESS_KEY
    ACCESS_SECRET = info.ACCESS_SECRET
    BEARER_TOKEN = info.BEARER_TOKEN

    # Your username
    username = info.USERNAME

    # CSV file where tweets are stored (see sample_actions.csv)
    tweets = "tweets.csv"

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    client = tweepy.Client(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

    user = client.get_user(username=username)[0]
    id = user.id

    # Fetch QRT ID and tweet text
    qrt_id = fetch_qrt()
    with open("tweets.csv") as f:
        to_tweet = f.readline().rstrip()

    # Send tweet
    print("Tweeting \"" + to_tweet + "\"")
    if qrt_id == 0: # Root tweet
        tweet = client.create_tweet(text=to_tweet).data
    else: # Quote RT
        tweet = client.create_tweet(text=to_tweet, quote_tweet_id=qrt_id).data

    log_entry = {"text": tweet['text'],
     "date-time": str(datetime.now()),
     "id": int(tweet['id']),
     "quote_id": int(qrt_id)
    }

    # Log the tweet
    log(log_entry)

    # Remove tweet from tweet queue
    remove_line("tweets.csv", 1)

    # Play tweet sound
    if info.TWEET_SOUNDS:
        playsound.playsound("assets/sounds/twit_notif.mp3")
    
    print("Tweet sent!")
    return to_tweet

# Send Tweet manually by executing this Python script
if __name__ == "__main__":
    body = tweet()
    if info.TEXT_UPDATES:
        text_client.send_text('just Tweeted \"' + body + '\"')
