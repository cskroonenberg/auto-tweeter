# Author: Caden Kroonenberg
# Date: 12-2-21

import os

if __name__ == "__main__":
    mypath = 'data/'
    if not os.path.isdir(mypath):
        os.makedirs(mypath)

    with open('data/info.py', 'w') as f:
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
        if sounds == "y":
            f.write("\nTWEET_SOUNDS = True\n")
        else:
            f.write("\nTWEET_SOUNDS = False\n")

        f.close()
    try:
        with open('tweets.csv', 'x') as f:
            f.close()
    except:
        pass
    try:
        with open('log.json', 'x') as f:
            f.write("{\n\t\"tweets\": []\n}")
            f.close()
    except:
        pass