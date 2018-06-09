# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 01:10:08 2018

@author: Saurabh
"""


import tweepy
import csv
import pandas as pd
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
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
searched_tweets = [status for status in tweepy.Cursor(api.search, q='#Crypto').items(10)]
# print(searched_tweets)
for tweet in searched_tweets:
	# print("here")
	print(tweet._json["user"]["name"])
	# print("\n")
	csvWriter.writerow([tweet.user.name, tweet._json["text"]])

# for tweet in tweepy.Cursor(api.search,q="#cryptocurrency",count=10,lang="en").items():
#     print("here")
#     csvWriter.writerow([tweet.user.name, tweet._json["text"]])

for tweet in tweepy.Cursor(api.search,q="#cryptocurrency -filter:retweets",count=100,lang="en").items():
# 		                        # print (tweet.created_at, tweet.user._json["screen_name"], tweet.text)
		                        print("here")
# 		                        print("\n")
# 		                        csvWriter.writerow([tweet.created_at, tweet.text])
# 		                        break
        

# status = tweepy.Cursor(api.search,q="#bitcoin",count=100,lang="en").items():
#                         print (tweet.created_at, tweet.text, tweet.user._json["screen_name"])
                        # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
                        # break