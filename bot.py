import schedule
import time
import data.info as info
# Execute bot.py
def tweet():
    print(time.ctime())
    exec(open("tweeter.py").read())

if __name__ == "__main__":
    # Execute interval (every day at 12 PM)
    schedule.every().day.at("12:00").do(tweet)
    print(time.ctime())
    print('Initializing \'' + info.USERNAME + '\' bot.')
    while 1:
        schedule.run_pending()
        time.sleep(1)
