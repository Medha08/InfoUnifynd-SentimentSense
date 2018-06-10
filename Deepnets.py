# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 12:30:26 2018

@author: Saurabh
"""

from keras.models import Sequential,Model
from keras.layers import Dense
from keras.optimizers import SGD
from keras.layers import Input,Dropout
import keras
import pandas as pd
import numpy as np
import pickle

class NN():
    def __init__(self):
        model = Sequential()
        model.add(Dense(4,input_shape = (40,)))
        #model.add(Dropout(0.2))
        optimizer = keras.optimizers.Adam(0.02,0.5)#, 0.5)
        model.add(Dense(4))
        model.add(Dropout(0.01))
        model.add(Dense(4))
        model.add(Dropout(0.01))
        model.add(Dense(2))
        #
        
        
        model.add(Dense(1))
        model.compile(loss= 'binary_crossentropy', optimizer = optimizer)
        print (model.summary())
        
        self.Model = model
        
    def train(self,train_data,y_labels,epoch,batch_size):
        
        self.Model.fit(train_data,y_labels,epochs = epoch,batch_size = batch_size)
   
def acct(actual,pred):
    loss = [actual[i]-pred[i] for i in range(len(actual))]
    return loss
def split_Data():
    #Read the DATA
    price_Change = pd.read_csv('test.csv')
    news_Data = pd.read_csv('News_SA_output.csv')
    tweet_Data = pd.read_csv('Top_Dataset_SA_Tweet.csv') 
    rank_mat = pd.read_csv('Influencers_Ranking.csv')
    tweet_test = pd.read_csv('test_data.csv')
    reddit_test = pd.read_csv('test_data_reddit.csv')
    news_test = pd.read_csv('test_data_news.csv')
    pos = 0 
    num  = 0
    
    train_data = np.zeros((7,40))
    test_data =  np.zeros((1,40))
    y_labels =  np.zeros((7,1))
    ty_labels =  np.zeros((1,1))
    
    
    pos = 0 
    num  = 0
    
    
    for t,i in tweet_test.iterrows():
        pos=pos+int(i['Sentiment'])
        num+=1
    pos = pos/num
    pos = pos*10
    
    for i in range(5,5+int(pos)):
        test_data[0][i] = 1
        
    
    pos = 0 
    num  = 0
    
    
    for t,i in reddit_test.iterrows():
        pos=pos+int(i['Sentiment'])
        num+=1
    pos = pos/num
    pos = pos*5
    
    for i in range(35,5+int(pos)):
        test_data[0][i] = 1
        
    pos = 0 
    num  = 0
    
    
    for t,i in news_test.iterrows():
        pos=pos+int(i['Sentiment'])
        num+=1
    pos = pos/num
    pos = pos*5
    
    for i in range(0,5+int(pos)):
        test_data[0][i] = 1
        
        
    ty_labels = 193.81
    
    
    '''I need to divide it by two '''
    tweet_Data['values'] = tweet_Data['values']/2    
    news_Data = news_Data.reset_index(drop=True)
    tweet_Data = tweet_Data.reset_index(drop=True)
    reddit_Data = pd.read_csv('reddit_analysis.csv')
    Days = ['Mon','Tue','Wed' ,'Thu','Fri','Sat','Sun']
    #print (rank_mat)
    
    even  = 0
    odd = 0
    for i in range(len(Days)):
        if (i%2==0 or i%2==1)  :
            indexs = reddit_Data[reddit_Data['Day']==Days[i]].index
            qw = 35
            for index in indexs:
                train_data[even][qw] += reddit_Data.loc[index]['values']
                qw+=1
            y_labels[even] = (price_Change[price_Change['Date']==Days[i]]['Difference'])
            even+=1
        
    even  = 0
    odd = 0      
    for i in range(len(Days)):
        if (i%2==0 or i%2==1)  :
            indexs = news_Data[news_Data['Date']==Days[i]].index
            qw = 0
            for index in indexs:
                train_data[even][index] += news_Data.loc[index]['values']
                qw+=1
            y_labels[even] = (price_Change[price_Change['Date']==Days[i]]['Difference'])
            even+=1
        
    
    
            
    even  = 0
    odd = 0
    for i in range(len(Days)):
        if (i%2==0 or i%2==1) and i!=5:
            indexs = tweet_Data[tweet_Data['Date']==Days[i]].index
            
            for e in indexs:
                N = tweet_Data.loc[e]['name']
                e = 0
                for t in range(30):
                    if rank_mat.loc[t]['username']==N:
                        e = t
                        break
                print (N)
                #print (ind)
                e = e+5
                train_data[even][e] += tweet_Data.loc[e]['values']
            #y_labels.append(price_Change[price_Change['Date']==Days[i]]['Difference'])
            even+=1
        
    return train_data,y_labels,test_data,ty_labels
            
     
if __name__=='__main__':
    deepnets = NN()
    train_data, y_labels,test_data, ty_labels = split_Data()
    Days = ['Mon','Tue','Wed' ,'Thu','Fri','Sat','Sun']
    avg_sentiment_per_day = {}
    print (train_data)
    a = 0
    for i in train_data:
        t  = 0
        for j in i:
            print (j)
            t+=j
        t/=5
        avg_sentiment_per_day[Days[a]] = t
        a+=1
        
    with open('obj' + '.pkl', 'wb') as f:
        pickle.dump(avg_sentiment_per_day, f, pickle.HIGHEST_PROTOCOL)
        
            
        
    
    
    deepnets.train(train_data,y_labels,1000,2)
    
    print (ty_labels)
    
    
    Pred = deepnets.Model.predict(test_data)
    
    print (Pred)
    
    print (avg_sentiment_per_day)
    
    

        
        
        
        
        