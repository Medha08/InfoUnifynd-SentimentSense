import requests
import re
import numpy as np

import pandas as pd
from textblob import TextBlob
import json

r = requests.get('https://newsapi.org/v2/top-headlines?sources=crypto-coins-news&apiKey=c7f7fc0490074243888cc544008bff3e')

# print(type(r.json()))
jsonData  = r.json()
newsData = []
for i in jsonData['articles']:
	#print("here")
	news = {}
	news["created_at"] = i["publishedAt"]
	text = re.sub(r'@\S+|https?://\S+', '', i["description"])
	cleaned = "".join(re.findall('[A-Z][^A-Z]*', text))
	tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",cleaned).split())
	news["description"] = tweet
	newsData.append(news)

#print(newsData)

def find_Sentiment():
    # df = pd.read_csv(filename)
    df = newsData
    sentiment_df = []
    print("DF",df)

    # for i in range(len(df)):
    # 	for j in range(len(df[i])):
    # 		#print("Here")
    # 		try:
    # 			temp = []
	    		
	   #  		analysis = TextBlob(news["description"])
	   #  		created_at = news["created_at"]
	   #  		temp.append(created_at)
	   #  		temp.append(analysis.sentiment.polarity)
	   #  		#print (temp[1])
	   #  		sentiment_df.append(temp)     


	   #  	except:
	   #  		print("Faulty Data")

        
    # print (sentiment_df) 
    
    # return sentiment_df


if __name__=='__main__':
	sentiment_df = find_Sentiment()