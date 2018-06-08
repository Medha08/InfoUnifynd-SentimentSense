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

for tweet in tweepy.Cursor(api.search,q="#cryptocurrency",count=100,lang="en").items():
                        print (tweet.created_at, tweet.text)
                        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
        

for tweet in tweepy.Cursor(api.search,q="#bitcoin",count=100,lang="en").items():
                        print (tweet.created_at, tweet.text)
                        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
        