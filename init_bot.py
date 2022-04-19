# Author: Caden Kroonenberg
# Date: 12-2-21

import os

if __name__ == "__main__":
    mypath = 'data/'
    if not os.path.isdir(mypath):
        os.makedirs(mypath)

    with open('data/info.py', 'w') as f:
        username = input("What's your Twitter username?:\n>> ")
        print("")
        f.write("USERNAME = \'" + username + "\'\n\n")

        consumer_key = input("What's your Twitter consumer key?:\n>> ")
        print("")
        f.write("CONSUMER_KEY = \'" + consumer_key + "\'\n")

        consumer_secret = input("What's your Twitter consumer secret?:\n>> ")
        print("")
        f.write("CONSUMER_SECRET = \'" + consumer_secret + "\'\n")

        bearer_token = input("What's your Twitter bearer token?:\n>> ")
        print("")
        f.write("BEARER_TOKEN = \'" + bearer_token + "\'\n")
        
        access_key = input("What's your Twitter access key?:\n>> ")
        print("")
        f.write("ACCESS_KEY = \'" + access_key + "\'\n")

        access_secret = input("What's your Twitter access secret?:\n>> ")
        print("")
        f.write("ACCESS_SECRET = \'" + access_secret + "\'\n")

        sounds = ""
        while sounds != "y" and sounds != "n":
            sounds = input("Do you want your Twitter bot to make sounds when it tweets?: (Y)es or (N)o\n>> ").lower()
            if sounds != "y" and sounds != "n":
                print("\n\tERROR: Please input \'Y\' for Yes or \'N\' for No.\n")
        print("")
        if sounds == "y":
            f.write("\nTWEET_SOUNDS = True\n")
        else:
            f.write("\nTWEET_SOUNDS = False\n")

        texts = ""
        while texts != "y" and texts != "n":
            texts = input("Do you want to set up text updates through Twilio right now?: (Y)es or (N)o\n>> ").lower()
            if texts != "y" and texts != "n":
                print("\n\tERROR: Please input \'Y\' for Yes or \'N\' for No.\n")
        print("")
        if texts == "y":
            f.write("\nTEXT_UPDATES = True\n")
            twilio_sid = input("What's your Twilio account SID?:\n>> ")
            print("")
            f.write("TWILIO_SID = \'" + twilio_sid + "\'\n")
            twilio_auth = input("What's your Twilio auth token?:\n>> ")
            print("")
            f.write("TWILIO_AUTH = \'" + twilio_auth + "\'\n")
            twilio_phone_num = input("What's your Twilio phone #?:\t(Format: +10123456789)\n>> ")
            print("")
            f.write("TWILIO_PHONE_NUM = \'" + twilio_phone_num + "\'\n")
            user_num = input("What phone # should the bot send updates to?:\t(Format: +10123456789)\n>> ")
            print("")
            f.write("USER_PHONE_NUM = \'" + user_num + "\'\n")
        else:
            f.write("\nTEXT_UPDATES = False # To get this set up, set this value to True and see https://www.twilio.com/docs/sms/quickstart/python for the rest of the information.\n")
            print("If you want to set up text updates in the future, set TEXT_UPDATES to True in data/info.py, then fill in the other necessary info from Twilio")
            f.write("TWILIO_SID = \'YOUR TWILIO SID HERE\'\n")
            f.write("TWILIO_AUTH = \'YOUR TWILIO AUTH TOKEN HERE\'\n")
            f.write("TWILIO_PHONE_NUM = \'YOUR TWILIO PHONE NUMBER HERE\'\n")
            f.write("USER_PHONE_NUM = \'YOUR PERSONAL PHONE NUMBER HERE\' # Must be verified through the Twilio developer portal. See https://support.twilio.com/hc/en-us/articles/223180048-Adding-a-Verified-Phone-Number-or-Caller-ID-with-Twilio\n")

        f.close()
    try:
        with open('tweets.csv', 'x') as f:
            f.close()
    except:
        pass
    try:
        with open('data/log.json', 'x') as f:
            f.write("{\n\t\"tweets\": []\n}")
            f.close()
    except:
        pass