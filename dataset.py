import numpy as np
import pandas as pd
import tweepy
import csv
from datetime import date
import calendar
my_date = date.today()
import re
import json

####input your credentials here
consumer_key = 'mFE0Dl9pfPq7w2UEAC17Hwa3q'
consumer_secret = 'yyXGtQ7xoWiiY0MdtEOHUWSm4F5z77mkZ8Zljpj4UoIdmUwvl6'
access_token = '1005170408159473664-WWRYYruJqgAU0e6i5e1qgiqHz1zi3X'
access_token_secret = 'wNfSYM35T1gzJv0jnz5nsDSuz1jSHCv6myK2b6Gtwu7mO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
try:
    csvFile = open('ua.csv', 'a')
    csvWriter = csv.writer(csvFile)
except:
    print("Could not load file")


# try:
status = tweepy.Cursor(api.search,q="#bitcoin",lang="en").items(5000)
# rt = json.load(status._json)
# print(status.items())
# RT
c=0
for tweet in status:
    text = tweet._json["text"]
    y = (my_date.weekday()-c)%7
    csvWriter.writerow([calendar.day_name[y][0:3], tweet._json["user"]["name"], text, tweet._json["user"]["followers_count"], tweet._json["user"]["verified"], tweet._json["retweet_count"], tweet._json["favorite_count"]])
    c=c+1

# AC
c=0
for gg in tweepy.Cursor(api.search,q="#bitcoin",lang="en").items(5000):
	# print("here")
	y = (my_date.weekday()-c)%7
	if 'retweeted_status' in tweet._json.keys():
		text = tweet._json["retweeted_status"]["text"]
		print(text)
		csvWriter.writerow([calendar.day_name[y][0:3], tweet._json["retweeted_status"]["user"]["name"], text, tweet._json["retweeted_status"]["user"]["followers_count"], tweet._json["retweeted_status"]["user"]["verified"], tweet._json["retweeted_status"]["retweet_count"], tweet._json["retweeted_status"]["favorite_count"]])
		c=c+1

# except:
#     print("Failed to process")
# csvFile.close()
