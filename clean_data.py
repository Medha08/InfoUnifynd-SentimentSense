# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 01:37:58 2018

@author: Saurabh
"""

import numpy as np

import pandas as pd
from textblob import TextBlob

import csv
import requests
import json
from datetime import date
import calendar
my_date = date.today()



url = 'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/latest?period_id=1DAY&limit=7'
headers = {'X-CoinAPI-Key' : 'B1F03F85-01B1-408C-A128-F39602EEB90D'}
response = requests.get(url, headers=headers)

text_parsed = json.loads(response.text)
c=0

with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ["Date", "OpenPrice", "ClosePrice", "Difference"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for x in text_parsed:
        y = (my_date.weekday()-c)%7
        writer.writerow({'Date': calendar.day_name[y][0:3], 'OpenPrice': x['price_open'],'ClosePrice':x['price_close'],'Difference':x['price_open']-x['price_close']})
        c= c+1

def find_Sentiment(filename = "temp.csv"):
    df = pd.read_csv(filename)
    sentiment_df = []
    for i in range(len(df)):
        temp = []
        analysis = TextBlob(df.iloc[i]['text'])
        usr = df.iloc[i]['username']
        day = df.iloc[i]['day']
        followers = df.iloc[i]['follower']
        retweet = df.iloc[i]['retweet']
        temp.append(usr)
        temp.append(day)
        temp.append(followers)
        temp.append(retweet)
        temp.append(analysis.sentiment.polarity)
        print (temp)
        sentiment_df.append(temp)
        
    print (sentiment_df) 
    
    return sentiment_df

def find_Correlation(sentiment_df,price_Change):
    
    Final_corr = {}
    
    for i in range(len(sentiment_df)):
        usr = sentiment_df[i][0]
        day = sentiment_df[i][1]
        follower = sentiment_df[i][2]
        retweet = sentiment_df[i][3]
        val = float(sentiment_df[i][4])
        diff = price_Change[price_Change['Date']==day]['Difference']
        val = val*diff
        try:
            Final_corr.update({usr:[Final_corr[usr][0] + val,Final_corr[usr][1]+1,follower,Final_corr[usr][3]+retweet]})
        except:
            Final_corr.update({usr:[val,1,0,0]})
    
    for i in Final_corr.keys():
        Final_corr[i][0] = Final_corr[i][0]/Final_corr[i][1]          
    
    return Final_corr
            
        
            
    
    

if __name__=='__main__':
    
    
    sentiment_df = find_Sentiment()
    price_Change = pd.read_csv('test.csv')
    
    
    Final_corr = find_Correlation(sentiment_df,price_Change)
    
    
    print (Final_corr)
    
    User_rank = {}
    
    for i in Final_corr.keys():
        User_rank.update({i:0.6*Final_corr[i][0]+0.2*Final_corr[i][2]+0.2*Final_corr[i][3]})
    import operator
    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    sorted_x = sorted(User_rank, key=operator.itemgetter(1))
    #rank = sorted(User_rank.values())
    print (sorted_x)    
    
    

