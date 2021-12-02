# Author: Caden Kroonenberg
# Date: 12-2-21

import os

if __name__ == "__main__":
    mypath = 'data/'
    if not os.path.isdir(mypath):
        os.makedirs(mypath)

    with open('data/info.py', 'w') as f:
        addiction = input("What addiction are you quitting?:\n>> ")
        print("")
        f.write("ADDICTION = \'" + addiction + "\'\n\n")

        with open('data/day.txt', 'w') as d:
            day = input("How many days have passed since you first quit? (If today's your first day, use 0):\n>> ")
            print("")
            d.write(day)
            d.close()
        
        username = input("What's your twitter username?:\n>> ")
        print("")
        f.write("USERNAME = \'" + username + "\'\n\n")

        consumer_key = input("What's your twitter consumer key?:\n>> ")
        print("")
        f.write("CONSUMER_KEY = \'" + consumer_key + "\'\n")

        consumer_secret = input("What's your twitter consumer secret?:\n>> ")
        print("")
        f.write("CONSUMER_SECRET = \'" + consumer_secret + "\'\n")

        bearer_token = input("What's your twitter bearer token?:\n>> ")
        print("")
        f.write("BEARER_TOKEN = \'" + bearer_token + "\'\n")
        
        access_key = input("What's your twitter access key?:\n>> ")
        print("")
        f.write("ACCESS_KEY = \'" + access_key + "\'\n")

        access_secret = input("What's your twitter access secret?:\n>> ")
        print("")
        f.write("ACCESS_SECRET = \'" + access_secret + "\'\n")

        sounds = ""
        while sounds != "y" and sounds != "n":
            sounds = input("Do you want your twitter bot to make sounds when it tweets?: (Y)es or (N)o\n>> ").lower()
            if sounds != "y" and sounds != "n":
                print("\n\tERROR: Please input \'Y\' for Yes or \'N\' for No.\n")
        print("")
        if sounds == "Y":
            f.write("\nTWEET_SOUNDS = True\n")
        else:
            f.write("\nTWEET_SOUNDS = False\n")

        f.close()

    with open('data/qrt.txt', 'w') as f:
        f.write("0")
        f.close()

    with open('tweets.csv', 'w') as f:
        f.close()