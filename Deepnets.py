x# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 12:30:26 2018

@author: Saurabh
"""

from keras.models import Sequential,Model
from keras.layers import Dense
from keras.optimizers import Adam
from keras.layers import Input

class NN():
    def __init__(self):
        model = Sequential()
        model.add(Dense(4,intput_shape = (1,)))
        model.Dropout(0.2)
        optimizer = Adam(0.0002, 0.5)
        model.add(Dense(2,activation = 'tanh'))
        model.Dropout(0.2)
        
        
        model.add(Dense(1,activation = 'sigmoid'))
        model.compile(loss= 'binary_crossentropy', optimizer = optimizer)
        print (model.summary())
        
        inp = Input(128,)
        
        out = model(inp)
        
        self.Model = Model(inp,out)
        
    def train(self,train_data,y_labels,epoch,batch_size):
        
        self.Model.fit(train_data,y_labels,epochs = epoch,batch_size =batch_size)
   
def acct(actual,pred):
    loss = [actual[i]-pred[i] for i in range(len(actual))]
    return loss
def split_Data():
    
     
if __name__=='__main__':
    deepnets = NN()
    train_data, y_labels,test_data, ty_data = split_Data()
    deepnets.train()
    
    Pred = deepnets.Model.predict(test_Data)
    
    print ("Loss : ",acct(ty_data,Pred))
    
    

        
        
        
        
        