import numpy as np 
import pandas as pd 
import pymongo
from collections import Counter
import operator
import time
from datetime import datetime,timedelta
import re
client=pymongo.MongoClient("mongodb+srv://KokilaReddy:KokilaReddy@cluster0.5nrpf.mongodb.net/Social_media_data?retryWrites=true&w=majority")
db=client['Social_media_data']
class YouTube:
    def __init__(self,brand,duration):
        self.youtube=db['youTube']
        self.brand=brand
        #time for requested 
        minimumtime=datetime.now()-timedelta(days=duration)
        query={"tag":str(self.brand),"created_time":{"$gte":minimumtime}}
        result=self.youtube.find(query)
        df=pd.DataFrame(list(result))

        #getting numeric columns
        try:
            dictonary=df['misc']
            numeric_df=pd.DataFrame(list(dictonary))
            
            self.numeric_df=numeric_df
        except:
            print(df)
            print("data doesn't exists!")
        self.df=df
        
    def getHashTags(self):
        try:
            self.tags=[tag for list1 in self.numeric_df['tags'] for tag in list1]
            frequency=Counter(self.tags)
            #frequency=sorted(frequency.items(),key=operator.itemgetter(1),reverse=True)
            #top15=dict(frequency[:15])
            return frequency
        except:
            return []
    
    def InfluencingChannels(self,num=10):
        try:
            likecount=self.numeric_df[['channelTitle','likeCount']]
            sorted_values=likecount.sort_values('likeCount',axis=0,ascending=False)
            top_values=sorted_values.iloc[:num]
            return top_values.to_dict('records')
        except:
            return []
    
    def ChannelsWithMoreDiscussions(self,num=10):
        try:
            commentCount=self.numeric_df[['channelTitle','commentCount']]
            sorted_values=commentCount.sort_values('commentCount',axis=0,ascending=False)
            top_values=sorted_values.iloc[:num]
            return top_values.to_dict('records')
        except:
            return []

    def categoriesOfMentions(self):
        try:
            categorycount={}
            for i in self.numeric_df.index:
                if self.numeric_df['category'][i] in categorycount:
                    categorycount[self.numeric_df['category'][i]]+=1
            else:
                    categorycount[self.numeric_df['category'][i]]=0
            return categorycount
        except:
            return []
    def MostDiscussed(self):
        pass
    	
        
    def negativeQuestions(self):
        pass
