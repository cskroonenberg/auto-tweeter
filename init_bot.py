# Author: Caden Kroonenberg
# Date: 12-2-21

if __name__ == "__main__":
    with open('data/addiction.txt', 'w') as f:
        addiction = input("What addiction are you quitting?:\n>> ")
        print("")
        f.write(addiction)
        f.close()

    with open('data/day.txt', 'w') as f:
        day = input("How many days have passed since you first quit? (If today's your first day, use 0):\n>> ")
        print("")
        f.write(day)
        f.close()

    with open('data/username.txt', 'w') as f:
        username = input("What's your twitter username?:\n>> ")
        print("")
        f.write(username)
        f.close()

    with open('data/qrt.txt', 'w') as f:
        f.write("0")
        f.close()
    
    with open('data/keys.py', 'w') as f:
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
        f.close()