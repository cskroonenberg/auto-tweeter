import schedule
import time

# Execute bot.py
def tweet():
    print(time.ctime())
    exec(open("bot.py").read())
    
if __name__ == "__main__":
    # Execute interval (every day at 12 PM)
    schedule.every().day.at("12:00").do(tweet)
    print(time.ctime())
    while 1:
        schedule.run_pending()
        time.sleep(1)
