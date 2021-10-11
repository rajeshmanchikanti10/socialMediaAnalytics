import numpy as np 
import pandas as pd 
import pymongo
from collections import Counter
import operator
import time
from datetime import datetime,timedelta
client=pymongo.MongoClient("mongodb+srv://KokilaReddy:KokilaReddy@cluster0.5nrpf.mongodb.net/Social_media_data?retryWrites=true&w=majority")
db=client['Social_media_data']
class Reddit:
    def __init__(self,brand,duration):
        self.reddit=db['reddit']
        self.brand=brand
        #timeforrequested
        minimumtime=datetime.now()-timedelta(days=duration)
        query={"tag":str(self.brand),"created_time":{"$gte":minimumtime}}
        result=self.reddit.find(query)
        df=pd.DataFrame(list(result))
        
        try:
            #creating newdf for required df
            dictonary=df['misc']
            new_df=pd.DataFrame(list(dictonary))
            
            self.new_df=new_df
        except:
            print(df)
            print("data doesn't exists!")

        self.df=df
        
    def hotTopicBaseOnCc(self):
        try:
            commment_max=self.new_df['comments_num'].max()
            hotTopic=self.new_df.loc[self.new_df['comments_num']==commment_max]
            return str(hotTopic.title)
        except:
            return ""
    
    def hotTopicBasedOnScore(self):
        try:
            upvotesmax=self.new_df["score"].max()
            hottopicscore=self.new_df[self.new_df['score']==upvotesmax]
            return str(hottopicscore.title)
        except:
            return ""
    

    def getSummary(self):
	

    def getNegativeQuestions(self):
        pass
