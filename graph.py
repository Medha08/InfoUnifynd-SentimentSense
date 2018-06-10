# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 09:15:36 2018

@author: Saurabh
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
price_Change = pd.read_csv('test.csv')

X = range(8)
print (X)

weekdays_dic ={'Sun' :7 , 'Mon':6 ,'Tue':5, 'Wed':4,'Thu':3,'Fri':2,'Sat':1}
dataset =pd.read_csv('Data_Set.csv')
Y = np.zeros((7,1))

for i,row in dataset.iterrows():
    d = row['created_at']
    #print (d)
    Y[weekdays_dic[d]-1] +=row['retweet_count']

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()


XX = price_Change['Difference']
XX = np.absolute(XX)
Z = Y
XX = XX.values.reshape(len(XX),1)
Z = Z.reshape(len(Z),1)
    #print ('\n\n\n\n\n',Y)

diff = scaler.fit_transform(XX)
    
retweet = scaler.fit_transform(Z)

diff = diff.flatten()
retweet = retweet.flatten()

print (len(retweet))

plt.plot([0,1,2,3,4,5,6],diff,label = 'Difference in Price')
plt.plot([0,1,2,3,4,5,6],retweet,label = 'Retweet Number') 

plt.show()

