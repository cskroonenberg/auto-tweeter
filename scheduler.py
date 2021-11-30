# Author: Caden Kroonenberg
# Date: 11-29-21
import schedule
import time

# Execute bot.py
def my_func():
    current_time = time.ctime()
    print("Time: " + current_time)
    exec(open("bot.py").read())

# Execute interval (every day at 10 PM)
schedule.every().day.at("22:00").do(my_func)

while 1:
    schedule.run_pending()
    time.sleep(1)
