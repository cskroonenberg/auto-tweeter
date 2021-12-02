import schedule
import time

# Execute bot.py
def my_func():
    print(time.ctime())
    exec(open("bot.py").read())

# Execute interval (every day at 12 PM)
schedule.every().day.at("12:00").do(my_func)
print(time.ctime())
while 1:
    schedule.run_pending()
    time.sleep(1)