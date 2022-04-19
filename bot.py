import schedule
import time
import data.info as info
import json
from tweeter import tweet
from text_client import send_text
# Execute bot.py
def send_tweet():
    print(time.ctime())
    body = tweet()
    # Update user when Tweet is sent out
    if info.TEXT_UPDATES:
        send_text('just Tweeted \"' + body + '\"')

if __name__ == "__main__":
    # Execute interval (every day at 12 PM)
    schedule.every().day.at("12:00").do(send_tweet)
    print(time.ctime())
    init_str = 'Initializing @' + info.USERNAME + ' bot.'
    # Update user when Twitter bot is started up
    if info.TEXT_UPDATES:
        send_text(init_str)
    print(init_str)
    while 1:
        schedule.run_pending()
        time.sleep(1)
