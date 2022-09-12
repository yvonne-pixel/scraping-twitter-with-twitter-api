
# import required libraries

import tweepy
import configparser
import pandas as pd

# reading the config file

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key' ]
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret'] 
 
# authentication

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# create an api instance

api = tweepy.API(auth)

# fetch tweets from twitter home feed

public_tweets = api.home_timeline()

# storing the data in a dataframe

columns = ['Time', 'User_Name', 'Tweet']
data = []

for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name,tweet.text])
    
df = pd.DataFrame(data, columns=columns)
df.to_csv('twitter_data.csv')
