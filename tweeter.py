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

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    client = tweepy.Client(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

    user = client.get_user(username=username)[0]
    id = user.id

    # Fetch day and QRT values
    tweet_no = int(fetch_val("data/tweet_no.txt"))
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
        if csvreader.line_num < tweet_no:
            print("Need more things to Tweet!\nExiting...")
            exit()

    to_tweet = str(actions[tweet_no])

    # Send tweet
    print("Tweeting \"" + to_tweet + "\"")
    if qrt_id == 0: # Root tweet
        tweet = client.create_tweet(text=to_tweet)
    else: # Quote RT
        tweet = client.create_tweet(text=to_tweet, quote_tweet_id=qrt_id)

    log_entry = {"text": tweet.text,
     "date-time": str(datetime.now()),
     "id": tweet.id,
     "quote_id": qrt_id
    }

    # Log the tweet
    log(log_entry)
    
    # Remove tweet from tweet queue
    remove_line("tweets.csv", 1)

    # Play tweet sound
    if info.TWEET_SOUNDS:
        playsound.playsound("assets/sounds/twit_notif.mp3")
    
    print("Tweet sent!")

    # Set day and QRT values for next script execution
    overwrite("data/qrt.txt", tweet.id)
    overwrite("data/tweet_no.txt", tweet_no+1)