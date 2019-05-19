import tweepy
import os
import pandas as pd

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRE')

q = input('enter the hashtag or keyword: ')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#create list to append tweets to
tweets = []

#append all tweet data to list
for tweet in tweepy.Cursor(api.search, q, count=1000000).items():
    tweets.append(tweet)

    #copnvert tweets list to pandas.Dataframe
tweets_df = pd.DataFrame(vars(tweets[i])
for i in range(len(tweets)))

#define file path to save teh csv file with the Data
FILE_PATH = 'tweets_data0.csv'

#use pandas to save dataframeot csv
tweets_df.to_csv(FILE_PATH)
