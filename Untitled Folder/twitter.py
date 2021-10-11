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
class Twitter:
    def __init__(self,brand,duration):
        self.twitter=db['twitter']
        self.brand=brand
        #timeforrequested
        minimumtime=datetime.now()-timedelta(days=duration)
        query={"tag":str(self.brand),"created_time":{"$gte":minimumtime}}
        result=self.twitter.find(query)
        df=pd.DataFrame(list(result))
            
        #getting numer columns
        try:
            dictonary=df['misc']
            new_df=pd.DataFrame(list(dictonary))  
            self.new_df=new_df
        except:
            print(df)
            print("Data doesn't exists")
        self.df=df

    def findInfluentialUser(self):
        try:
            #print(self.new_df.retweet_count)
            retweet_countmax=self.new_df['retweet_count'].max()
            active_users=self.new_df[self.new_df["retweet_count"]==retweet_countmax]
            return list(active_users.user_name)
        except:
            return []
    def  HashTags(self):
        try:
            listofhashtags=[]
            re_hashtag=re.compile(r'#([^\s:]+)')
            for tweet in self.df['text']:
                listofhashtags.append(re_hashtag.findall(tweet))
            hashtags=[hashtag for list1 in listofhashtags for hashtag in list1]
            frequency=Counter(hashtags)
            return frequency
        except:
            return []
    def getMostDiscussedTopic(self):
        pass
    def getNegativeQuestions(self):
        pass
    