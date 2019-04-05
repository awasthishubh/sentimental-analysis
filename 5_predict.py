

import pandas as pd
import numpy as np
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

# searchqueries="Never Let Me Go"
searchqueries="RBI Policy"

users =tweepy.Cursor(api.search,q=searchqueries, tweet_mode='extended').items()
ftable = pd.read_csv('ftable.csv')
ftable = ftable.drop_duplicates(subset = 'word').reset_index(drop=True)
total_number = 200
count=0
pos=0
neg=0
while count < total_number:
    try:
        user = next(users)
        test = user._json['full_text']
        if(not user._json['lang'] == "en"): continue
        print(test)
        count+=1
        print(count,'\n')
        # test = 'I am sick. today.'
        # test = 'i dont know what to do anymore'
        # test='I recently participated in a hackathon organised my Apple Developers Group VIT. My teammates were Loukik and Ankit Bando and our team was named Ctrl-Alt-Elite :p It was a 36 hour hackathon and it took us around 3-4 hours to finally decide the problem statement and we were still unsure about it haha. We got placed for the most innovative idea award and I was at my happiest when I came to know about it even though I missed the award ceremony and was busy sleeping Just felt like thanking my teammates for being there with me throughout and keeping me pumped up and motivated Team Ctrl-Alt-Elite doesn\'t end here.'

        positive_instance = 24070.0#len(pd.read_csv('fun.csv')['text']) + len(pd.read_csv('happy.csv')['text'])
        negative_instance = 23930.0#len(pd.read_csv('sad.csv')['text']) + len(pd.read_csv('unhappy.csv')['text'])

        test_words = test.split()

        prob_positive = float(positive_instance/(positive_instance+negative_instance))
        prob_negative = 1 - prob_positive

        pos_word = 1.0*prob_positive
        neg_word = 1.0*prob_negative
        for i in range(len(test_words)):
            word = test_words[i]
            #print(word)
            index_val = ftable.index[ftable['word'] == word]
            if (len(index_val) > 0):
                #print(index_val[0])
                pos_val = ftable['positive'].iloc[index_val[0]]
                neg_val = ftable['negative'].iloc[index_val[0]]
                if(pos_val):
                    pos_word = pos_word * pos_val/positive_instance
                if(neg_val):
                    neg_word = neg_word * neg_val/negative_instance
        if pos_word > neg_word:
            pos+=1
        else:
            neg+=1
    except StopIteration:
        print('no more result')
        break
print('positive:',pos*100.0/(pos+neg))
print('negative:',neg*100.0/(pos+neg))
#print(pos_word)
#print(neg_word)



