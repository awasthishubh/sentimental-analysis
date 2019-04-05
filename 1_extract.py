from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json
import time
import pandas as pd
import pprint
pp = pprint.PrettyPrinter(indent=4)

access_token = "86356hTdijZOc36-qM7Sl8A0syDXiR6RKecPipS60060cTIXDK"
access_secret = "n4zudWIGfHoEdVyQ7WuPfoVccib4cn6vCCO5D87az4EPg"
consumer_key = "ijzBxXnnIGWDZQ19JlgoLHQ6Y"
consumer_secret = "VLzOYuIR6OBVm5J4Yci4bwgSkmaAhLLjPmyhW0NGLnUEhXCily"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

searchqueries=["sad","unhappy","happy","fun"]
total_number = 50

for searchquery in searchqueries:
    print("\033[1;32;40m################################## Extracting Tweets by keyword \033[1;37;40m"+searchquery+"\033[1;32;40m ################################## \033[0m")
    users =tweepy.Cursor(api.search,q=searchquery, tweet_mode='extended').items()
    
    id= 1 if (searchquery in ["happy","fun"]) else 0
    text = [0] * total_number
    idvalues = [id] * total_number

    count=0
    while count < total_number:
        try:
            user = next(users)
        except tweepy.TweepError: #rate limiting occur
            print("sleeping....")
            time.sleep(60)
            user = next(users)
        try:
            text_value = user._json['full_text']
            language = user._json['lang']

            pp.pprint(text_value)
            print(language)
            
            if language == "en":
                text[count] = text_value
                count = count + 1
            print("current saved is:")
            print(count,'\n\n')

        except UnicodeEncodeError:
            print ("UnicodeEncodeError")


    print("Creating dataframe:")

    d = {"id": idvalues,"text": text, }
    df = pd.DataFrame(data = d)

    df.to_csv(searchquery+'.csv', header=True, index=False, encoding='utf-8')

    print ("completed")